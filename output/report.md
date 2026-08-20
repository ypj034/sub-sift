# sub-sift 运行报告

- 运行时间: 2026-08-20 16:18:40 CST
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
| protocol_allowlist | 31016 |
| validity | 5484 |
| server_denylist | 4363 |
| suspicious_pattern | 96 |
| security_vmess | 24583 |
| security_vless | 70294 |
| security_trojan | 31271 |
| region_allowlist | 74689 |
| **合计** | **241796** |

## 主清单（active → 冷却 → disabled；组内按 avg 降序）
| link | 状态 | success_rate | last | avg |
|---|---|---|---|---|
| https://raw.githubusercontent.com/ebrasha/free-v2ray-public-list/refs/heads/main/all_extracted_configs.txt | active | 2/2 | 10054 | 10019.5 |
| https://raw.githubusercontent.com/DukeMehdi/FreeList-V2ray-Configs/refs/heads/main/Configs/VLESS-DukeMehdi-Configs.txt | active | 2/2 | 6486 | 6486.0 |
| https://raw.githubusercontent.com/mheidari98/.proxy/main/all | active | 2/2 | 5477 | 5477.0 |
| https://raw.githubusercontent.com/DukeMehdi/FreeList-V2ray-Configs/refs/heads/main/Configs/TROJAN-DukeMehdi-Configs.txt | active | 2/2 | 3696 | 3696.0 |
| https://raw.githubusercontent.com/sakha1370/OpenRay/main/output/all_valid_proxies.txt | active | 2/2 | 3060 | 3060.0 |
| https://raw.githubusercontent.com/sevcator/5ubscrpt10n/main/mini/m1n1-5ub-14.txt | active | 2/2 | 2260 | 2260.0 |
| https://raw.githubusercontent.com/xiaoji235/airport-free/main/v2ray.txt | active | 2/2 | 2143 | 2143.0 |
| https://raw.githubusercontent.com/xiaoji235/airport-free/refs/heads/main/v2ray/clashnodecc.txt | active | 2/2 | 2141 | 2141.0 |
| https://raw.githubusercontent.com/sevcator/5ubscrpt10n/main/mini/m1n1-5ub-19.txt | active | 2/2 | 1939 | 1939.0 |
| https://mihomoparty.github.io/uploads/{Y}/{mm}/2-{Ymd}.txt | active | 2/2 | 1780 | 1780.0 |
| https://clashbest.github.io/uploads/{Y}/{mm}/2-{Ymd}.txt | active | 2/2 | 1780 | 1780.0 |
| https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/main/all_configs.txt | active | 2/2 | 1587 | 1586.0 |
| https://raw.githubusercontent.com/liMilCo/v2r/main/configs.txt | active | 2/2 | 1544 | 1544.0 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/soroushmirzaei.yaml | active | 2/2 | 1443 | 1443.0 |
| https://raw.githubusercontent.com/Leon406/SubCrawler/master/sub/share/vless | active | 2/2 | 1043 | 1043.0 |
| https://clashgithub.com/wp-content/uploads/rss/{Ymd}.txt | active | 2/2 | 623 | 623.0 |
| https://mihomoparty.github.io/uploads/{Y}/{mm}/4-{Ymd}.txt | active | 2/2 | 608 | 608.0 |
| https://raw.githubusercontent.com/anaer/Sub/main/clash.yaml | active | 2/2 | 523 | 523.0 |
| https://raw.githubusercontent.com/asgharkapk/Sub-Config-Extractor/main/output_configs/mixed/Leon406/SubCrawler/sub/share/a11.yaml | active | 2/2 | 497 | 497.0 |
| https://github.com/Au1rxx/free-vpn-subscriptions/raw/main/output/by-country/v2ray-base64-JP.txt | active | 2/2 | 378 | 378.0 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/anaer.yaml | active | 2/2 | 342 | 342.0 |
| https://raw.githubusercontent.com/mahdibland/SSAggregator/master/sub/sub_merge_yaml.yml | active | 2/2 | 342 | 342.0 |
| https://raw.githubusercontent.com/mahdibland/V2RayAggregator/master/sub/sub_merge_yaml.yml | active | 2/2 | 342 | 342.0 |
| https://node.freeclashnode.com/uploads/{Y}/{mm}/2-{Ymd}.yaml | active | 2/2 | 274 | 274.0 |
| https://clashbest.github.io/uploads/{Y}/{mm}/2-{Ymd}.yaml | active | 2/2 | 274 | 274.0 |
| https://raw.githubusercontent.com/NiceVPN123/NiceVPN/main/utils/pool/output.yaml | active | 2/2 | 226 | 226.0 |
| https://raw.githubusercontent.com/NiceVPN123/NiceVPN/main/Clash.yaml | active | 2/2 | 225 | 225.0 |
| https://github.com/Au1rxx/free-vpn-subscriptions/raw/main/output/by-country/v2ray-base64-SG.txt | active | 2/2 | 223 | 223.0 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/coldwater-10.yaml | active | 2/2 | 199 | 199.0 |
| https://raw.githubusercontent.com/Q3dlaXpoaQ/V2rayN_Clash_Node_Getter/main/APIs/sc2.yaml | active | 2/2 | 181 | 181.0 |
| https://raw.githubusercontent.com/Q3dlaXpoaQ/V2rayN_Clash_Node_Getter/refs/heads/main/APIs/sc2.yaml | active | 2/2 | 181 | 181.0 |
| https://raw.githubusercontent.com/F0rc3Run/F0rc3Run/refs/heads/main/splitted-by-protocol/trojan.txt | active | 2/2 | 162 | 162.0 |
| https://raw.githubusercontent.com/liMilCo/v2r/main/base64/2.txt | active | 2/2 | 155 | 155.0 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/trial.yaml | active | 2/2 | 149 | 149.0 |
| https://github.com/Au1rxx/free-vpn-subscriptions/raw/main/output/by-country/v2ray-base64-US.txt | active | 2/2 | 144 | 144.0 |
| https://raw.githubusercontent.com/barry-far/V2ray-config/main/Sub2.txt | active | 2/2 | 137 | 137.0 |
| https://raw.githubusercontent.com/ALIILAPRO/v2rayNG-Config/main/sub.txt | active | 2/2 | 129 | 129.0 |
| https://github.com/Au1rxx/free-vpn-subscriptions/raw/main/output/by-country/v2ray-base64-HK.txt | active | 2/2 | 128 | 128.0 |
| https://raw.githubusercontent.com/MhdiTaheri/V2rayCollector/main/sub/mix | active | 2/2 | 127 | 127.0 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/_previous.yaml | active | 2/2 | 105 | 105.0 |
| https://github.com/crackbest/V2ray-Config/raw/refs/heads/main/config.txt | active | 2/2 | 74 | 74.0 |
| https://raw.githubusercontent.com/crackbest/V2ray-Config/refs/heads/main/config.txt | active | 2/2 | 74 | 74.0 |
| https://raw.githubusercontent.com/xtoolkit/TVC/main/subscriptions/meta/mix | active | 2/2 | 67 | 67.0 |
| https://raw.githubusercontent.com/ts-sf/fly/main/clash | active | 2/2 | 67 | 67.0 |
| https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/main/Base64/BLACK_VLESS_RUS_base64.txt | active | 2/2 | 61 | 61.0 |
| https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/main/BLACK_VLESS_RUS.txt | active | 2/2 | 61 | 61.0 |
| https://clashbest.github.io/uploads/{Y}/{mm}/1-{Ymd}.txt | active | 2/2 | 58 | 58.0 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/clashfree.yaml | active | 2/2 | 56 | 56.0 |
| https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/main/Base64/BLACK_VLESS_RUS_mobile_base64.txt | active | 2/2 | 52 | 52.0 |
| https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/main/BLACK_VLESS_RUS_mobile.txt | active | 2/2 | 52 | 52.0 |
| https://clashbest.github.io/uploads/{Y}/{mm}/0-{Ymd}.txt | active | 2/2 | 49 | 49.0 |
| https://raw.githubusercontent.com/hans-thomas/v2ray-subscription/refs/heads/master/servers.txt | active | 2/2 | 46 | 46.0 |
| https://raw.githubusercontent.com/Arefgh72/v2ray-proxy-pars-tester/main/output/github_all.txt | active | 2/2 | 46 | 46.0 |
| https://raw.githubusercontent.com/ts-sf/fly/main/v2 | active | 2/2 | 45 | 45.0 |
| https://raw.githubusercontent.com/F0rc3Run/F0rc3Run/refs/heads/main/splitted-by-protocol/vless.txt | active | 2/2 | 45 | 45.0 |
| https://raw.githubusercontent.com/acymz/AutoVPN/main/data/V2.txt | active | 2/2 | 31 | 31.0 |
| https://raw.githubusercontent.com/Barabama/FreeNodes/main/nodes/blues.txt | active | 2/2 | 26 | 26.0 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/snakem982.yaml | active | 2/2 | 24 | 24.0 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/zhangkaiitugithub.yaml | active | 2/2 | 24 | 24.0 |
| https://raw.githubusercontent.com/LoneKingCode/free-proxy-db/main/proxies/all.txt | active | 2/2 | 24 | 24.0 |
| https://raw.githubusercontent.com/Ruk1ng001/freeSub/main/clash.yaml | active | 2/2 | 22 | 22.0 |
| https://github.com/Au1rxx/free-vpn-subscriptions/raw/main/output/by-country/v2ray-base64-KR.txt | active | 2/2 | 20 | 20.0 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/yudou.yaml | active | 2/2 | 17 | 17.0 |
| https://raw.githubusercontent.com/PangTouY00/Auto_proxy/main/Long_term_subscription_num | active | 2/2 | 16 | 16.0 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/tssf.yaml | active | 2/2 | 16 | 16.0 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/aiboboxx.yaml | active | 2/2 | 15 | 15.0 |
| https://www.xrayvip.com/free.txt | active | 2/2 | 15 | 15.0 |
| https://raw.githubusercontent.com/Surfboardv2ray/v2ray-worker-sub/refs/heads/master/Eternity.txt | active | 2/2 | 15 | 15.0 |
| https://raw.githubusercontent.com/ovmvo/SubShare/main/sub/permanent/mihomo.yaml | active | 2/2 | 14 | 14.0 |
| https://raw.githubusercontent.com/snakem982/proxypool/main/source/clash-meta-2.yaml | active | 2/2 | 12 | 12.0 |
| https://raw.githubusercontent.com/MatinGhanbari/v2ray-configs/main/subscriptions/v2ray/subs/sub2.txt | active | 2/2 | 12 | 12.0 |
| https://raw.githubusercontent.com/peasoft/NoMoreWalls/master/list.meta.yml | active | 2/2 | 9 | 9.0 |
| https://raw.githubusercontent.com/peasoft/NoMoreWalls/master/snippets/nodes.meta.yml | active | 2/2 | 9 | 9.0 |
| https://raw.githubusercontent.com/ggborr/FREEE-VPN/main/3v2 | active | 2/2 | 9 | 9.0 |
| https://raw.githubusercontent.com/mgit0001/test_clash/main/heima.txt | active | 2/2 | 8 | 8.0 |
| https://raw.githubusercontent.com/mgit0001/test_clash/refs/heads/main/heima.txt | active | 2/2 | 8 | 8.0 |
| https://raw.githubusercontent.com/Barabama/FreeNodes/main/nodes/ndnode.txt | active | 2/2 | 7 | 7.0 |
| https://raw.githubusercontent.com/vxiaov/free_proxies/main/clash/clash.provider.yaml | active | 2/2 | 7 | 7.0 |
| https://raw.githubusercontent.com/zhangkaiitugithub/passcro/main/speednodes.yaml | active | 2/2 | 7 | 7.0 |
| https://raw.githubusercontent.com/free18/v2ray/main/c.yaml | active | 2/2 | 7 | 7.0 |
| https://raw.githubusercontent.com/Pawdroid/Free-servers/main/sub | active | 2/2 | 8 | 7.0 |
| https://raw.githubusercontent.com/Pawdroid/Free-servers/refs/heads/main/sub | active | 2/2 | 8 | 7.0 |
| https://raw.githubusercontent.com/justVisiting992/xray-Config-Collector/main/clash.yaml | active | 2/2 | 6 | 6.0 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/_pool.yaml | active | 2/2 | 6 | 6.0 |
| https://raw.githubusercontent.com/actionsfz/v2ray/master/all.yaml | active | 2/2 | 6 | 6.0 |
| https://raw.githubusercontent.com/actionsfz/v2ray/refs/heads/master/all.yaml | active | 2/2 | 6 | 6.0 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/xrayvip.yaml | active | 2/2 | 6 | 6.0 |
| https://raw.githubusercontent.com/peacefish/nodefree/main/sub/proxy_cf.yaml | active | 2/2 | 6 | 6.0 |
| https://raw.githubusercontent.com/HakurouKen/free-node/main/public | active | 2/2 | 5 | 5.0 |
| https://raw.githubusercontent.com/Shjpr9/Subs/refs/heads/main/sub.txt | active | 2/2 | 5 | 5.0 |
| https://raw.githubusercontent.com/mahdibland/ShadowsocksAggregator/master/Eternity.yml | active | 2/2 | 4 | 4.0 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/ttvg.yaml | active | 2/2 | 4 | 4.0 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/hkaa0.yaml | active | 2/2 | 4 | 4.0 |
| https://raw.githubusercontent.com/Barabama/FreeNodes/main/nodes/nodefree.txt | active | 2/2 | 3 | 3.0 |
| https://raw.githubusercontent.com/mfbpn/tg_mfbpn_sub/main/trial.yaml | active | 2/2 | 3 | 3.0 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/mahdibland.yaml | active | 2/2 | 3 | 3.0 |
| https://raw.githubusercontent.com/Barabama/FreeNodes/main/nodes/v2rayshare.txt | active | 2/2 | 3 | 3.0 |
| https://raw.githubusercontent.com/Barabama/FreeNodes/main/nodes/wenode.txt | active | 2/2 | 3 | 3.0 |
| https://raw.githubusercontent.com/Barabama/FreeNodes/main/nodes/yudou66.txt | active | 2/2 | 3 | 3.0 |
| https://raw.githubusercontent.com/Barabama/FreeNodes/main/nodes/yudou66.yaml | active | 2/2 | 3 | 3.0 |
| https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/main/Base64/BLACK_SS+All_RUS_base64.txt | active | 2/2 | 3 | 3.0 |
| https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/main/BLACK_SS+All_RUS.txt | active | 2/2 | 3 | 3.0 |
| https://raw.githubusercontent.com/shaoyouvip/free/refs/heads/main/all.yaml | active | 2/2 | 2 | 2.0 |
| https://raw.githubusercontent.com/F0rc3Run/F0rc3Run/refs/heads/main/splitted-by-protocol/vmess.txt | active | 2/2 | 2 | 2.0 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/SFZY666.yaml | active | 2/2 | 2 | 2.0 |
| https://raw.githubusercontent.com/xiaoji235/airport-free/refs/heads/main/v2ray/v2rayshare.txt | active | 2/2 | 2 | 2.0 |
| https://raw.githubusercontent.com/hello-world-1989/cn-news/main/end-gfw-together | active | 2/2 | 2 | 2.0 |
| https://github.com/Au1rxx/free-vpn-subscriptions/raw/main/output/by-country/v2ray-base64-TW.txt | active | 2/2 | 2 | 2.0 |
| https://raw.githubusercontent.com/Barabama/FreeNodes/main/nodes/clashmeta.txt | active | 2/2 | 1 | 1.0 |
| https://raw.githubusercontent.com/vxiaov/free_proxies/main/links.txt | active | 2/2 | 1 | 1.0 |
| https://raw.githubusercontent.com/free-nodes/clashfree/main/clash{Ymd}.yml | active | 2/2 | 0 | 0.0 |
| https://proxypool.link/trojan/sub | active | 2/2 | 0 | 0.0 |
| https://raw.githubusercontent.com/DukeMehdi/FreeList-V2ray-Configs/refs/heads/main/Configs/VMESS-DukeMehdi-Configs.txt | active | 2/2 | 0 | 0.0 |
| https://github.com/AzadNetCH/Clash/raw/refs/heads/main/AzadNet.txt | active | 2/2 | 0 | 0.0 |
| https://raw.githubusercontent.com/aiboboxx/v2rayfree/main/README.md | active | 2/2 | 0 | 0.0 |
| https://raw.githubusercontent.com/aiboboxx/v2rayfree/refs/heads/main/README.md | active | 2/2 | 0 | 0.0 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/refs/heads/main/V2RAY.txt | active | 2/2 | 0 | 0.0 |
| https://node.freeclashnode.com/uploads/{Y}/{mm}/0-{Ymd}.yaml | active | 2/2 | 0 | 0.0 |
| https://raw.githubusercontent.com/Q3dlaXpoaQ/V2rayN_Clash_Node_Getter/main/APIs/sc0.yaml | active | 2/2 | 0 | 0.0 |
| https://raw.githubusercontent.com/Q3dlaXpoaQ/V2rayN_Clash_Node_Getter/refs/heads/main/APIs/sc0.yaml | active | 2/2 | 0 | 0.0 |
| https://node.freeclashnode.com/uploads/{Y}/{mm}/1-{Ymd}.yaml | active | 2/2 | 0 | 0.0 |
| https://raw.githubusercontent.com/peasoft/NoMoreWalls/master/list.yml | active | 2/2 | 0 | 0.0 |
| https://raw.githubusercontent.com/Misaka-blog/chromego_merge/main/sub/merged_proxies_new.yaml | active | 2/2 | 0 | 0.0 |
| https://raw.githubusercontent.com/Q3dlaXpoaQ/V2rayN_Clash_Node_Getter/main/APIs/sc1.yaml | active | 2/2 | 0 | 0.0 |
| https://raw.githubusercontent.com/Q3dlaXpoaQ/V2rayN_Clash_Node_Getter/refs/heads/main/APIs/sc1.yaml | active | 2/2 | 0 | 0.0 |
| https://raw.githubusercontent.com/chengaopan/AutoMergePublicNodes/master/list.yml | active | 2/2 | 0 | 0.0 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/chengaopan.yaml | active | 2/2 | 0 | 0.0 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/peasoft.yaml | active | 2/2 | 0 | 0.0 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/ripaojiedian.yaml | active | 2/2 | 0 | 0.0 |
| https://raw.githubusercontent.com/ripaojiedian/freenode/main/clash | active | 2/2 | 0 | 0.0 |
| https://raw.githubusercontent.com/Barabama/FreeNodes/main/nodes/clashmeta.yaml | active | 2/2 | 0 | 0.0 |
| https://node.freeclashnode.com/uploads/{Y}/{mm}/3-{Ymd}.yaml | active | 2/2 | 0 | 0.0 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/blue-Youtube.yaml | active | 2/2 | 0 | 0.0 |
| https://raw.githubusercontent.com/Q3dlaXpoaQ/V2rayN_Clash_Node_Getter/main/APIs/sc3.yaml | active | 2/2 | 0 | 0.0 |
| https://raw.githubusercontent.com/Q3dlaXpoaQ/V2rayN_Clash_Node_Getter/refs/heads/main/APIs/sc3.yaml | active | 2/2 | 0 | 0.0 |
| https://raw.githubusercontent.com/ermaozi/get_subscribe/main/subscribe/clash.yml | active | 2/2 | 0 | 0.0 |
| https://raw.githubusercontent.com/firefoxmmx2/v2rayshare_subcription/main/subscription/clash_sub.yaml | active | 2/2 | 0 | 0.0 |
| https://raw.githubusercontent.com/go4sharing/sub/main/sub.yaml | active | 2/2 | 0 | 0.0 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/ermaozi.yaml | active | 2/2 | 0 | 0.0 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/Pawdroid.yaml | active | 2/2 | 0 | 0.0 |
| https://node.freeclashnode.com/uploads/{Y}/{mm}/4-{Ymd}.yaml | active | 2/2 | 0 | 0.0 |
| https://github.com/mermeroo/V2RAY-CLASH-BASE64-Subscription.Links/raw/refs/heads/main/SUB%20LINKS | active | 2/2 | 0 | 0.0 |
| https://raw.githubusercontent.com/andigwandi/free-proxy/main/proxy_list.txt | active | 2/2 | 0 | 0.0 |
| https://raw.githubusercontent.com/asgharkapk/Sub-Config-Extractor/main/output_configs/clash/Ruk1ng001.yaml | active | 2/2 | 0 | 0.0 |
| https://raw.githubusercontent.com/asgharkapk/Sub-Config-Extractor/main/output_configs/surfboard/Barabama_ndnode.yaml | active | 2/2 | 0 | 0.0 |
| https://raw.githubusercontent.com/asgharkapk/Sub-Config-Extractor/main/output_configs/surfboard/Ruk1ng001.yaml | active | 2/2 | 0 | 0.0 |
| https://raw.githubusercontent.com/Barabama/FreeNodes/main/nodes/nodev2ray.txt | active | 2/2 | 0 | 0.0 |
| https://raw.githubusercontent.com/dpangestuw/Free-Proxy/main/All_proxies.txt | active | 2/2 | 0 | 0.0 |
| https://raw.githubusercontent.com/linzjian666/chromego_extractor/main/outputs/clash_meta.yaml | active | 2/2 | 0 | 0.0 |
| https://raw.githubusercontent.com/officialputuid/ProxyForEveryone/main/xResults/old-data/RAW.txt | active | 2/2 | 0 | 0.0 |
| https://raw.githubusercontent.com/officialputuid/ProxyForEveryone/main/xResults/RAW.txt | active | 2/2 | 0 | 0.0 |
| https://raw.githubusercontent.com/shahidbhutta/Clash/main/Router | active | 2/2 | 0 | 0.0 |
| https://raw.githubusercontent.com/shahidbhutta/Clash/refs/heads/main/Router | active | 2/2 | 0 | 0.0 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/changfengoss.yaml | active | 2/2 | 0 | 0.0 |
| https://raw.githubusercontent.com/SnapdragonLee/SystemProxy/master/dist/clash_config.yaml | active | 2/2 | 0 | 0.0 |
| https://raw.githubusercontent.com/xiaoji235/airport-free/refs/heads/main/v2ray/naidounode.txt | active | 2/2 | 0 | 0.0 |
| https://free.datiya.com/uploads/{Ymd}-clash.yaml | active | 2/2 | 0 | 0.0 |
| https://free.datiya.com/uploads/{Ymd}-v2ray.txt | active | 2/2 | 0 | 0.0 |
| https://raw.githubusercontent.com/Delta-Kronecker/V2ray-Config/main/config/clash.yaml | active | 2/2 | 0 | 0.0 |
| https://www.ermao.net/sub/clash/ermao.net | active | 2/2 | 0 | 0.0 |
| https://clashbest.github.io/uploads/{Y}/{mm}/0-{Ymd}.yaml | active | 2/2 | 0 | 0.0 |
| https://clashbest.github.io/uploads/{Y}/{mm}/1-{Ymd}.yaml | active | 2/2 | 0 | 0.0 |
| https://clashbest.github.io/uploads/{Y}/{mm}/3-{Ymd}.yaml | active | 2/2 | 0 | 0.0 |
| https://clashbest.github.io/uploads/{Y}/{mm}/4-{Ymd}.yaml | active | 2/2 | 0 | 0.0 |
| https://clashbest.github.io/uploads/{Y}/{mm}/{Ymd}.json | active | 2/2 | 0 | 0.0 |
| https://mihomoparty.github.io/uploads/{Y}/{mm}/0-{Ymd}.yaml | active | 2/2 | 0 | 0.0 |
| https://mihomoparty.github.io/uploads/{Y}/{mm}/1-{Ymd}.yaml | active | 2/2 | 0 | 0.0 |
| https://mihomoparty.github.io/uploads/{Y}/{mm}/4-{Ymd}.yaml | active | 2/2 | 0 | 0.0 |
| https://mihomoparty.github.io/uploads/{Y}/{mm}/{Ymd}.json | active | 2/2 | 0 | 0.0 |
| https://link.rittbo.kdns.fr/sub?token=8794e5157120a9982b0ceed9dcef5de7 | active | 0/2 | 0 | 0.0 |
| https://raw.githubusercontent.com/free-nodes/v2rayfree/main/v{ymd}1 | active | 0/2 | 0 | 0.0 |
| https://raw.githubusercontent.com/free-nodes/v2rayfree/main/v{ymd}2 | active | 0/2 | 0 | 0.0 |
| https://raw.githubusercontent.com/lagzian/SS-Collector/main/SS/trinity_clash.yaml | active | 0/2 | 0 | 0.0 |
| https://raw.githubusercontent.com/lagzian/SS-Collector/main/SS/TrinityBase | active | 0/2 | 0 | 0.0 |
| https://raw.githubusercontent.com/lagzian/SS-Collector/main/SS/VM_TrinityBase | active | 0/2 | 0 | 0.0 |
| https://raw.githubusercontent.com/MrMohebi/xray-proxy-grabber-telegram/master/collected-proxies/clash-meta/all.yaml | active | 0/2 | 0 | 0.0 |
| https://raw.githubusercontent.com/yorkLiu/FreeV2RayNode/main/v2ray.txt | active | 0/2 | 0 | 0.0 |

## 聚合源（按近 N 次平均拉取数降序）
| id | link | success_rate | last | avg |
|---|---|---|---|---|
| sinspired_scan | https://raw.githubusercontent.com/sinspired/airport/main/subs/merged/scan.txt | 2/2 | 20 | 20.0 |
| sinspired_col | https://raw.githubusercontent.com/sinspired/airport/main/subs/merged/col.txt | 2/2 | 17 | 17.0 |
| sinspired_cm | https://raw.githubusercontent.com/sinspired/airport/main/subs/merged/cm.txt | 2/2 | 12 | 12.0 |
