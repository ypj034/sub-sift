# sub-sift 运行报告

- 运行时间: 2026-08-20 03:04:35 CST
- 主清单订阅链接数: 177
- 本次实际拉取: 177（冷却/禁用跳过: 0）
- 拉取成功: 152，失败: 25
- 有效节点数（筛选后去重前）: 53303
- 输出节点数（去重后）: 12093
- GeoIP 数据源: mmdb: data/GeoLite2-Country.mmdb
- 输出文件: output/v2ray.txt, output/plain.txt

## 规则计数器
| 规则 | 原因 | 数量 |
|---|---|---|
| region_allowlist | region_not_allowed | 68420 |
| security_vless | unsafe_no_tls | 60588 |
| protocol_allowlist | protocol_not_allowed | 29351 |
| security_vmess | unsafe_no_tls | 23854 |
| security_trojan | unsafe_no_tls | 22132 |
| security_trojan | unsafe_allow_insecure | 6246 |
| security_vless | unsafe_allow_insecure | 6173 |
| validity_fields | invalid_field | 4472 |
| junk_keywords | junk_keyword | 2157 |
| validity_target | invalid_target | 250 |
| security_vmess | unsafe_weak_cipher | 6 |

## 主清单（按近 N 次总节点数降序）
| link | 状态 | success_rate | last | avg | total |
|---|---|---|---|---|---|
| https://raw.githubusercontent.com/ebrasha/free-v2ray-public-list/refs/heads/main/all_extracted_configs.txt | active | 1/1 | 11411 | 11411.0 | 11411 |
| https://raw.githubusercontent.com/DukeMehdi/FreeList-V2ray-Configs/refs/heads/main/Configs/VLESS-DukeMehdi-Configs.txt | active | 1/1 | 7046 | 7046.0 | 7046 |
| https://raw.githubusercontent.com/mheidari98/.proxy/main/all | active | 1/1 | 5323 | 5323.0 | 5323 |
| https://raw.githubusercontent.com/DukeMehdi/FreeList-V2ray-Configs/refs/heads/main/Configs/TROJAN-DukeMehdi-Configs.txt | active | 1/1 | 4531 | 4531.0 | 4531 |
| https://raw.githubusercontent.com/sakha1370/OpenRay/main/output/all_valid_proxies.txt | active | 1/1 | 3430 | 3430.0 | 3430 |
| https://raw.githubusercontent.com/sevcator/5ubscrpt10n/main/mini/m1n1-5ub-14.txt | active | 1/1 | 2337 | 2337.0 | 2337 |
| https://raw.githubusercontent.com/xiaoji235/airport-free/main/v2ray.txt | active | 1/1 | 2191 | 2191.0 | 2191 |
| https://raw.githubusercontent.com/xiaoji235/airport-free/refs/heads/main/v2ray/clashnodecc.txt | active | 1/1 | 2189 | 2189.0 | 2189 |
| https://raw.githubusercontent.com/liMilCo/v2r/main/configs.txt | active | 1/1 | 1962 | 1962.0 | 1962 |
| https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/main/all_configs.txt | active | 1/1 | 1662 | 1662.0 | 1662 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/soroushmirzaei.yaml | active | 1/1 | 1458 | 1458.0 | 1458 |
| https://raw.githubusercontent.com/sevcator/5ubscrpt10n/main/mini/m1n1-5ub-19.txt | active | 1/1 | 1287 | 1287.0 | 1287 |
| https://raw.githubusercontent.com/Leon406/SubCrawler/master/sub/share/vless | active | 1/1 | 975 | 975.0 | 975 |
| https://clashgithub.com/wp-content/uploads/rss/{Ymd}.txt | active | 1/1 | 642 | 642.0 | 642 |
| https://github.com/Au1rxx/free-vpn-subscriptions/raw/main/output/by-country/v2ray-base64-JP.txt | active | 1/1 | 608 | 608.0 | 608 |
| https://raw.githubusercontent.com/anaer/Sub/main/clash.yaml | active | 1/1 | 542 | 542.0 | 542 |
| https://raw.githubusercontent.com/asgharkapk/Sub-Config-Extractor/main/output_configs/mixed/Leon406/SubCrawler/sub/share/a11.yaml | active | 1/1 | 441 | 441.0 | 441 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/anaer.yaml | active | 1/1 | 357 | 357.0 | 357 |
| https://raw.githubusercontent.com/mahdibland/SSAggregator/master/sub/sub_merge_yaml.yml | active | 1/1 | 355 | 355.0 | 355 |
| https://raw.githubusercontent.com/mahdibland/V2RayAggregator/master/sub/sub_merge_yaml.yml | active | 1/1 | 355 | 355.0 | 355 |
| https://node.freeclashnode.com/uploads/{Y}/{mm}/2-{Ymd}.yaml | active | 1/1 | 297 | 297.0 | 297 |
| https://raw.githubusercontent.com/NiceVPN123/NiceVPN/main/utils/pool/output.yaml | active | 1/1 | 230 | 230.0 | 230 |
| https://raw.githubusercontent.com/NiceVPN123/NiceVPN/main/Clash.yaml | active | 1/1 | 229 | 229.0 | 229 |
| https://github.com/Au1rxx/free-vpn-subscriptions/raw/main/output/by-country/v2ray-base64-SG.txt | active | 1/1 | 228 | 228.0 | 228 |
| https://raw.githubusercontent.com/liMilCo/v2r/main/base64/2.txt | active | 1/1 | 218 | 218.0 | 218 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/coldwater-10.yaml | active | 1/1 | 199 | 199.0 | 199 |
| https://raw.githubusercontent.com/Q3dlaXpoaQ/V2rayN_Clash_Node_Getter/main/APIs/sc2.yaml | active | 1/1 | 195 | 195.0 | 195 |
| https://raw.githubusercontent.com/Q3dlaXpoaQ/V2rayN_Clash_Node_Getter/refs/heads/main/APIs/sc2.yaml | active | 1/1 | 195 | 195.0 | 195 |
| https://raw.githubusercontent.com/F0rc3Run/F0rc3Run/refs/heads/main/splitted-by-protocol/trojan.txt | active | 1/1 | 165 | 165.0 | 165 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/trial.yaml | active | 1/1 | 155 | 155.0 | 155 |
| https://raw.githubusercontent.com/barry-far/V2ray-config/main/Sub2.txt | active | 1/1 | 149 | 149.0 | 149 |
| https://raw.githubusercontent.com/MhdiTaheri/V2rayCollector/main/sub/mix | active | 1/1 | 140 | 140.0 | 140 |
| https://raw.githubusercontent.com/ALIILAPRO/v2rayNG-Config/main/sub.txt | active | 1/1 | 133 | 133.0 | 133 |
| https://github.com/Au1rxx/free-vpn-subscriptions/raw/main/output/by-country/v2ray-base64-HK.txt | active | 1/1 | 126 | 126.0 | 126 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/_previous.yaml | active | 1/1 | 108 | 108.0 | 108 |
| https://raw.githubusercontent.com/ts-sf/fly/main/clash | active | 1/1 | 82 | 82.0 | 82 |
| https://github.com/crackbest/V2ray-Config/raw/refs/heads/main/config.txt | active | 1/1 | 76 | 76.0 | 76 |
| https://raw.githubusercontent.com/crackbest/V2ray-Config/refs/heads/main/config.txt | active | 1/1 | 76 | 76.0 | 76 |
| https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/main/Base64/BLACK_VLESS_RUS_base64.txt | active | 1/1 | 76 | 76.0 | 76 |
| https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/main/BLACK_VLESS_RUS.txt | active | 1/1 | 76 | 76.0 | 76 |
| https://raw.githubusercontent.com/xtoolkit/TVC/main/subscriptions/meta/mix | active | 1/1 | 74 | 74.0 | 74 |
| https://github.com/Au1rxx/free-vpn-subscriptions/raw/main/output/by-country/v2ray-base64-US.txt | active | 1/1 | 65 | 65.0 | 65 |
| https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/main/Base64/BLACK_VLESS_RUS_mobile_base64.txt | active | 1/1 | 62 | 62.0 | 62 |
| https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/main/BLACK_VLESS_RUS_mobile.txt | active | 1/1 | 62 | 62.0 | 62 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/clashfree.yaml | active | 1/1 | 56 | 56.0 | 56 |
| https://raw.githubusercontent.com/F0rc3Run/F0rc3Run/refs/heads/main/splitted-by-protocol/vless.txt | active | 1/1 | 52 | 52.0 | 52 |
| https://raw.githubusercontent.com/ts-sf/fly/main/v2 | active | 1/1 | 51 | 51.0 | 51 |
| https://raw.githubusercontent.com/hans-thomas/v2ray-subscription/refs/heads/master/servers.txt | active | 1/1 | 47 | 47.0 | 47 |
| https://raw.githubusercontent.com/Arefgh72/v2ray-proxy-pars-tester/main/output/github_all.txt | active | 1/1 | 46 | 46.0 | 46 |
| https://raw.githubusercontent.com/acymz/AutoVPN/main/data/V2.txt | active | 1/1 | 44 | 44.0 | 44 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/snakem982.yaml | active | 1/1 | 27 | 27.0 | 27 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/zhangkaiitugithub.yaml | active | 1/1 | 27 | 27.0 | 27 |
| https://raw.githubusercontent.com/snakem982/proxypool/main/source/clash-meta-2.yaml | active | 1/1 | 27 | 27.0 | 27 |
| https://raw.githubusercontent.com/LoneKingCode/free-proxy-db/main/proxies/all.txt | active | 1/1 | 26 | 26.0 | 26 |
| https://raw.githubusercontent.com/Barabama/FreeNodes/main/nodes/blues.txt | active | 1/1 | 26 | 26.0 | 26 |
| https://raw.githubusercontent.com/Ruk1ng001/freeSub/main/clash.yaml | active | 1/1 | 22 | 22.0 | 22 |
| https://www.xrayvip.com/free.txt | active | 1/1 | 21 | 21.0 | 21 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/aiboboxx.yaml | active | 1/1 | 17 | 17.0 | 17 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/yudou.yaml | active | 1/1 | 17 | 17.0 | 17 |
| https://raw.githubusercontent.com/PangTouY00/Auto_proxy/main/Long_term_subscription_num | active | 1/1 | 17 | 17.0 | 17 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/tssf.yaml | active | 1/1 | 16 | 16.0 | 16 |
| https://raw.githubusercontent.com/Surfboardv2ray/v2ray-worker-sub/refs/heads/master/Eternity.txt | active | 1/1 | 15 | 15.0 | 15 |
| https://raw.githubusercontent.com/justVisiting992/xray-Config-Collector/main/clash.yaml | active | 1/1 | 14 | 14.0 | 14 |
| https://raw.githubusercontent.com/ovmvo/SubShare/main/sub/permanent/mihomo.yaml | active | 1/1 | 14 | 14.0 | 14 |
| https://raw.githubusercontent.com/peasoft/NoMoreWalls/master/list.meta.yml | active | 1/1 | 13 | 13.0 | 13 |
| https://raw.githubusercontent.com/peasoft/NoMoreWalls/master/snippets/nodes.meta.yml | active | 1/1 | 13 | 13.0 | 13 |
| https://github.com/Au1rxx/free-vpn-subscriptions/raw/main/output/by-country/v2ray-base64-KR.txt | active | 1/1 | 12 | 12.0 | 12 |
| https://raw.githubusercontent.com/MatinGhanbari/v2ray-configs/main/subscriptions/v2ray/subs/sub2.txt | active | 1/1 | 12 | 12.0 | 12 |
| https://raw.githubusercontent.com/HakurouKen/free-node/main/public | active | 1/1 | 10 | 10.0 | 10 |
| https://raw.githubusercontent.com/ggborr/FREEE-VPN/main/3v2 | active | 1/1 | 9 | 9.0 | 9 |
| https://raw.githubusercontent.com/shaoyouvip/free/refs/heads/main/all.yaml | active | 1/1 | 9 | 9.0 | 9 |
| https://raw.githubusercontent.com/mgit0001/test_clash/main/heima.txt | active | 1/1 | 8 | 8.0 | 8 |
| https://raw.githubusercontent.com/mgit0001/test_clash/refs/heads/main/heima.txt | active | 1/1 | 8 | 8.0 | 8 |
| https://raw.githubusercontent.com/Barabama/FreeNodes/main/nodes/ndnode.txt | active | 1/1 | 7 | 7.0 | 7 |
| https://raw.githubusercontent.com/vxiaov/free_proxies/main/clash/clash.provider.yaml | active | 1/1 | 7 | 7.0 | 7 |
| https://raw.githubusercontent.com/zhangkaiitugithub/passcro/main/speednodes.yaml | active | 1/1 | 7 | 7.0 | 7 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/_pool.yaml | active | 1/1 | 6 | 6.0 | 6 |
| https://raw.githubusercontent.com/actionsfz/v2ray/master/all.yaml | active | 1/1 | 6 | 6.0 | 6 |
| https://raw.githubusercontent.com/actionsfz/v2ray/refs/heads/master/all.yaml | active | 1/1 | 6 | 6.0 | 6 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/xrayvip.yaml | active | 1/1 | 6 | 6.0 | 6 |
| https://raw.githubusercontent.com/Shjpr9/Subs/refs/heads/main/sub.txt | active | 1/1 | 5 | 5.0 | 5 |
| https://raw.githubusercontent.com/mahdibland/ShadowsocksAggregator/master/Eternity.yml | active | 1/1 | 4 | 4.0 | 4 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/ttvg.yaml | active | 1/1 | 4 | 4.0 | 4 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/hkaa0.yaml | active | 1/1 | 4 | 4.0 | 4 |
| https://proxypool.link/trojan/sub | active | 1/1 | 3 | 3.0 | 3 |
| https://raw.githubusercontent.com/mfbpn/tg_mfbpn_sub/main/trial.yaml | active | 1/1 | 3 | 3.0 | 3 |
| https://raw.githubusercontent.com/F0rc3Run/F0rc3Run/refs/heads/main/splitted-by-protocol/vmess.txt | active | 1/1 | 3 | 3.0 | 3 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/mahdibland.yaml | active | 1/1 | 3 | 3.0 | 3 |
| https://raw.githubusercontent.com/Barabama/FreeNodes/main/nodes/nodefree.txt | active | 1/1 | 3 | 3.0 | 3 |
| https://raw.githubusercontent.com/Barabama/FreeNodes/main/nodes/v2rayshare.txt | active | 1/1 | 3 | 3.0 | 3 |
| https://raw.githubusercontent.com/Barabama/FreeNodes/main/nodes/wenode.txt | active | 1/1 | 3 | 3.0 | 3 |
| https://raw.githubusercontent.com/Barabama/FreeNodes/main/nodes/yudou66.txt | active | 1/1 | 3 | 3.0 | 3 |
| https://raw.githubusercontent.com/Barabama/FreeNodes/main/nodes/yudou66.yaml | active | 1/1 | 3 | 3.0 | 3 |
| https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/main/Base64/BLACK_SS+All_RUS_base64.txt | active | 1/1 | 2 | 2.0 | 2 |
| https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/main/BLACK_SS+All_RUS.txt | active | 1/1 | 2 | 2.0 | 2 |
| https://raw.githubusercontent.com/peacefish/nodefree/main/sub/proxy_cf.yaml | active | 1/1 | 2 | 2.0 | 2 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/SFZY666.yaml | active | 1/1 | 2 | 2.0 | 2 |
| https://raw.githubusercontent.com/xiaoji235/airport-free/refs/heads/main/v2ray/v2rayshare.txt | active | 1/1 | 2 | 2.0 | 2 |
| https://raw.githubusercontent.com/Pawdroid/Free-servers/main/sub | active | 1/1 | 2 | 2.0 | 2 |
| https://raw.githubusercontent.com/Pawdroid/Free-servers/refs/heads/main/sub | active | 1/1 | 2 | 2.0 | 2 |
| https://raw.githubusercontent.com/hello-world-1989/cn-news/main/end-gfw-together | active | 1/1 | 2 | 2.0 | 2 |
| https://raw.githubusercontent.com/free18/v2ray/main/c.yaml | active | 1/1 | 1 | 1.0 | 1 |
| https://github.com/Au1rxx/free-vpn-subscriptions/raw/main/output/by-country/v2ray-base64-TW.txt | active | 1/1 | 1 | 1.0 | 1 |
| https://raw.githubusercontent.com/Barabama/FreeNodes/main/nodes/clashmeta.txt | active | 1/1 | 1 | 1.0 | 1 |
| https://raw.githubusercontent.com/vxiaov/free_proxies/main/links.txt | active | 1/1 | 1 | 1.0 | 1 |
| https://raw.githubusercontent.com/Delta-Kronecker/V2ray-Config/main/config/clash.yaml | active | 1/1 | 0 | 0.0 | 0 |
| https://raw.githubusercontent.com/DukeMehdi/FreeList-V2ray-Configs/refs/heads/main/Configs/VMESS-DukeMehdi-Configs.txt | active | 1/1 | 0 | 0.0 | 0 |
| https://github.com/AzadNetCH/Clash/raw/refs/heads/main/AzadNet.txt | active | 1/1 | 0 | 0.0 | 0 |
| https://raw.githubusercontent.com/free-nodes/clashfree/main/clash{Ymd}.yml | active | 1/1 | 0 | 0.0 | 0 |
| https://raw.githubusercontent.com/aiboboxx/v2rayfree/main/README.md | active | 1/1 | 0 | 0.0 | 0 |
| https://raw.githubusercontent.com/aiboboxx/v2rayfree/refs/heads/main/README.md | active | 1/1 | 0 | 0.0 | 0 |
| https://clashbest.github.io/uploads/{Y}/{mm}/2-{Ymd}.txt | active | 0/1 | 0 | 0.0 | 0 |
| https://mihomoparty.github.io/uploads/{Y}/{mm}/2-{Ymd}.txt | active | 0/1 | 0 | 0.0 | 0 |
| https://mihomoparty.github.io/uploads/{Y}/{mm}/4-{Ymd}.txt | active | 0/1 | 0 | 0.0 | 0 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/refs/heads/main/V2RAY.txt | active | 1/1 | 0 | 0.0 | 0 |
| https://node.freeclashnode.com/uploads/{Y}/{mm}/0-{Ymd}.yaml | active | 1/1 | 0 | 0.0 | 0 |
| https://raw.githubusercontent.com/Q3dlaXpoaQ/V2rayN_Clash_Node_Getter/main/APIs/sc0.yaml | active | 1/1 | 0 | 0.0 | 0 |
| https://raw.githubusercontent.com/Q3dlaXpoaQ/V2rayN_Clash_Node_Getter/refs/heads/main/APIs/sc0.yaml | active | 1/1 | 0 | 0.0 | 0 |
| https://clashbest.github.io/uploads/{Y}/{mm}/0-{Ymd}.txt | active | 0/1 | 0 | 0.0 | 0 |
| https://node.freeclashnode.com/uploads/{Y}/{mm}/1-{Ymd}.yaml | active | 1/1 | 0 | 0.0 | 0 |
| https://raw.githubusercontent.com/peasoft/NoMoreWalls/master/list.yml | active | 1/1 | 0 | 0.0 | 0 |
| https://raw.githubusercontent.com/Misaka-blog/chromego_merge/main/sub/merged_proxies_new.yaml | active | 1/1 | 0 | 0.0 | 0 |
| https://raw.githubusercontent.com/Q3dlaXpoaQ/V2rayN_Clash_Node_Getter/main/APIs/sc1.yaml | active | 1/1 | 0 | 0.0 | 0 |
| https://raw.githubusercontent.com/Q3dlaXpoaQ/V2rayN_Clash_Node_Getter/refs/heads/main/APIs/sc1.yaml | active | 1/1 | 0 | 0.0 | 0 |
| https://raw.githubusercontent.com/chengaopan/AutoMergePublicNodes/master/list.yml | active | 1/1 | 0 | 0.0 | 0 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/chengaopan.yaml | active | 1/1 | 0 | 0.0 | 0 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/peasoft.yaml | active | 1/1 | 0 | 0.0 | 0 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/ripaojiedian.yaml | active | 1/1 | 0 | 0.0 | 0 |
| https://free.datiya.com/uploads/{Ymd}-clash.yaml | active | 0/1 | 0 | 0.0 | 0 |
| https://raw.githubusercontent.com/ripaojiedian/freenode/main/clash | active | 1/1 | 0 | 0.0 | 0 |
| https://raw.githubusercontent.com/Barabama/FreeNodes/main/nodes/clashmeta.yaml | active | 1/1 | 0 | 0.0 | 0 |
| https://node.freeclashnode.com/uploads/{Y}/{mm}/3-{Ymd}.yaml | active | 1/1 | 0 | 0.0 | 0 |
| https://clashbest.github.io/uploads/{Y}/{mm}/1-{Ymd}.txt | active | 0/1 | 0 | 0.0 | 0 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/blue-Youtube.yaml | active | 1/1 | 0 | 0.0 | 0 |
| https://raw.githubusercontent.com/Q3dlaXpoaQ/V2rayN_Clash_Node_Getter/main/APIs/sc3.yaml | active | 1/1 | 0 | 0.0 | 0 |
| https://raw.githubusercontent.com/Q3dlaXpoaQ/V2rayN_Clash_Node_Getter/refs/heads/main/APIs/sc3.yaml | active | 1/1 | 0 | 0.0 | 0 |
| https://www.ermao.net/sub/clash/ermao.net | active | 1/1 | 0 | 0.0 | 0 |
| https://raw.githubusercontent.com/ermaozi/get_subscribe/main/subscribe/clash.yml | active | 1/1 | 0 | 0.0 | 0 |
| https://raw.githubusercontent.com/firefoxmmx2/v2rayshare_subcription/main/subscription/clash_sub.yaml | active | 1/1 | 0 | 0.0 | 0 |
| https://raw.githubusercontent.com/go4sharing/sub/main/sub.yaml | active | 1/1 | 0 | 0.0 | 0 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/ermaozi.yaml | active | 1/1 | 0 | 0.0 | 0 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/Pawdroid.yaml | active | 1/1 | 0 | 0.0 | 0 |
| https://clashbest.github.io/uploads/{Y}/{mm}/0-{Ymd}.yaml | active | 0/1 | 0 | 0.0 | 0 |
| https://clashbest.github.io/uploads/{Y}/{mm}/1-{Ymd}.yaml | active | 0/1 | 0 | 0.0 | 0 |
| https://clashbest.github.io/uploads/{Y}/{mm}/2-{Ymd}.yaml | active | 0/1 | 0 | 0.0 | 0 |
| https://clashbest.github.io/uploads/{Y}/{mm}/3-{Ymd}.yaml | active | 0/1 | 0 | 0.0 | 0 |
| https://clashbest.github.io/uploads/{Y}/{mm}/4-{Ymd}.yaml | active | 0/1 | 0 | 0.0 | 0 |
| https://clashbest.github.io/uploads/{Y}/{mm}/{Ymd}.json | active | 0/1 | 0 | 0.0 | 0 |
| https://mihomoparty.github.io/uploads/{Y}/{mm}/0-{Ymd}.yaml | active | 0/1 | 0 | 0.0 | 0 |
| https://mihomoparty.github.io/uploads/{Y}/{mm}/1-{Ymd}.yaml | active | 0/1 | 0 | 0.0 | 0 |
| https://mihomoparty.github.io/uploads/{Y}/{mm}/4-{Ymd}.yaml | active | 0/1 | 0 | 0.0 | 0 |
| https://mihomoparty.github.io/uploads/{Y}/{mm}/{Ymd}.json | active | 0/1 | 0 | 0.0 | 0 |
| https://node.freeclashnode.com/uploads/{Y}/{mm}/4-{Ymd}.yaml | active | 1/1 | 0 | 0.0 | 0 |
| https://free.datiya.com/uploads/{Ymd}-v2ray.txt | active | 0/1 | 0 | 0.0 | 0 |
| https://github.com/mermeroo/V2RAY-CLASH-BASE64-Subscription.Links/raw/refs/heads/main/SUB%20LINKS | active | 1/1 | 0 | 0.0 | 0 |
| https://link.rittbo.kdns.fr/sub?token=8794e5157120a9982b0ceed9dcef5de7 | active | 0/1 | 0 | 0.0 | 0 |
| https://raw.githubusercontent.com/andigwandi/free-proxy/main/proxy_list.txt | active | 1/1 | 0 | 0.0 | 0 |
| https://raw.githubusercontent.com/asgharkapk/Sub-Config-Extractor/main/output_configs/clash/Ruk1ng001.yaml | active | 1/1 | 0 | 0.0 | 0 |
| https://raw.githubusercontent.com/asgharkapk/Sub-Config-Extractor/main/output_configs/surfboard/Barabama_ndnode.yaml | active | 1/1 | 0 | 0.0 | 0 |
| https://raw.githubusercontent.com/asgharkapk/Sub-Config-Extractor/main/output_configs/surfboard/Ruk1ng001.yaml | active | 1/1 | 0 | 0.0 | 0 |
| https://raw.githubusercontent.com/Barabama/FreeNodes/main/nodes/nodev2ray.txt | active | 1/1 | 0 | 0.0 | 0 |
| https://raw.githubusercontent.com/dpangestuw/Free-Proxy/main/All_proxies.txt | active | 1/1 | 0 | 0.0 | 0 |
| https://raw.githubusercontent.com/free-nodes/v2rayfree/main/v{ymd}1 | active | 0/1 | 0 | 0.0 | 0 |
| https://raw.githubusercontent.com/free-nodes/v2rayfree/main/v{ymd}2 | active | 0/1 | 0 | 0.0 | 0 |
| https://raw.githubusercontent.com/lagzian/SS-Collector/main/SS/trinity_clash.yaml | active | 0/1 | 0 | 0.0 | 0 |
| https://raw.githubusercontent.com/lagzian/SS-Collector/main/SS/TrinityBase | active | 0/1 | 0 | 0.0 | 0 |
| https://raw.githubusercontent.com/lagzian/SS-Collector/main/SS/VM_TrinityBase | active | 0/1 | 0 | 0.0 | 0 |
| https://raw.githubusercontent.com/linzjian666/chromego_extractor/main/outputs/clash_meta.yaml | active | 1/1 | 0 | 0.0 | 0 |
| https://raw.githubusercontent.com/MrMohebi/xray-proxy-grabber-telegram/master/collected-proxies/clash-meta/all.yaml | active | 0/1 | 0 | 0.0 | 0 |
| https://raw.githubusercontent.com/officialputuid/ProxyForEveryone/main/xResults/old-data/RAW.txt | active | 1/1 | 0 | 0.0 | 0 |
| https://raw.githubusercontent.com/officialputuid/ProxyForEveryone/main/xResults/RAW.txt | active | 1/1 | 0 | 0.0 | 0 |
| https://raw.githubusercontent.com/shahidbhutta/Clash/main/Router | active | 1/1 | 0 | 0.0 | 0 |
| https://raw.githubusercontent.com/shahidbhutta/Clash/refs/heads/main/Router | active | 1/1 | 0 | 0.0 | 0 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/changfengoss.yaml | active | 1/1 | 0 | 0.0 | 0 |
| https://raw.githubusercontent.com/SnapdragonLee/SystemProxy/master/dist/clash_config.yaml | active | 1/1 | 0 | 0.0 | 0 |
| https://raw.githubusercontent.com/xiaoji235/airport-free/refs/heads/main/v2ray/naidounode.txt | active | 1/1 | 0 | 0.0 | 0 |
| https://raw.githubusercontent.com/yorkLiu/FreeV2RayNode/main/v2ray.txt | active | 0/1 | 0 | 0.0 | 0 |

## 聚合源（按近 N 次平均拉取数降序）
| id | link | success_rate | last | avg |
|---|---|---|---|---|
| sinspired_scan | https://raw.githubusercontent.com/sinspired/airport/main/subs/merged/scan.txt | 1/1 | 20 | 20.0 |
| sinspired_col | https://raw.githubusercontent.com/sinspired/airport/main/subs/merged/col.txt | 1/1 | 17 | 17.0 |
| sinspired_cm | https://raw.githubusercontent.com/sinspired/airport/main/subs/merged/cm.txt | 1/1 | 12 | 12.0 |

## 重叠度
- 被多个来源（≥2）拉到的订阅链接: 0 / 177
- 占比: 0.0%
