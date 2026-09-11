"""server_denylist：server 指向公共测试/基准服务或已知投毒域名 → REJECT。

清单分三段（内置硬编码，保证始终拦截；config 可追加，追加项不覆盖内置）：

- A1-1 测速站（注册域末两段精确匹配）：Ookla / Cloudflare / Netflix 等测速
  服务域名，只提供测速功能、绝不承载代理。投毒节点常用测速域名伪装 server。
- A1-2 连通性检测（完整 host 精确匹配）：系统级网络检测端点
  （Android 连通性检查、Apple 网络验证等），同样绝无可能承载代理。
  必须用完整 host 匹配——若用注册域匹配会把整个 cloudflare.com / google.com /
  apple.com 拦掉，误伤 Reality 节点的 sni 与 CDN 中转。
- A2 已知投毒域名（注册域末两段精确匹配）：从历史输出样本提取的投毒者
  批量注册域名（随机子域 + 非标端口 + 知名站 sni）。投毒者更换密码/标记
  仍可用域名兜底拦截；"换域名"的新投毒由 suspicious_pattern 规则覆盖。

双模式匹配的原因：
- 独立注册域用"末两段"精确匹配（含任意子域），绝不用子串匹配，
  防止 speedtesty.xyz / myspeedtest.net 这类合法注册域被误伤。
- 知名服务子域用"完整 host"精确匹配，防止误杀整个品牌域。
"""
from __future__ import annotations

from ..common.domain import reg_domain
from ..common.enums import RejectReason, RuleCategory
from ..common.node import Node
from .base import Rule, RuleResult

# ── A1-1 测速站（注册域末两段精确匹配）───────────────────────────────
# 注意: speed.cloudflare.com 不在此清单（其注册域为 cloudflare.com，
# 放入会用注册域匹配误杀整个 cloudflare.com），它走下方完整 host 匹配。
_SPEEDTEST_DOMAINS = frozenset({
    "speedtest.net",        # Ookla
    "speedtest.org",
    "speedtestcustom.com",  # Ookla 自定义测速
    "speedtest.com.cn",     # Ookla 中国版（世纪互联）
    "fast.com",             # Netflix
    "openspeedtest.com",
    "speedcheck.org",
    "speedof.me",
    "nperf.com",
    "testmy.net",
    "meter.net",
    "librespeed.org",       # 开源测速软件
})

# ── A1-2 连通性检测（完整 host 精确匹配）───────────────────────────────
# 系统级"网络是否可用"检测端点；投毒者常伪装成这些域名。
_CONNECTIVITY_HOSTS = frozenset({
    "speed.cloudflare.com",      # Cloudflare 测速
    "cp.cloudflare.com",         # Cloudflare 连接测试（generate_204）
    "connectivitycheck.gstatic.com",  # Android 网络检测
    "clients3.google.com",       # Google 204 检测
    "captive.apple.com",         # Apple 网络验证
    "detectportal.firefox.com",  # Firefox 门户检测
    "neverssl.com",              # HTTP 重定向测试
})

# ── A2 已知投毒域名（注册域末两段精确匹配）────────────────────────────
# 来源：当前输出样本全量提取（形态确认 + banv2ray 铁证），
# 均为"随机子域 + 非标端口 + 知名站 sni"的投毒形态。
_POISON_DOMAINS = frozenset({
    "admni.ir", "auragg.org", "barnikle1.me", "belzema.ir", "berzema.ir",
    "blueheartz.ir", "by-api-yandex.com", "carpetsart.ir", "cdnnow.xyz",
    "cloakify.app", "clonecloudcenter.ir", "cloudpooya.ir", "consolgame.ir",
    "contigolibre.com", "cyberdeepsea.top", "dearhossein-taktaz.ir",
    "dop999.com", "dopweed.com", "football-player.ir", "frost-api.com",
    "gjtxyszcicaly.com", "greewebservices.ir", "gxsdfewocinexuxiqee.com",
    "hchdhsbs12gd.ir", "healingfluence.org", "iranfreemarz.com",
    "iranlast.com", "jumperservice.com", "kfc-520.com", "korvexe.ir",
    "kvnfreetest.uk", "loriq.site", "lorluma.ir", "mahkocholo.com",
    "maktabmotahari.ir", "maps-yandex.com", "maps-yandex.net",
    "marzban-locations.com", "mbcloudy.ir", "mbcloudynias.ir",
    "mbmovietime.ir", "mobile-shahab.ir", "mobleamiri10.ir",
    "monopolitass.ir", "murphyweb.sbs", "nenenet1.ir", "netraidly.ru",
    "onavinet.ir", "oorluma.ir", "opik.net", "outforyou.ir", "panelbaz.com",
    "poki-pakipon.ir", "ramcalshoping.ir", "relqino.ir",
    "restaurantbomb.com", "safire-soleiman.ir", "sbrf-cdn342.ru",
    "serendpiti.ir", "service-panelbaz.ir", "slovovpn.com", "sorcepack.ir",
    "ssdhdd.org", "vpn-sword-art.online", "vtret.com", "wargen-alkaline.ir",
    "whooisthebest.ir", "xanka.best", "zestmarket.ir",
})

_REG_DENYLIST = _SPEEDTEST_DOMAINS | _POISON_DOMAINS


class ServerDenylistRule(Rule):
    rule_id = "server_denylist"
    category = RuleCategory.VALIDITY

    def __init__(
        self,
        extra_domains: list[str] | None = None,
        extra_hosts: list[str] | None = None,
    ) -> None:
        """extra_domains: 追加注册域（末两段匹配）；extra_hosts: 追加完整 host 精确匹配。"""
        self._reg = set(_REG_DENYLIST)
        self._hosts = set(_CONNECTIVITY_HOSTS)
        if extra_domains:
            self._reg.update(d.strip().lower() for d in extra_domains if d and d.strip())
        if extra_hosts:
            self._hosts.update(h.strip().lower() for h in extra_hosts if h and h.strip())

    def evaluate(self, node: Node) -> RuleResult:
        server = (node.server or "").strip().lower()
        if not server or ":" in server:
            return RuleResult.pass_()  # 空 / IPv6 不适用
        # 完整 host 精确匹配（连通性检测等知名服务子域）
        if server in self._hosts:
            return RuleResult.reject(RejectReason.FAKE_SERVER)
        # 注册域末两段精确匹配（测速站 + 已知投毒域名）
        if reg_domain(server) in self._reg:
            return RuleResult.reject(RejectReason.FAKE_SERVER)
        return RuleResult.pass_()
