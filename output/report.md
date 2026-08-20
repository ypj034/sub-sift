# sub-sift 运行报告

- 运行时间: 2026-08-20 13:53:37 CST
- 主清单订阅链接数: 177
- 本次实际拉取: 177（冷却/禁用跳过: 0）
- 拉取成功: 169，失败: 8
- 有效节点数（筛选后去重前）: 56286
- 输出节点数（去重后）: 12256
- GeoIP 数据源: mmdb: data/GeoLite2-Country.mmdb
- 输出文件: output/v2ray.txt, output/plain.txt

## 规则计数器
| 规则 | 拒绝数 |
|---|---|
| protocol_allowlist | 30866 |
| validity | 4919 |
| security_vmess | 24656 |
| security_vless | 71619 |
| security_trojan | 31468 |
| junk_keywords | 2152 |
| region_allowlist | 73150 |

## 主清单（active → 冷却 → disabled；组内按 avg 降序）
| link | 状态 | success_rate | last | avg |
|---|---|---|---|---|
| https://raw.githubusercontent.com/ebrasha/free-v2ray-public-list/refs/heads/main/all_extracted_configs.txt | active | 4/4 | 10709 | 10830.2 |
| https://raw.githubusercontent.com/DukeMehdi/FreeList-V2ray-Configs/refs/heads/main/Configs/VLESS-DukeMehdi-Configs.txt | active | 4/4 | 7099 | 7067.5 |
| https://raw.githubusercontent.com/mheidari98/.proxy/main/all | active | 4/4 | 5644 | 5424.2 |
| https://raw.githubusercontent.com/DukeMehdi/FreeList-V2ray-Configs/refs/heads/main/Configs/TROJAN-DukeMehdi-Configs.txt | active | 4/4 | 3742 | 3864.8 |
| https://raw.githubusercontent.com/sakha1370/OpenRay/main/output/all_valid_proxies.txt | active | 4/4 | 3451 | 3435.0 |
| https://raw.githubusercontent.com/sevcator/5ubscrpt10n/main/mini/m1n1-5ub-14.txt | active | 4/4 | 2339 | 2338.5 |
| https://raw.githubusercontent.com/xiaoji235/airport-free/main/v2ray.txt | active | 4/4 | 2191 | 2191.0 |
| https://raw.githubusercontent.com/xiaoji235/airport-free/refs/heads/main/v2ray/clashnodecc.txt | active | 4/4 | 2189 | 2189.0 |
| https://raw.githubusercontent.com/liMilCo/v2r/main/configs.txt | active | 4/4 | 1604 | 1783.2 |
| https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/main/all_configs.txt | active | 4/4 | 1625 | 1652.0 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/soroushmirzaei.yaml | active | 4/4 | 1443 | 1446.8 |
| https://raw.githubusercontent.com/sevcator/5ubscrpt10n/main/mini/m1n1-5ub-19.txt | active | 4/4 | 1294 | 1292.2 |
| https://raw.githubusercontent.com/Leon406/SubCrawler/master/sub/share/vless | active | 4/4 | 1110 | 1073.2 |
| https://clashgithub.com/wp-content/uploads/rss/{Ymd}.txt | active | 4/4 | 642 | 642.0 |
| https://raw.githubusercontent.com/anaer/Sub/main/clash.yaml | active | 4/4 | 542 | 542.0 |
| https://clashbest.github.io/uploads/{Y}/{mm}/2-{Ymd}.txt | active | 1/4 | 1824 | 456.0 |
| https://mihomoparty.github.io/uploads/{Y}/{mm}/2-{Ymd}.txt | active | 1/4 | 1824 | 456.0 |
| https://raw.githubusercontent.com/asgharkapk/Sub-Config-Extractor/main/output_configs/mixed/Leon406/SubCrawler/sub/share/a11.yaml | active | 4/4 | 441 | 441.0 |
| https://github.com/Au1rxx/free-vpn-subscriptions/raw/main/output/by-country/v2ray-base64-JP.txt | active | 4/4 | 378 | 435.5 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/anaer.yaml | active | 4/4 | 351 | 352.5 |
| https://raw.githubusercontent.com/mahdibland/SSAggregator/master/sub/sub_merge_yaml.yml | active | 4/4 | 349 | 352.0 |
| https://raw.githubusercontent.com/mahdibland/V2RayAggregator/master/sub/sub_merge_yaml.yml | active | 4/4 | 349 | 352.0 |
| https://raw.githubusercontent.com/free-nodes/clashfree/main/clash{Ymd}.yml | active | 4/4 | 0 | 297.0 |
| https://node.freeclashnode.com/uploads/{Y}/{mm}/2-{Ymd}.yaml | active | 4/4 | 297 | 297.0 |
| https://raw.githubusercontent.com/NiceVPN123/NiceVPN/main/utils/pool/output.yaml | active | 4/4 | 230 | 230.0 |
| https://raw.githubusercontent.com/NiceVPN123/NiceVPN/main/Clash.yaml | active | 4/4 | 229 | 229.0 |
| https://github.com/Au1rxx/free-vpn-subscriptions/raw/main/output/by-country/v2ray-base64-SG.txt | active | 4/4 | 223 | 224.2 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/coldwater-10.yaml | active | 4/4 | 199 | 199.0 |
| https://raw.githubusercontent.com/Q3dlaXpoaQ/V2rayN_Clash_Node_Getter/main/APIs/sc2.yaml | active | 4/4 | 195 | 195.0 |
| https://raw.githubusercontent.com/Q3dlaXpoaQ/V2rayN_Clash_Node_Getter/refs/heads/main/APIs/sc2.yaml | active | 4/4 | 195 | 195.0 |
| https://raw.githubusercontent.com/liMilCo/v2r/main/base64/2.txt | active | 4/4 | 161 | 189.5 |
| https://mihomoparty.github.io/uploads/{Y}/{mm}/4-{Ymd}.txt | active | 1/4 | 626 | 156.5 |
| https://raw.githubusercontent.com/F0rc3Run/F0rc3Run/refs/heads/main/splitted-by-protocol/trojan.txt | active | 4/4 | 151 | 154.5 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/trial.yaml | active | 4/4 | 154 | 154.2 |
| https://raw.githubusercontent.com/barry-far/V2ray-config/main/Sub2.txt | active | 4/4 | 141 | 152.2 |
| https://raw.githubusercontent.com/MhdiTaheri/V2rayCollector/main/sub/mix | active | 4/4 | 131 | 136.8 |
| https://raw.githubusercontent.com/ALIILAPRO/v2rayNG-Config/main/sub.txt | active | 4/4 | 134 | 133.8 |
| https://github.com/Au1rxx/free-vpn-subscriptions/raw/main/output/by-country/v2ray-base64-HK.txt | active | 4/4 | 128 | 127.5 |
| https://github.com/Au1rxx/free-vpn-subscriptions/raw/main/output/by-country/v2ray-base64-US.txt | active | 4/4 | 144 | 124.2 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/_previous.yaml | active | 4/4 | 108 | 108.0 |
| https://raw.githubusercontent.com/xtoolkit/TVC/main/subscriptions/meta/mix | active | 4/4 | 76 | 77.2 |
| https://raw.githubusercontent.com/ts-sf/fly/main/clash | active | 4/4 | 69 | 75.2 |
| https://github.com/crackbest/V2ray-Config/raw/refs/heads/main/config.txt | active | 4/4 | 73 | 74.8 |
| https://raw.githubusercontent.com/crackbest/V2ray-Config/refs/heads/main/config.txt | active | 4/4 | 73 | 74.8 |
| https://clashbest.github.io/uploads/{Y}/{mm}/2-{Ymd}.yaml | active | 1/4 | 297 | 74.2 |
| https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/main/Base64/BLACK_VLESS_RUS_base64.txt | active | 4/4 | 67 | 62.0 |
| https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/main/BLACK_VLESS_RUS.txt | active | 4/4 | 67 | 62.0 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/clashfree.yaml | active | 4/4 | 56 | 56.0 |
| https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/main/Base64/BLACK_VLESS_RUS_mobile_base64.txt | active | 4/4 | 54 | 52.0 |
| https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/main/BLACK_VLESS_RUS_mobile.txt | active | 4/4 | 54 | 52.0 |
| https://raw.githubusercontent.com/ts-sf/fly/main/v2 | active | 4/4 | 45 | 48.0 |
| https://raw.githubusercontent.com/hans-thomas/v2ray-subscription/refs/heads/master/servers.txt | active | 4/4 | 47 | 47.0 |
| https://raw.githubusercontent.com/Arefgh72/v2ray-proxy-pars-tester/main/output/github_all.txt | active | 4/4 | 46 | 46.0 |
| https://raw.githubusercontent.com/F0rc3Run/F0rc3Run/refs/heads/main/splitted-by-protocol/vless.txt | active | 4/4 | 38 | 41.5 |
| https://raw.githubusercontent.com/acymz/AutoVPN/main/data/V2.txt | active | 4/4 | 41 | 38.8 |
| https://raw.githubusercontent.com/LoneKingCode/free-proxy-db/main/proxies/all.txt | active | 4/4 | 27 | 26.2 |
| https://raw.githubusercontent.com/Barabama/FreeNodes/main/nodes/blues.txt | active | 4/4 | 26 | 26.0 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/snakem982.yaml | active | 4/4 | 25 | 25.5 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/zhangkaiitugithub.yaml | active | 4/4 | 25 | 25.5 |
| https://raw.githubusercontent.com/Ruk1ng001/freeSub/main/clash.yaml | active | 4/4 | 22 | 22.0 |
| https://raw.githubusercontent.com/snakem982/proxypool/main/source/clash-meta-2.yaml | active | 4/4 | 12 | 18.8 |
| https://github.com/Au1rxx/free-vpn-subscriptions/raw/main/output/by-country/v2ray-base64-KR.txt | active | 4/4 | 20 | 18.0 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/yudou.yaml | active | 4/4 | 17 | 17.0 |
| https://www.xrayvip.com/free.txt | active | 4/4 | 15 | 16.5 |
| https://raw.githubusercontent.com/PangTouY00/Auto_proxy/main/Long_term_subscription_num | active | 4/4 | 16 | 16.5 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/aiboboxx.yaml | active | 4/4 | 16 | 16.2 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/tssf.yaml | active | 4/4 | 16 | 16.0 |
| https://clashbest.github.io/uploads/{Y}/{mm}/1-{Ymd}.txt | active | 1/4 | 61 | 15.2 |
| https://raw.githubusercontent.com/Surfboardv2ray/v2ray-worker-sub/refs/heads/master/Eternity.txt | active | 4/4 | 15 | 15.0 |
| https://raw.githubusercontent.com/justVisiting992/xray-Config-Collector/main/clash.yaml | active | 4/4 | 15 | 14.8 |
| https://raw.githubusercontent.com/ovmvo/SubShare/main/sub/permanent/mihomo.yaml | active | 4/4 | 14 | 14.0 |
| https://raw.githubusercontent.com/peasoft/NoMoreWalls/master/list.meta.yml | active | 4/4 | 16 | 12.8 |
| https://raw.githubusercontent.com/peasoft/NoMoreWalls/master/snippets/nodes.meta.yml | active | 4/4 | 16 | 12.8 |
| https://clashbest.github.io/uploads/{Y}/{mm}/0-{Ymd}.txt | active | 1/4 | 51 | 12.8 |
| https://raw.githubusercontent.com/MatinGhanbari/v2ray-configs/main/subscriptions/v2ray/subs/sub2.txt | active | 4/4 | 12 | 12.0 |
| https://raw.githubusercontent.com/ggborr/FREEE-VPN/main/3v2 | active | 4/4 | 9 | 9.0 |
| https://raw.githubusercontent.com/mgit0001/test_clash/main/heima.txt | active | 4/4 | 8 | 8.0 |
| https://raw.githubusercontent.com/mgit0001/test_clash/refs/heads/main/heima.txt | active | 4/4 | 8 | 8.0 |
| https://raw.githubusercontent.com/Barabama/FreeNodes/main/nodes/ndnode.txt | active | 4/4 | 7 | 7.0 |
| https://raw.githubusercontent.com/vxiaov/free_proxies/main/clash/clash.provider.yaml | active | 4/4 | 7 | 7.0 |
| https://raw.githubusercontent.com/zhangkaiitugithub/passcro/main/speednodes.yaml | active | 4/4 | 7 | 7.0 |
| https://raw.githubusercontent.com/shaoyouvip/free/refs/heads/main/all.yaml | active | 4/4 | 9 | 6.5 |
| https://raw.githubusercontent.com/HakurouKen/free-node/main/public | active | 4/4 | 5 | 6.2 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/_pool.yaml | active | 4/4 | 6 | 6.0 |
| https://raw.githubusercontent.com/actionsfz/v2ray/master/all.yaml | active | 4/4 | 6 | 6.0 |
| https://raw.githubusercontent.com/actionsfz/v2ray/refs/heads/master/all.yaml | active | 4/4 | 6 | 6.0 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/xrayvip.yaml | active | 4/4 | 6 | 6.0 |
| https://raw.githubusercontent.com/Shjpr9/Subs/refs/heads/main/sub.txt | active | 4/4 | 5 | 5.0 |
| https://raw.githubusercontent.com/Pawdroid/Free-servers/main/sub | active | 4/4 | 5 | 4.2 |
| https://raw.githubusercontent.com/Pawdroid/Free-servers/refs/heads/main/sub | active | 4/4 | 5 | 4.2 |
| https://raw.githubusercontent.com/mahdibland/ShadowsocksAggregator/master/Eternity.yml | active | 4/4 | 4 | 4.0 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/ttvg.yaml | active | 4/4 | 4 | 4.0 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/hkaa0.yaml | active | 4/4 | 4 | 4.0 |
| https://raw.githubusercontent.com/mfbpn/tg_mfbpn_sub/main/trial.yaml | active | 4/4 | 3 | 3.0 |
| https://raw.githubusercontent.com/F0rc3Run/F0rc3Run/refs/heads/main/splitted-by-protocol/vmess.txt | active | 4/4 | 3 | 3.0 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/mahdibland.yaml | active | 4/4 | 3 | 3.0 |
| https://raw.githubusercontent.com/Barabama/FreeNodes/main/nodes/nodefree.txt | active | 4/4 | 3 | 3.0 |
| https://raw.githubusercontent.com/Barabama/FreeNodes/main/nodes/v2rayshare.txt | active | 4/4 | 3 | 3.0 |
| https://raw.githubusercontent.com/Barabama/FreeNodes/main/nodes/wenode.txt | active | 4/4 | 3 | 3.0 |
| https://raw.githubusercontent.com/Barabama/FreeNodes/main/nodes/yudou66.txt | active | 4/4 | 3 | 3.0 |
| https://raw.githubusercontent.com/Barabama/FreeNodes/main/nodes/yudou66.yaml | active | 4/4 | 3 | 3.0 |
| https://raw.githubusercontent.com/peacefish/nodefree/main/sub/proxy_cf.yaml | active | 4/4 | 6 | 3.0 |
| https://proxypool.link/trojan/sub | active | 4/4 | 2 | 2.0 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/SFZY666.yaml | active | 4/4 | 2 | 2.0 |
| https://raw.githubusercontent.com/xiaoji235/airport-free/refs/heads/main/v2ray/v2rayshare.txt | active | 4/4 | 2 | 2.0 |
| https://raw.githubusercontent.com/hello-world-1989/cn-news/main/end-gfw-together | active | 4/4 | 2 | 2.0 |
| https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/main/Base64/BLACK_SS+All_RUS_base64.txt | active | 4/4 | 3 | 2.0 |
| https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/main/BLACK_SS+All_RUS.txt | active | 4/4 | 3 | 2.0 |
| https://github.com/Au1rxx/free-vpn-subscriptions/raw/main/output/by-country/v2ray-base64-TW.txt | active | 4/4 | 2 | 1.8 |
| https://raw.githubusercontent.com/free18/v2ray/main/c.yaml | active | 4/4 | 1 | 1.0 |
| https://raw.githubusercontent.com/Barabama/FreeNodes/main/nodes/clashmeta.txt | active | 4/4 | 1 | 1.0 |
| https://raw.githubusercontent.com/vxiaov/free_proxies/main/links.txt | active | 4/4 | 1 | 1.0 |
| https://raw.githubusercontent.com/Delta-Kronecker/V2ray-Config/main/config/clash.yaml | active | 4/4 | 0 | 0.0 |
| https://raw.githubusercontent.com/DukeMehdi/FreeList-V2ray-Configs/refs/heads/main/Configs/VMESS-DukeMehdi-Configs.txt | active | 4/4 | 0 | 0.0 |
| https://github.com/AzadNetCH/Clash/raw/refs/heads/main/AzadNet.txt | active | 4/4 | 0 | 0.0 |
| https://raw.githubusercontent.com/aiboboxx/v2rayfree/main/README.md | active | 4/4 | 0 | 0.0 |
| https://raw.githubusercontent.com/aiboboxx/v2rayfree/refs/heads/main/README.md | active | 4/4 | 0 | 0.0 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/refs/heads/main/V2RAY.txt | active | 4/4 | 0 | 0.0 |
| https://node.freeclashnode.com/uploads/{Y}/{mm}/0-{Ymd}.yaml | active | 4/4 | 0 | 0.0 |
| https://raw.githubusercontent.com/Q3dlaXpoaQ/V2rayN_Clash_Node_Getter/main/APIs/sc0.yaml | active | 4/4 | 0 | 0.0 |
| https://raw.githubusercontent.com/Q3dlaXpoaQ/V2rayN_Clash_Node_Getter/refs/heads/main/APIs/sc0.yaml | active | 4/4 | 0 | 0.0 |
| https://node.freeclashnode.com/uploads/{Y}/{mm}/1-{Ymd}.yaml | active | 4/4 | 0 | 0.0 |
| https://raw.githubusercontent.com/peasoft/NoMoreWalls/master/list.yml | active | 4/4 | 0 | 0.0 |
| https://raw.githubusercontent.com/Misaka-blog/chromego_merge/main/sub/merged_proxies_new.yaml | active | 4/4 | 0 | 0.0 |
| https://raw.githubusercontent.com/Q3dlaXpoaQ/V2rayN_Clash_Node_Getter/main/APIs/sc1.yaml | active | 4/4 | 0 | 0.0 |
| https://raw.githubusercontent.com/Q3dlaXpoaQ/V2rayN_Clash_Node_Getter/refs/heads/main/APIs/sc1.yaml | active | 4/4 | 0 | 0.0 |
| https://raw.githubusercontent.com/chengaopan/AutoMergePublicNodes/master/list.yml | active | 4/4 | 0 | 0.0 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/chengaopan.yaml | active | 4/4 | 0 | 0.0 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/peasoft.yaml | active | 4/4 | 0 | 0.0 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/ripaojiedian.yaml | active | 4/4 | 0 | 0.0 |
| https://raw.githubusercontent.com/ripaojiedian/freenode/main/clash | active | 4/4 | 0 | 0.0 |
| https://raw.githubusercontent.com/Barabama/FreeNodes/main/nodes/clashmeta.yaml | active | 4/4 | 0 | 0.0 |
| https://node.freeclashnode.com/uploads/{Y}/{mm}/3-{Ymd}.yaml | active | 4/4 | 0 | 0.0 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/blue-Youtube.yaml | active | 4/4 | 0 | 0.0 |
| https://raw.githubusercontent.com/Q3dlaXpoaQ/V2rayN_Clash_Node_Getter/main/APIs/sc3.yaml | active | 4/4 | 0 | 0.0 |
| https://raw.githubusercontent.com/Q3dlaXpoaQ/V2rayN_Clash_Node_Getter/refs/heads/main/APIs/sc3.yaml | active | 4/4 | 0 | 0.0 |
| https://www.ermao.net/sub/clash/ermao.net | active | 4/4 | 0 | 0.0 |
| https://raw.githubusercontent.com/ermaozi/get_subscribe/main/subscribe/clash.yml | active | 4/4 | 0 | 0.0 |
| https://raw.githubusercontent.com/firefoxmmx2/v2rayshare_subcription/main/subscription/clash_sub.yaml | active | 4/4 | 0 | 0.0 |
| https://raw.githubusercontent.com/go4sharing/sub/main/sub.yaml | active | 4/4 | 0 | 0.0 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/ermaozi.yaml | active | 4/4 | 0 | 0.0 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/Pawdroid.yaml | active | 4/4 | 0 | 0.0 |
| https://node.freeclashnode.com/uploads/{Y}/{mm}/4-{Ymd}.yaml | active | 4/4 | 0 | 0.0 |
| https://github.com/mermeroo/V2RAY-CLASH-BASE64-Subscription.Links/raw/refs/heads/main/SUB%20LINKS | active | 4/4 | 0 | 0.0 |
| https://raw.githubusercontent.com/andigwandi/free-proxy/main/proxy_list.txt | active | 4/4 | 0 | 0.0 |
| https://raw.githubusercontent.com/asgharkapk/Sub-Config-Extractor/main/output_configs/clash/Ruk1ng001.yaml | active | 4/4 | 0 | 0.0 |
| https://raw.githubusercontent.com/asgharkapk/Sub-Config-Extractor/main/output_configs/surfboard/Barabama_ndnode.yaml | active | 4/4 | 0 | 0.0 |
| https://raw.githubusercontent.com/asgharkapk/Sub-Config-Extractor/main/output_configs/surfboard/Ruk1ng001.yaml | active | 4/4 | 0 | 0.0 |
| https://raw.githubusercontent.com/Barabama/FreeNodes/main/nodes/nodev2ray.txt | active | 4/4 | 0 | 0.0 |
| https://raw.githubusercontent.com/dpangestuw/Free-Proxy/main/All_proxies.txt | active | 4/4 | 0 | 0.0 |
| https://raw.githubusercontent.com/linzjian666/chromego_extractor/main/outputs/clash_meta.yaml | active | 4/4 | 0 | 0.0 |
| https://raw.githubusercontent.com/officialputuid/ProxyForEveryone/main/xResults/old-data/RAW.txt | active | 4/4 | 0 | 0.0 |
| https://raw.githubusercontent.com/officialputuid/ProxyForEveryone/main/xResults/RAW.txt | active | 4/4 | 0 | 0.0 |
| https://raw.githubusercontent.com/shahidbhutta/Clash/main/Router | active | 4/4 | 0 | 0.0 |
| https://raw.githubusercontent.com/shahidbhutta/Clash/refs/heads/main/Router | active | 4/4 | 0 | 0.0 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/changfengoss.yaml | active | 4/4 | 0 | 0.0 |
| https://raw.githubusercontent.com/SnapdragonLee/SystemProxy/master/dist/clash_config.yaml | active | 4/4 | 0 | 0.0 |
| https://raw.githubusercontent.com/xiaoji235/airport-free/refs/heads/main/v2ray/naidounode.txt | active | 4/4 | 0 | 0.0 |
| https://free.datiya.com/uploads/{Ymd}-clash.yaml | active | 3/4 | 0 | 0.0 |
| https://free.datiya.com/uploads/{Ymd}-v2ray.txt | active | 3/4 | 0 | 0.0 |
| https://clashbest.github.io/uploads/{Y}/{mm}/0-{Ymd}.yaml | active | 1/4 | 0 | 0.0 |
| https://clashbest.github.io/uploads/{Y}/{mm}/1-{Ymd}.yaml | active | 1/4 | 0 | 0.0 |
| https://clashbest.github.io/uploads/{Y}/{mm}/3-{Ymd}.yaml | active | 1/4 | 0 | 0.0 |
| https://clashbest.github.io/uploads/{Y}/{mm}/4-{Ymd}.yaml | active | 1/4 | 0 | 0.0 |
| https://clashbest.github.io/uploads/{Y}/{mm}/{Ymd}.json | active | 1/4 | 0 | 0.0 |
| https://mihomoparty.github.io/uploads/{Y}/{mm}/0-{Ymd}.yaml | active | 1/4 | 0 | 0.0 |
| https://mihomoparty.github.io/uploads/{Y}/{mm}/1-{Ymd}.yaml | active | 1/4 | 0 | 0.0 |
| https://mihomoparty.github.io/uploads/{Y}/{mm}/4-{Ymd}.yaml | active | 1/4 | 0 | 0.0 |
| https://mihomoparty.github.io/uploads/{Y}/{mm}/{Ymd}.json | active | 1/4 | 0 | 0.0 |
| https://link.rittbo.kdns.fr/sub?token=8794e5157120a9982b0ceed9dcef5de7 | 冷却至 08-23 | 0/4 | 0 | 0.0 |
| https://raw.githubusercontent.com/free-nodes/v2rayfree/main/v{ymd}1 | 冷却至 08-23 | 0/4 | 0 | 0.0 |
| https://raw.githubusercontent.com/free-nodes/v2rayfree/main/v{ymd}2 | 冷却至 08-23 | 0/4 | 0 | 0.0 |
| https://raw.githubusercontent.com/lagzian/SS-Collector/main/SS/trinity_clash.yaml | 冷却至 08-23 | 0/4 | 0 | 0.0 |
| https://raw.githubusercontent.com/lagzian/SS-Collector/main/SS/TrinityBase | 冷却至 08-23 | 0/4 | 0 | 0.0 |
| https://raw.githubusercontent.com/lagzian/SS-Collector/main/SS/VM_TrinityBase | 冷却至 08-23 | 0/4 | 0 | 0.0 |
| https://raw.githubusercontent.com/MrMohebi/xray-proxy-grabber-telegram/master/collected-proxies/clash-meta/all.yaml | 冷却至 08-23 | 0/4 | 0 | 0.0 |
| https://raw.githubusercontent.com/yorkLiu/FreeV2RayNode/main/v2ray.txt | 冷却至 08-23 | 0/4 | 0 | 0.0 |

## 聚合源（按近 N 次平均拉取数降序）
| id | link | success_rate | last | avg |
|---|---|---|---|---|
| sinspired_scan | https://raw.githubusercontent.com/sinspired/airport/main/subs/merged/scan.txt | 4/4 | 20 | 19.5 |
| sinspired_col | https://raw.githubusercontent.com/sinspired/airport/main/subs/merged/col.txt | 4/4 | 17 | 17.0 |
| sinspired_cm | https://raw.githubusercontent.com/sinspired/airport/main/subs/merged/cm.txt | 4/4 | 12 | 12.0 |
