# sub-sift 运行报告

- 运行时间: 2026-08-20 16:25:27 CST
- 主清单订阅链接数: 177
- 本次实际拉取: 177（冷却/禁用跳过: 0）
- 拉取成功: 169，失败: 8
- 有效节点数（筛选后去重前）: 54449
- 输出节点数（去重后）: 11950
- GeoIP 数据源: mmdb: data/GeoLite2-Country.mmdb
- 输出文件: output/v2ray.txt, output/plain.txt

## 规则计数器
| 规则 | 拒绝数 |
|---|---|
| 协议过滤 | 31014 |
| 字段有效性 | 5484 |
| 假节点域名 | 4364 |
| 投毒形态 | 96 |
| vmess 安全 | 24583 |
| vless 安全 | 70295 |
| trojan 安全 | 31271 |
| 地区过滤 | 74689 |
| **合计** | **241796** |

## 主清单（active → 冷却 → disabled；组内按 avg 降序）
| 链接 | 状态 | 成功率 | 最近 | 平均 | 被拒 |
|---|---|---|:---:|---|---|
| https://raw.githubusercontent.com/ebrasha/free-v2ray-public-list/refs/heads/main/all_extracted_configs.txt | active | 3/3 | 10054 | 10031.0 | 38101 |
| https://raw.githubusercontent.com/DukeMehdi/FreeList-V2ray-Configs/refs/heads/main/Configs/VLESS-DukeMehdi-Configs.txt | active | 3/3 | 6486 | 6486.0 | 22439 |
| https://raw.githubusercontent.com/mheidari98/.proxy/main/all | active | 3/3 | 5477 | 5477.0 | 15085 |
| https://raw.githubusercontent.com/DukeMehdi/FreeList-V2ray-Configs/refs/heads/main/Configs/TROJAN-DukeMehdi-Configs.txt | active | 3/3 | 3696 | 3696.0 | 3057 |
| https://raw.githubusercontent.com/sakha1370/OpenRay/main/output/all_valid_proxies.txt | active | 3/3 | 3060 | 3060.0 | 8656 |
| https://raw.githubusercontent.com/sevcator/5ubscrpt10n/main/mini/m1n1-5ub-14.txt | active | 3/3 | 2260 | 2260.0 | 7420 |
| https://raw.githubusercontent.com/xiaoji235/airport-free/main/v2ray.txt | active | 3/3 | 2143 | 2143.0 | 3755 |
| https://raw.githubusercontent.com/xiaoji235/airport-free/refs/heads/main/v2ray/clashnodecc.txt | active | 3/3 | 2141 | 2141.0 | 3743 |
| https://raw.githubusercontent.com/sevcator/5ubscrpt10n/main/mini/m1n1-5ub-19.txt | active | 3/3 | 1939 | 1939.0 | 7584 |
| https://mihomoparty.github.io/uploads/{Y}/{mm}/2-{Ymd}.txt | active | 3/3 | 1780 | 1780.0 | 3311 |
| https://clashbest.github.io/uploads/{Y}/{mm}/2-{Ymd}.txt | active | 3/3 | 1780 | 1780.0 | 3311 |
| https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/main/all_configs.txt | active | 3/3 | 1587 | 1586.3 | 5555 |
| https://raw.githubusercontent.com/liMilCo/v2r/main/configs.txt | active | 3/3 | 1544 | 1544.0 | 4854 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/soroushmirzaei.yaml | active | 3/3 | 1443 | 1443.0 | 40798 |
| https://raw.githubusercontent.com/Leon406/SubCrawler/master/sub/share/vless | active | 3/3 | 1043 | 1043.0 | 3501 |
| https://clashgithub.com/wp-content/uploads/rss/{Ymd}.txt | active | 3/3 | 623 | 623.0 | 970 |
| https://mihomoparty.github.io/uploads/{Y}/{mm}/4-{Ymd}.txt | active | 3/3 | 608 | 608.0 | 962 |
| https://raw.githubusercontent.com/anaer/Sub/main/clash.yaml | active | 3/3 | 523 | 523.0 | 1586 |
| https://raw.githubusercontent.com/asgharkapk/Sub-Config-Extractor/main/output_configs/mixed/Leon406/SubCrawler/sub/share/a11.yaml | active | 3/3 | 497 | 497.0 | 203 |
| https://github.com/Au1rxx/free-vpn-subscriptions/raw/main/output/by-country/v2ray-base64-JP.txt | active | 3/3 | 378 | 378.0 | 440 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/anaer.yaml | active | 3/3 | 342 | 342.0 | 1815 |
| https://raw.githubusercontent.com/mahdibland/SSAggregator/master/sub/sub_merge_yaml.yml | active | 3/3 | 342 | 342.0 | 4204 |
| https://raw.githubusercontent.com/mahdibland/V2RayAggregator/master/sub/sub_merge_yaml.yml | active | 3/3 | 342 | 342.0 | 4204 |
| https://node.freeclashnode.com/uploads/{Y}/{mm}/2-{Ymd}.yaml | active | 3/3 | 274 | 274.0 | 4805 |
| https://clashbest.github.io/uploads/{Y}/{mm}/2-{Ymd}.yaml | active | 3/3 | 274 | 274.0 | 4805 |
| https://raw.githubusercontent.com/NiceVPN123/NiceVPN/main/utils/pool/output.yaml | active | 3/3 | 226 | 226.0 | 3501 |
| https://raw.githubusercontent.com/NiceVPN123/NiceVPN/main/Clash.yaml | active | 3/3 | 225 | 225.0 | 3418 |
| https://github.com/Au1rxx/free-vpn-subscriptions/raw/main/output/by-country/v2ray-base64-SG.txt | active | 3/3 | 223 | 223.0 | 140 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/coldwater-10.yaml | active | 3/3 | 199 | 199.0 | 1561 |
| https://raw.githubusercontent.com/Q3dlaXpoaQ/V2rayN_Clash_Node_Getter/main/APIs/sc2.yaml | active | 3/3 | 181 | 181.0 | 3475 |
| https://raw.githubusercontent.com/Q3dlaXpoaQ/V2rayN_Clash_Node_Getter/refs/heads/main/APIs/sc2.yaml | active | 3/3 | 181 | 181.0 | 3475 |
| https://raw.githubusercontent.com/F0rc3Run/F0rc3Run/refs/heads/main/splitted-by-protocol/trojan.txt | active | 3/3 | 162 | 162.0 | 36 |
| https://raw.githubusercontent.com/liMilCo/v2r/main/base64/2.txt | active | 3/3 | 155 | 155.0 | 302 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/trial.yaml | active | 3/3 | 149 | 149.0 | 607 |
| https://github.com/Au1rxx/free-vpn-subscriptions/raw/main/output/by-country/v2ray-base64-US.txt | active | 3/3 | 144 | 144.0 | 80 |
| https://raw.githubusercontent.com/barry-far/V2ray-config/main/Sub2.txt | active | 3/3 | 137 | 137.0 | 333 |
| https://raw.githubusercontent.com/ALIILAPRO/v2rayNG-Config/main/sub.txt | active | 3/3 | 129 | 129.0 | 678 |
| https://github.com/Au1rxx/free-vpn-subscriptions/raw/main/output/by-country/v2ray-base64-HK.txt | active | 3/3 | 128 | 128.0 | 55 |
| https://raw.githubusercontent.com/MhdiTaheri/V2rayCollector/main/sub/mix | active | 3/3 | 127 | 127.0 | 851 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/_previous.yaml | active | 3/3 | 105 | 105.0 | 410 |
| https://github.com/crackbest/V2ray-Config/raw/refs/heads/main/config.txt | active | 3/3 | 74 | 74.0 | 421 |
| https://raw.githubusercontent.com/crackbest/V2ray-Config/refs/heads/main/config.txt | active | 3/3 | 74 | 74.0 | 421 |
| https://raw.githubusercontent.com/xtoolkit/TVC/main/subscriptions/meta/mix | active | 3/3 | 67 | 67.0 | 279 |
| https://raw.githubusercontent.com/ts-sf/fly/main/clash | active | 3/3 | 67 | 67.0 | 133 |
| https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/main/Base64/BLACK_VLESS_RUS_base64.txt | active | 3/3 | 61 | 61.0 | 93 |
| https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/main/BLACK_VLESS_RUS.txt | active | 3/3 | 61 | 61.0 | 93 |
| https://clashbest.github.io/uploads/{Y}/{mm}/1-{Ymd}.txt | active | 3/3 | 58 | 58.0 | 211 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/clashfree.yaml | active | 3/3 | 56 | 56.0 | 498 |
| https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/main/Base64/BLACK_VLESS_RUS_mobile_base64.txt | active | 3/3 | 52 | 52.0 | 91 |
| https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/main/BLACK_VLESS_RUS_mobile.txt | active | 3/3 | 52 | 52.0 | 91 |
| https://clashbest.github.io/uploads/{Y}/{mm}/0-{Ymd}.txt | active | 3/3 | 49 | 49.0 | 186 |
| https://raw.githubusercontent.com/hans-thomas/v2ray-subscription/refs/heads/master/servers.txt | active | 3/3 | 46 | 46.0 | 86 |
| https://raw.githubusercontent.com/Arefgh72/v2ray-proxy-pars-tester/main/output/github_all.txt | active | 3/3 | 46 | 46.0 | 2776 |
| https://raw.githubusercontent.com/ts-sf/fly/main/v2 | active | 3/3 | 45 | 45.0 | 156 |
| https://raw.githubusercontent.com/F0rc3Run/F0rc3Run/refs/heads/main/splitted-by-protocol/vless.txt | active | 3/3 | 45 | 45.0 | 201 |
| https://raw.githubusercontent.com/acymz/AutoVPN/main/data/V2.txt | active | 3/3 | 31 | 31.0 | 214 |
| https://raw.githubusercontent.com/Barabama/FreeNodes/main/nodes/blues.txt | active | 3/3 | 26 | 26.0 | 109 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/snakem982.yaml | active | 3/3 | 24 | 24.0 | 41 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/zhangkaiitugithub.yaml | active | 3/3 | 24 | 24.0 | 41 |
| https://raw.githubusercontent.com/LoneKingCode/free-proxy-db/main/proxies/all.txt | active | 3/3 | 24 | 24.0 | 355 |
| https://raw.githubusercontent.com/Ruk1ng001/freeSub/main/clash.yaml | active | 3/3 | 22 | 22.0 | 83 |
| https://github.com/Au1rxx/free-vpn-subscriptions/raw/main/output/by-country/v2ray-base64-KR.txt | active | 3/3 | 20 | 20.0 | 19 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/yudou.yaml | active | 3/3 | 17 | 17.0 | 49 |
| https://raw.githubusercontent.com/PangTouY00/Auto_proxy/main/Long_term_subscription_num | active | 3/3 | 16 | 16.0 | 181 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/tssf.yaml | active | 3/3 | 16 | 16.0 | 65 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/aiboboxx.yaml | active | 3/3 | 15 | 15.0 | 701 |
| https://www.xrayvip.com/free.txt | active | 3/3 | 15 | 15.0 | 49 |
| https://raw.githubusercontent.com/Surfboardv2ray/v2ray-worker-sub/refs/heads/master/Eternity.txt | active | 3/3 | 15 | 15.0 | 185 |
| https://raw.githubusercontent.com/ovmvo/SubShare/main/sub/permanent/mihomo.yaml | active | 3/3 | 14 | 14.0 | 37 |
| https://raw.githubusercontent.com/snakem982/proxypool/main/source/clash-meta-2.yaml | active | 3/3 | 12 | 12.0 | 114 |
| https://raw.githubusercontent.com/MatinGhanbari/v2ray-configs/main/subscriptions/v2ray/subs/sub2.txt | active | 3/3 | 12 | 12.0 | 126 |
| https://raw.githubusercontent.com/peasoft/NoMoreWalls/master/list.meta.yml | active | 3/3 | 9 | 9.0 | 147 |
| https://raw.githubusercontent.com/peasoft/NoMoreWalls/master/snippets/nodes.meta.yml | active | 3/3 | 9 | 9.0 | 147 |
| https://raw.githubusercontent.com/ggborr/FREEE-VPN/main/3v2 | active | 3/3 | 9 | 9.0 | 7 |
| https://raw.githubusercontent.com/mgit0001/test_clash/main/heima.txt | active | 3/3 | 8 | 8.0 | 17 |
| https://raw.githubusercontent.com/mgit0001/test_clash/refs/heads/main/heima.txt | active | 3/3 | 8 | 8.0 | 17 |
| https://raw.githubusercontent.com/Pawdroid/Free-servers/main/sub | active | 3/3 | 8 | 7.3 | 12 |
| https://raw.githubusercontent.com/Pawdroid/Free-servers/refs/heads/main/sub | active | 3/3 | 8 | 7.3 | 12 |
| https://raw.githubusercontent.com/Barabama/FreeNodes/main/nodes/ndnode.txt | active | 3/3 | 7 | 7.0 | 7 |
| https://raw.githubusercontent.com/vxiaov/free_proxies/main/clash/clash.provider.yaml | active | 3/3 | 7 | 7.0 | 19 |
| https://raw.githubusercontent.com/zhangkaiitugithub/passcro/main/speednodes.yaml | active | 3/3 | 7 | 7.0 | 5 |
| https://raw.githubusercontent.com/free18/v2ray/main/c.yaml | active | 3/3 | 7 | 7.0 | 186 |
| https://raw.githubusercontent.com/justVisiting992/xray-Config-Collector/main/clash.yaml | active | 3/3 | 6 | 6.0 | 1059 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/_pool.yaml | active | 3/3 | 6 | 6.0 | 222 |
| https://raw.githubusercontent.com/actionsfz/v2ray/master/all.yaml | active | 3/3 | 6 | 6.0 | 79 |
| https://raw.githubusercontent.com/actionsfz/v2ray/refs/heads/master/all.yaml | active | 3/3 | 6 | 6.0 | 79 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/xrayvip.yaml | active | 3/3 | 6 | 6.0 | 18 |
| https://raw.githubusercontent.com/peacefish/nodefree/main/sub/proxy_cf.yaml | active | 3/3 | 6 | 6.0 | 43 |
| https://raw.githubusercontent.com/HakurouKen/free-node/main/public | active | 3/3 | 5 | 5.0 | 22 |
| https://raw.githubusercontent.com/Shjpr9/Subs/refs/heads/main/sub.txt | active | 3/3 | 5 | 5.0 | 139 |
| https://raw.githubusercontent.com/mahdibland/ShadowsocksAggregator/master/Eternity.yml | active | 3/3 | 4 | 4.0 | 197 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/ttvg.yaml | active | 3/3 | 4 | 4.0 | 14 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/hkaa0.yaml | active | 3/3 | 4 | 4.0 | 6154 |
| https://raw.githubusercontent.com/Barabama/FreeNodes/main/nodes/nodefree.txt | active | 3/3 | 3 | 3.0 | 20 |
| https://raw.githubusercontent.com/mfbpn/tg_mfbpn_sub/main/trial.yaml | active | 3/3 | 3 | 3.0 | 115 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/mahdibland.yaml | active | 3/3 | 3 | 3.0 | 196 |
| https://raw.githubusercontent.com/Barabama/FreeNodes/main/nodes/v2rayshare.txt | active | 3/3 | 3 | 3.0 | 20 |
| https://raw.githubusercontent.com/Barabama/FreeNodes/main/nodes/wenode.txt | active | 3/3 | 3 | 3.0 | 20 |
| https://raw.githubusercontent.com/Barabama/FreeNodes/main/nodes/yudou66.txt | active | 3/3 | 3 | 3.0 | 161 |
| https://raw.githubusercontent.com/Barabama/FreeNodes/main/nodes/yudou66.yaml | active | 3/3 | 3 | 3.0 | 160 |
| https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/main/Base64/BLACK_SS+All_RUS_base64.txt | active | 3/3 | 3 | 3.0 | 73 |
| https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/main/BLACK_SS+All_RUS.txt | active | 3/3 | 3 | 3.0 | 73 |
| https://raw.githubusercontent.com/shaoyouvip/free/refs/heads/main/all.yaml | active | 3/3 | 2 | 2.0 | 10 |
| https://raw.githubusercontent.com/F0rc3Run/F0rc3Run/refs/heads/main/splitted-by-protocol/vmess.txt | active | 3/3 | 2 | 2.0 | 31 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/SFZY666.yaml | active | 3/3 | 2 | 2.0 | 10 |
| https://raw.githubusercontent.com/xiaoji235/airport-free/refs/heads/main/v2ray/v2rayshare.txt | active | 3/3 | 2 | 2.0 | 12 |
| https://raw.githubusercontent.com/hello-world-1989/cn-news/main/end-gfw-together | active | 3/3 | 2 | 2.0 | 0 |
| https://github.com/Au1rxx/free-vpn-subscriptions/raw/main/output/by-country/v2ray-base64-TW.txt | active | 3/3 | 2 | 2.0 | 21 |
| https://raw.githubusercontent.com/Barabama/FreeNodes/main/nodes/clashmeta.txt | active | 3/3 | 1 | 1.0 | 11 |
| https://raw.githubusercontent.com/vxiaov/free_proxies/main/links.txt | active | 3/3 | 1 | 1.0 | 6 |
| https://raw.githubusercontent.com/free-nodes/clashfree/main/clash{Ymd}.yml | active | 3/3 | 0 | 0.0 | 0 |
| https://proxypool.link/trojan/sub | active | 3/3 | 0 | 0.0 | 0 |
| https://raw.githubusercontent.com/DukeMehdi/FreeList-V2ray-Configs/refs/heads/main/Configs/VMESS-DukeMehdi-Configs.txt | active | 3/3 | 0 | 0.0 | 0 |
| https://github.com/AzadNetCH/Clash/raw/refs/heads/main/AzadNet.txt | active | 3/3 | 0 | 0.0 | 17 |
| https://raw.githubusercontent.com/aiboboxx/v2rayfree/main/README.md | active | 3/3 | 0 | 0.0 | 20 |
| https://raw.githubusercontent.com/aiboboxx/v2rayfree/refs/heads/main/README.md | active | 3/3 | 0 | 0.0 | 20 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/refs/heads/main/V2RAY.txt | active | 3/3 | 0 | 0.0 | 0 |
| https://node.freeclashnode.com/uploads/{Y}/{mm}/0-{Ymd}.yaml | active | 3/3 | 0 | 0.0 | 235 |
| https://raw.githubusercontent.com/Q3dlaXpoaQ/V2rayN_Clash_Node_Getter/main/APIs/sc0.yaml | active | 3/3 | 0 | 0.0 | 241 |
| https://raw.githubusercontent.com/Q3dlaXpoaQ/V2rayN_Clash_Node_Getter/refs/heads/main/APIs/sc0.yaml | active | 3/3 | 0 | 0.0 | 241 |
| https://node.freeclashnode.com/uploads/{Y}/{mm}/1-{Ymd}.yaml | active | 3/3 | 0 | 0.0 | 266 |
| https://raw.githubusercontent.com/peasoft/NoMoreWalls/master/list.yml | active | 3/3 | 0 | 0.0 | 26 |
| https://raw.githubusercontent.com/Misaka-blog/chromego_merge/main/sub/merged_proxies_new.yaml | active | 3/3 | 0 | 0.0 | 56 |
| https://raw.githubusercontent.com/Q3dlaXpoaQ/V2rayN_Clash_Node_Getter/main/APIs/sc1.yaml | active | 3/3 | 0 | 0.0 | 265 |
| https://raw.githubusercontent.com/Q3dlaXpoaQ/V2rayN_Clash_Node_Getter/refs/heads/main/APIs/sc1.yaml | active | 3/3 | 0 | 0.0 | 265 |
| https://raw.githubusercontent.com/chengaopan/AutoMergePublicNodes/master/list.yml | active | 3/3 | 0 | 0.0 | 15 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/chengaopan.yaml | active | 3/3 | 0 | 0.0 | 16 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/peasoft.yaml | active | 3/3 | 0 | 0.0 | 26 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/ripaojiedian.yaml | active | 3/3 | 0 | 0.0 | 14 |
| https://raw.githubusercontent.com/ripaojiedian/freenode/main/clash | active | 3/3 | 0 | 0.0 | 14 |
| https://raw.githubusercontent.com/Barabama/FreeNodes/main/nodes/clashmeta.yaml | active | 3/3 | 0 | 0.0 | 89 |
| https://node.freeclashnode.com/uploads/{Y}/{mm}/3-{Ymd}.yaml | active | 3/3 | 0 | 0.0 | 14 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/blue-Youtube.yaml | active | 3/3 | 0 | 0.0 | 47 |
| https://raw.githubusercontent.com/Q3dlaXpoaQ/V2rayN_Clash_Node_Getter/main/APIs/sc3.yaml | active | 3/3 | 0 | 0.0 | 14 |
| https://raw.githubusercontent.com/Q3dlaXpoaQ/V2rayN_Clash_Node_Getter/refs/heads/main/APIs/sc3.yaml | active | 3/3 | 0 | 0.0 | 14 |
| https://raw.githubusercontent.com/ermaozi/get_subscribe/main/subscribe/clash.yml | active | 3/3 | 0 | 0.0 | 20 |
| https://raw.githubusercontent.com/firefoxmmx2/v2rayshare_subcription/main/subscription/clash_sub.yaml | active | 3/3 | 0 | 0.0 | 14 |
| https://raw.githubusercontent.com/go4sharing/sub/main/sub.yaml | active | 3/3 | 0 | 0.0 | 24 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/ermaozi.yaml | active | 3/3 | 0 | 0.0 | 21 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/Pawdroid.yaml | active | 3/3 | 0 | 0.0 | 8 |
| https://node.freeclashnode.com/uploads/{Y}/{mm}/4-{Ymd}.yaml | active | 3/3 | 0 | 0.0 | 0 |
| https://github.com/mermeroo/V2RAY-CLASH-BASE64-Subscription.Links/raw/refs/heads/main/SUB%20LINKS | active | 3/3 | 0 | 0.0 | 0 |
| https://raw.githubusercontent.com/andigwandi/free-proxy/main/proxy_list.txt | active | 3/3 | 0 | 0.0 | 0 |
| https://raw.githubusercontent.com/asgharkapk/Sub-Config-Extractor/main/output_configs/clash/Ruk1ng001.yaml | active | 3/3 | 0 | 0.0 | 0 |
| https://raw.githubusercontent.com/asgharkapk/Sub-Config-Extractor/main/output_configs/surfboard/Barabama_ndnode.yaml | active | 3/3 | 0 | 0.0 | 0 |
| https://raw.githubusercontent.com/asgharkapk/Sub-Config-Extractor/main/output_configs/surfboard/Ruk1ng001.yaml | active | 3/3 | 0 | 0.0 | 0 |
| https://raw.githubusercontent.com/Barabama/FreeNodes/main/nodes/nodev2ray.txt | active | 3/3 | 0 | 0.0 | 13 |
| https://raw.githubusercontent.com/dpangestuw/Free-Proxy/main/All_proxies.txt | active | 3/3 | 0 | 0.0 | 0 |
| https://raw.githubusercontent.com/linzjian666/chromego_extractor/main/outputs/clash_meta.yaml | active | 3/3 | 0 | 0.0 | 0 |
| https://raw.githubusercontent.com/officialputuid/ProxyForEveryone/main/xResults/old-data/RAW.txt | active | 3/3 | 0 | 0.0 | 0 |
| https://raw.githubusercontent.com/officialputuid/ProxyForEveryone/main/xResults/RAW.txt | active | 3/3 | 0 | 0.0 | 0 |
| https://raw.githubusercontent.com/shahidbhutta/Clash/main/Router | active | 3/3 | 0 | 0.0 | 0 |
| https://raw.githubusercontent.com/shahidbhutta/Clash/refs/heads/main/Router | active | 3/3 | 0 | 0.0 | 0 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/changfengoss.yaml | active | 3/3 | 0 | 0.0 | 3 |
| https://raw.githubusercontent.com/SnapdragonLee/SystemProxy/master/dist/clash_config.yaml | active | 3/3 | 0 | 0.0 | 0 |
| https://raw.githubusercontent.com/xiaoji235/airport-free/refs/heads/main/v2ray/naidounode.txt | active | 3/3 | 0 | 0.0 | 0 |
| https://free.datiya.com/uploads/{Ymd}-clash.yaml | active | 3/3 | 0 | 0.0 | 14 |
| https://free.datiya.com/uploads/{Ymd}-v2ray.txt | active | 3/3 | 0 | 0.0 | 0 |
| https://raw.githubusercontent.com/Delta-Kronecker/V2ray-Config/main/config/clash.yaml | active | 3/3 | 0 | 0.0 | 6996 |
| https://www.ermao.net/sub/clash/ermao.net | active | 3/3 | 0 | 0.0 | 20 |
| https://clashbest.github.io/uploads/{Y}/{mm}/0-{Ymd}.yaml | active | 3/3 | 0 | 0.0 | 235 |
| https://clashbest.github.io/uploads/{Y}/{mm}/1-{Ymd}.yaml | active | 3/3 | 0 | 0.0 | 266 |
| https://clashbest.github.io/uploads/{Y}/{mm}/3-{Ymd}.yaml | active | 3/3 | 0 | 0.0 | 14 |
| https://clashbest.github.io/uploads/{Y}/{mm}/4-{Ymd}.yaml | active | 3/3 | 0 | 0.0 | 0 |
| https://clashbest.github.io/uploads/{Y}/{mm}/{Ymd}.json | active | 3/3 | 0 | 0.0 | 0 |
| https://mihomoparty.github.io/uploads/{Y}/{mm}/0-{Ymd}.yaml | active | 3/3 | 0 | 0.0 | 235 |
| https://mihomoparty.github.io/uploads/{Y}/{mm}/1-{Ymd}.yaml | active | 3/3 | 0 | 0.0 | 266 |
| https://mihomoparty.github.io/uploads/{Y}/{mm}/4-{Ymd}.yaml | active | 3/3 | 0 | 0.0 | 0 |
| https://mihomoparty.github.io/uploads/{Y}/{mm}/{Ymd}.json | active | 3/3 | 0 | 0.0 | 0 |
| https://link.rittbo.kdns.fr/sub?token=8794e5157120a9982b0ceed9dcef5de7 | active | 0/3 | 0 | 0.0 | 0 |
| https://raw.githubusercontent.com/free-nodes/v2rayfree/main/v{ymd}1 | active | 0/3 | 0 | 0.0 | 0 |
| https://raw.githubusercontent.com/free-nodes/v2rayfree/main/v{ymd}2 | active | 0/3 | 0 | 0.0 | 0 |
| https://raw.githubusercontent.com/lagzian/SS-Collector/main/SS/trinity_clash.yaml | active | 0/3 | 0 | 0.0 | 0 |
| https://raw.githubusercontent.com/lagzian/SS-Collector/main/SS/TrinityBase | active | 0/3 | 0 | 0.0 | 0 |
| https://raw.githubusercontent.com/lagzian/SS-Collector/main/SS/VM_TrinityBase | active | 0/3 | 0 | 0.0 | 0 |
| https://raw.githubusercontent.com/MrMohebi/xray-proxy-grabber-telegram/master/collected-proxies/clash-meta/all.yaml | active | 0/3 | 0 | 0.0 | 0 |
| https://raw.githubusercontent.com/yorkLiu/FreeV2RayNode/main/v2ray.txt | active | 0/3 | 0 | 0.0 | 0 |

## 聚合源（按近 N 次平均拉取数降序）
| id | 链接 | 成功率 | 最近 | 平均 |
|---|---|:---:|---|---|
| sinspired_scan | https://raw.githubusercontent.com/sinspired/airport/main/subs/merged/scan.txt | 3/3 | 20 | 20.0 |
| sinspired_scan | https://raw.githubusercontent.com/sinspired/airport/main/subs/merged/scan.txt | 3/3 | 20 | 20.0 |
| sinspired_col | https://raw.githubusercontent.com/sinspired/airport/main/subs/merged/col.txt | 3/3 | 17 | 17.0 |
| sinspired_col | https://raw.githubusercontent.com/sinspired/airport/main/subs/merged/col.txt | 3/3 | 17 | 17.0 |
| sinspired_cm | https://raw.githubusercontent.com/sinspired/airport/main/subs/merged/cm.txt | 3/3 | 12 | 12.0 |
| sinspired_cm | https://raw.githubusercontent.com/sinspired/airport/main/subs/merged/cm.txt | 3/3 | 12 | 12.0 |
