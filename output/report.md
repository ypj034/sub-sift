# sub-sift 运行报告

- 运行时间: 2026-08-22 09:25:37 CST
- 主清单订阅链接数: 177
- 本次实际拉取: 153（冷却/禁用跳过: 24）
- 拉取成功: 151，失败: 2
- 有效节点数（筛选后去重前）: 45548
- 输出节点数（去重后）: 11718
- GeoIP 数据源: mmdb: data/GeoLite2-Country.mmdb
- 输出文件: output/v2ray.txt, output/plain.txt

## 主清单（active → 冷却 → disabled；组内按 avg 降序）
| 链接 | 状态 | 成功率 | 有效率 | 重复率 | 平均 | 最近 | 无效 | 非加密 | 排除协议 | 排除地区 | 排除合计 |
| --- | :---: | :---: | :---: | :---: | --- | --- | --- | --- | --- | --- |
| https://raw.githubusercontent.com/ebrasha/free-v2ray-public-list/refs/heads/main/all_extracted_configs.txt | active | 14/14 | 22.2% | 91.2% | 10131.7 | 10236 | 2944 | 14619 | 6711 | 11621 | 35895 |
| https://raw.githubusercontent.com/mheidari98/.proxy/main/all | active | 14/14 | 30.9% | 99.0% | 6068.4 | 6621 | 486 | 5239 | 3730 | 5334 | 14789 |
| https://raw.githubusercontent.com/DukeMehdi/FreeList-V2ray-Configs/refs/heads/main/Configs/VLESS-DukeMehdi-Configs.txt | active | 13/14 | - | - | 6057.2 | 0 | 0 | 0 | 0 | 0 | 0 |
| https://raw.githubusercontent.com/DukeMehdi/FreeList-V2ray-Configs/refs/heads/main/Configs/TROJAN-DukeMehdi-Configs.txt | active | 14/14 | 55.9% | 82.6% | 3755.7 | 3830 | 75 | 833 | 0 | 2118 | 3026 |
| https://raw.githubusercontent.com/sakha1370/OpenRay/main/output/all_valid_proxies.txt | active | 14/14 | 27.4% | 100.0% | 3083.5 | 3114 | 850 | 3544 | 343 | 3511 | 8248 |
| https://raw.githubusercontent.com/sevcator/5ubscrpt10n/main/mini/m1n1-5ub-14.txt | active | 14/14 | 23.3% | 93.1% | 2260.0 | 2260 | 326 | 3635 | 0 | 3459 | 7420 |
| https://raw.githubusercontent.com/xiaoji235/airport-free/main/v2ray.txt | active | 14/14 | 36.3% | 100.0% | 2143.0 | 2143 | 193 | 1253 | 912 | 1397 | 3755 |
| https://raw.githubusercontent.com/xiaoji235/airport-free/refs/heads/main/v2ray/clashnodecc.txt | active | 14/14 | 36.4% | 100.0% | 2141.0 | 2141 | 193 | 1243 | 912 | 1395 | 3743 |
| https://raw.githubusercontent.com/sevcator/5ubscrpt10n/main/mini/m1n1-5ub-19.txt | active | 14/14 | 20.4% | 77.5% | 1939.0 | 1939 | 397 | 2856 | 0 | 4331 | 7584 |
| https://raw.githubusercontent.com/liMilCo/v2r/main/configs.txt | active | 14/14 | 27.3% | 94.5% | 1651.5 | 1845 | 343 | 2385 | 797 | 1392 | 4917 |
| https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/main/all_configs.txt | active | 14/14 | 22.7% | 100.0% | 1562.6 | 1571 | 331 | 2254 | 692 | 2067 | 5344 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/soroushmirzaei.yaml | active | 14/14 | 3.4% | 97.7% | 1443.0 | 1443 | 198 | 25699 | 1948 | 12953 | 40798 |
| https://raw.githubusercontent.com/Leon406/SubCrawler/master/sub/share/vless | active | 14/14 | 24.0% | 69.6% | 1115.6 | 1224 | 156 | 1266 | 0 | 2459 | 3881 |
| https://clashgithub.com/wp-content/uploads/rss/{Ymd}.txt | active | 14/14 | 38.9% | 99.2% | 620.9 | 635 | 150 | 339 | 359 | 150 | 998 |
| https://github.com/Au1rxx/free-vpn-subscriptions/raw/main/output/by-country/v2ray-base64-JP.txt | active | 14/14 | 65.4% | 94.3% | 463.8 | 666 | 0 | 338 | 11 | 4 | 353 |
| https://raw.githubusercontent.com/asgharkapk/Sub-Config-Extractor/main/output_configs/mixed/Leon406/SubCrawler/sub/share/a11.yaml | active | 14/14 | 65.4% | 99.3% | 455.6 | 426 | 0 | 81 | 71 | 73 | 225 |
| https://raw.githubusercontent.com/anaer/Sub/main/clash.yaml | active | 14/14 | 36.1% | 55.4% | 381.4 | 204 | 24 | 232 | 0 | 105 | 361 |
| https://raw.githubusercontent.com/free-nodes/clashfree/main/clash{Ymd}.yml | active | 14/14 | 36.1% | 100.0% | 374.1 | 582 | 148 | 386 | 347 | 147 | 1028 |
| https://raw.githubusercontent.com/mahdibland/SSAggregator/master/sub/sub_merge_yaml.yml | active | 14/14 | 8.1% | 100.0% | 346.2 | 328 | 9 | 1326 | 1829 | 558 | 3722 |
| https://raw.githubusercontent.com/mahdibland/V2RayAggregator/master/sub/sub_merge_yaml.yml | active | 14/14 | 8.1% | 100.0% | 346.2 | 328 | 9 | 1326 | 1829 | 558 | 3722 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/anaer.yaml | active | 14/14 | 15.9% | 12.0% | 342.0 | 342 | 61 | 923 | 0 | 831 | 1815 |
| https://node.freeclashnode.com/uploads/{Y}/{mm}/2-{Ymd}.yaml | active | 14/14 | 5.9% | 97.6% | 269.3 | 247 | 30 | 3082 | 245 | 571 | 3928 |
| https://raw.githubusercontent.com/NiceVPN123/NiceVPN/main/Clash.yaml | active | 14/14 | 6.2% | 16.0% | 225.0 | 225 | 10 | 1963 | 1177 | 268 | 3418 |
| https://raw.githubusercontent.com/NiceVPN123/NiceVPN/main/utils/pool/output.yaml | active | 13/14 | - | - | 209.9 | 0 | 0 | 0 | 0 | 0 | 0 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/coldwater-10.yaml | active | 14/14 | 11.3% | 8.0% | 199.0 | 199 | 2 | 458 | 0 | 1101 | 1561 |
| https://raw.githubusercontent.com/Q3dlaXpoaQ/V2rayN_Clash_Node_Getter/main/APIs/sc2.yaml | active | 14/14 | 5.0% | 100.0% | 181.0 | 181 | 35 | 2833 | 209 | 398 | 3475 |
| https://raw.githubusercontent.com/Q3dlaXpoaQ/V2rayN_Clash_Node_Getter/refs/heads/main/APIs/sc2.yaml | active | 14/14 | 5.0% | 100.0% | 181.0 | 181 | 35 | 2833 | 209 | 398 | 3475 |
| https://raw.githubusercontent.com/liMilCo/v2r/main/base64/2.txt | active | 14/14 | 41.4% | 100.0% | 167.5 | 190 | 16 | 114 | 41 | 98 | 269 |
| https://github.com/Au1rxx/free-vpn-subscriptions/raw/main/output/by-country/v2ray-base64-SG.txt | active | 14/14 | 63.0% | 96.6% | 153.2 | 87 | 0 | 31 | 15 | 5 | 51 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/trial.yaml | active | 14/14 | 19.7% | 30.9% | 149.0 | 149 | 6 | 157 | 289 | 155 | 607 |
| https://raw.githubusercontent.com/ALIILAPRO/v2rayNG-Config/main/sub.txt | active | 14/14 | 17.7% | 100.0% | 143.4 | 175 | 64 | 522 | 0 | 226 | 812 |
| https://raw.githubusercontent.com/barry-far/V2ray-config/main/Sub2.txt | active | 14/14 | 29.8% | 100.0% | 133.6 | 141 | 10 | 38 | 122 | 162 | 332 |
| https://github.com/Au1rxx/free-vpn-subscriptions/raw/main/output/by-country/v2ray-base64-US.txt | active | 14/14 | 60.4% | 87.4% | 132.1 | 183 | 0 | 34 | 36 | 50 | 120 |
| https://raw.githubusercontent.com/MhdiTaheri/V2rayCollector/main/sub/mix | active | 14/14 | 14.9% | 100.0% | 129.9 | 144 | 9 | 542 | 115 | 155 | 821 |
| https://raw.githubusercontent.com/F0rc3Run/F0rc3Run/refs/heads/main/splitted-by-protocol/trojan.txt | active | 14/14 | 72.1% | 100.0% | 128.4 | 88 | 0 | 0 | 0 | 34 | 34 |
| https://github.com/Au1rxx/free-vpn-subscriptions/raw/main/output/by-country/v2ray-base64-HK.txt | active | 14/14 | 72.8% | 98.6% | 113.6 | 139 | 0 | 24 | 17 | 11 | 52 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/_previous.yaml | active | 14/14 | 20.4% | 25.7% | 105.0 | 105 | 3 | 53 | 188 | 166 | 410 |
| https://github.com/crackbest/V2ray-Config/raw/refs/heads/main/config.txt | active | 14/14 | 17.8% | 100.0% | 78.0 | 87 | 12 | 148 | 68 | 175 | 403 |
| https://raw.githubusercontent.com/crackbest/V2ray-Config/refs/heads/main/config.txt | active | 14/14 | 17.8% | 100.0% | 78.0 | 87 | 12 | 148 | 68 | 175 | 403 |
| https://raw.githubusercontent.com/xtoolkit/TVC/main/subscriptions/meta/mix | active | 14/14 | 22.4% | 81.5% | 73.4 | 81 | 15 | 127 | 1 | 138 | 281 |
| https://raw.githubusercontent.com/ts-sf/fly/main/clash | active | 14/14 | 36.5% | 37.0% | 72.4 | 73 | 10 | 52 | 0 | 65 | 127 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/clashfree.yaml | active | 14/14 | 10.1% | 64.3% | 56.0 | 56 | 31 | 210 | 237 | 20 | 498 |
| https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/main/Base64/BLACK_VLESS_RUS_mobile_base64.txt | active | 14/14 | 31.8% | 100.0% | 54.4 | 47 | 1 | 4 | 24 | 72 | 101 |
| https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/main/BLACK_VLESS_RUS_mobile.txt | active | 14/14 | 31.8% | 100.0% | 54.4 | 47 | 1 | 4 | 24 | 72 | 101 |
| https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/main/Base64/BLACK_VLESS_RUS_base64.txt | active | 14/14 | 33.3% | 100.0% | 51.9 | 45 | 0 | 20 | 0 | 70 | 90 |
| https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/main/BLACK_VLESS_RUS.txt | active | 14/14 | 33.3% | 100.0% | 51.9 | 45 | 0 | 20 | 0 | 70 | 90 |
| https://raw.githubusercontent.com/F0rc3Run/F0rc3Run/refs/heads/main/splitted-by-protocol/vless.txt | active | 14/14 | 26.6% | 100.0% | 46.8 | 67 | 4 | 68 | 0 | 113 | 185 |
| https://raw.githubusercontent.com/hans-thomas/v2ray-subscription/refs/heads/master/servers.txt | active | 14/14 | 34.8% | 97.8% | 46.0 | 46 | 1 | 4 | 7 | 74 | 86 |
| https://raw.githubusercontent.com/Arefgh72/v2ray-proxy-pars-tester/main/output/github_all.txt | active | 14/14 | 1.6% | 97.8% | 46.0 | 46 | 4 | 793 | 1962 | 17 | 2776 |
| https://raw.githubusercontent.com/ts-sf/fly/main/v2 | active | 14/14 | 16.4% | 100.0% | 44.9 | 33 | 11 | 100 | 0 | 57 | 168 |
| https://raw.githubusercontent.com/acymz/AutoVPN/main/data/V2.txt | active | 14/14 | 13.3% | 100.0% | 31.6 | 28 | 10 | 30 | 92 | 51 | 183 |
| https://raw.githubusercontent.com/Barabama/FreeNodes/main/nodes/blues.txt | active | 14/14 | 19.3% | 30.8% | 26.0 | 26 | 3 | 83 | 1 | 22 | 109 |
| https://raw.githubusercontent.com/LoneKingCode/free-proxy-db/main/proxies/all.txt | active | 14/14 | 7.0% | 63.0% | 25.7 | 27 | 1 | 183 | 105 | 68 | 357 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/snakem982.yaml | active | 14/14 | 36.9% | 100.0% | 24.0 | 24 | 1 | 6 | 22 | 12 | 41 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/zhangkaiitugithub.yaml | active | 14/14 | 36.9% | 100.0% | 24.0 | 24 | 1 | 6 | 22 | 12 | 41 |
| https://raw.githubusercontent.com/Ruk1ng001/freeSub/main/clash.yaml | active | 14/14 | 9.5% | 93.8% | 18.6 | 16 | 0 | 36 | 103 | 13 | 152 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/yudou.yaml | active | 14/14 | 25.8% | 88.2% | 17.0 | 17 | 0 | 36 | 5 | 8 | 49 |
| https://github.com/Au1rxx/free-vpn-subscriptions/raw/main/output/by-country/v2ray-base64-KR.txt | active | 14/14 | 51.6% | 100.0% | 16.0 | 16 | 0 | 4 | 11 | 0 | 15 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/tssf.yaml | active | 14/14 | 19.8% | 43.8% | 16.0 | 16 | 7 | 39 | 14 | 5 | 65 |
| https://raw.githubusercontent.com/PangTouY00/Auto_proxy/main/Long_term_subscription_num | active | 14/14 | 8.1% | 100.0% | 15.0 | 13 | 0 | 18 | 89 | 41 | 148 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/aiboboxx.yaml | active | 14/14 | 2.1% | 26.7% | 15.0 | 15 | 19 | 635 | 24 | 23 | 701 |
| https://raw.githubusercontent.com/Surfboardv2ray/v2ray-worker-sub/refs/heads/master/Eternity.txt | active | 14/14 | 7.5% | 20.0% | 15.0 | 15 | 0 | 4 | 152 | 29 | 185 |
| https://raw.githubusercontent.com/ovmvo/SubShare/main/sub/permanent/mihomo.yaml | active | 14/14 | 27.5% | 71.4% | 14.0 | 14 | 8 | 6 | 9 | 14 | 37 |
| https://www.xrayvip.com/free.txt | active | 14/14 | 23.9% | 100.0% | 12.9 | 11 | 1 | 14 | 1 | 19 | 35 |
| https://raw.githubusercontent.com/snakem982/proxypool/main/source/clash-meta-2.yaml | active | 14/14 | 11.0% | 100.0% | 12.9 | 11 | 2 | 39 | 36 | 12 | 89 |
| https://raw.githubusercontent.com/peasoft/NoMoreWalls/master/list.meta.yml | active | 14/14 | 5.1% | 100.0% | 12.8 | 7 | 11 | 33 | 83 | 3 | 130 |
| https://raw.githubusercontent.com/peasoft/NoMoreWalls/master/snippets/nodes.meta.yml | active | 14/14 | 5.1% | 100.0% | 12.8 | 7 | 11 | 33 | 83 | 3 | 130 |
| https://raw.githubusercontent.com/MatinGhanbari/v2ray-configs/main/subscriptions/v2ray/subs/sub2.txt | active | 14/14 | 8.7% | 16.7% | 12.0 | 12 | 0 | 108 | 17 | 1 | 126 |
| https://raw.githubusercontent.com/ggborr/FREEE-VPN/main/3v2 | active | 14/14 | 56.2% | 77.8% | 9.0 | 9 | 0 | 5 | 1 | 1 | 7 |
| https://raw.githubusercontent.com/mgit0001/test_clash/main/heima.txt | active | 14/14 | 32.0% | 100.0% | 8.0 | 8 | 0 | 6 | 11 | 0 | 17 |
| https://raw.githubusercontent.com/mgit0001/test_clash/refs/heads/main/heima.txt | active | 14/14 | 32.0% | 100.0% | 8.0 | 8 | 0 | 6 | 11 | 0 | 17 |
| https://raw.githubusercontent.com/HakurouKen/free-node/main/public | active | 14/14 | 7.1% | 100.0% | 7.9 | 1 | 0 | 3 | 10 | 0 | 13 |
| https://raw.githubusercontent.com/Barabama/FreeNodes/main/nodes/ndnode.txt | active | 14/14 | 50.0% | 0.0% | 7.0 | 7 | 0 | 6 | 1 | 0 | 7 |
| https://raw.githubusercontent.com/vxiaov/free_proxies/main/clash/clash.provider.yaml | active | 14/14 | 26.9% | 100.0% | 7.0 | 7 | 0 | 8 | 11 | 0 | 19 |
| https://raw.githubusercontent.com/zhangkaiitugithub/passcro/main/speednodes.yaml | active | 14/14 | 58.3% | 100.0% | 7.0 | 7 | 0 | 1 | 3 | 1 | 5 |
| https://raw.githubusercontent.com/justVisiting992/xray-Config-Collector/main/clash.yaml | active | 14/14 | 0.8% | 55.6% | 6.1 | 9 | 22 | 529 | 402 | 148 | 1101 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/_pool.yaml | active | 14/14 | 2.6% | 0.0% | 6.0 | 6 | 0 | 141 | 73 | 8 | 222 |
| https://raw.githubusercontent.com/actionsfz/v2ray/master/all.yaml | active | 14/14 | 7.1% | 100.0% | 6.0 | 6 | 0 | 40 | 8 | 31 | 79 |
| https://raw.githubusercontent.com/actionsfz/v2ray/refs/heads/master/all.yaml | active | 14/14 | 7.1% | 100.0% | 6.0 | 6 | 0 | 40 | 8 | 31 | 79 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/xrayvip.yaml | active | 14/14 | 25.0% | 50.0% | 6.0 | 6 | 0 | 4 | 3 | 11 | 18 |
| https://raw.githubusercontent.com/free18/v2ray/main/c.yaml | active | 14/14 | 0.3% | 100.0% | 5.6 | 2 | 22 | 697 | 0 | 2 | 721 |
| https://raw.githubusercontent.com/Shjpr9/Subs/refs/heads/main/sub.txt | active | 14/14 | 3.5% | 40.0% | 5.0 | 5 | 15 | 90 | 0 | 34 | 139 |
| https://raw.githubusercontent.com/peacefish/nodefree/main/sub/proxy_cf.yaml | active | 14/14 | 16.2% | 100.0% | 5.0 | 11 | 1 | 32 | 9 | 15 | 57 |
| https://raw.githubusercontent.com/Pawdroid/Free-servers/main/sub | active | 14/14 | 10.0% | 100.0% | 4.9 | 2 | 0 | 4 | 2 | 12 | 18 |
| https://raw.githubusercontent.com/Pawdroid/Free-servers/refs/heads/main/sub | active | 14/14 | 10.0% | 100.0% | 4.8 | 2 | 0 | 4 | 2 | 12 | 18 |
| https://raw.githubusercontent.com/Delta-Kronecker/V2ray-Config/main/config/clash.yaml | active | 14/14 | 0.0% | - | 4.3 | 0 | 39 | 3766 | 588 | 0 | 4393 |
| https://raw.githubusercontent.com/shaoyouvip/free/refs/heads/main/all.yaml | active | 14/14 | 0.0% | - | 4.2 | 0 | 1 | 6 | 4 | 2 | 13 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/ttvg.yaml | active | 14/14 | 22.2% | 75.0% | 4.0 | 4 | 0 | 4 | 1 | 9 | 14 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/hkaa0.yaml | active | 14/14 | 0.1% | 100.0% | 4.0 | 4 | 0 | 6144 | 10 | 0 | 6154 |
| https://raw.githubusercontent.com/F0rc3Run/F0rc3Run/refs/heads/main/splitted-by-protocol/vmess.txt | active | 14/14 | 5.6% | 100.0% | 3.7 | 3 | 0 | 50 | 0 | 1 | 51 |
| https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/main/Base64/BLACK_SS+All_RUS_base64.txt | active | 14/14 | 2.9% | 100.0% | 3.4 | 2 | 1 | 6 | 55 | 5 | 67 |
| https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/main/BLACK_SS+All_RUS.txt | active | 14/14 | 2.9% | 100.0% | 3.4 | 2 | 1 | 6 | 55 | 5 | 67 |
| https://raw.githubusercontent.com/mahdibland/ShadowsocksAggregator/master/Eternity.yml | active | 14/14 | 1.0% | 100.0% | 3.3 | 2 | 0 | 136 | 62 | 1 | 199 |
| https://raw.githubusercontent.com/firefoxmmx2/v2rayshare_subcription/main/subscription/clash_sub.yaml | active | 14/14 | 36.7% | 100.0% | 3.1 | 11 | 0 | 2 | 9 | 8 | 19 |
| https://raw.githubusercontent.com/Barabama/FreeNodes/main/nodes/nodefree.txt | active | 14/14 | 13.0% | 100.0% | 3.0 | 3 | 0 | 3 | 10 | 7 | 20 |
| https://raw.githubusercontent.com/mfbpn/tg_mfbpn_sub/main/trial.yaml | active | 14/14 | 2.5% | 100.0% | 3.0 | 3 | 0 | 114 | 0 | 1 | 115 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/mahdibland.yaml | active | 14/14 | 1.5% | 33.3% | 3.0 | 3 | 0 | 35 | 159 | 2 | 196 |
| https://raw.githubusercontent.com/Barabama/FreeNodes/main/nodes/v2rayshare.txt | active | 14/14 | 13.0% | 100.0% | 3.0 | 3 | 0 | 3 | 10 | 7 | 20 |
| https://raw.githubusercontent.com/Barabama/FreeNodes/main/nodes/wenode.txt | active | 14/14 | 13.0% | 100.0% | 3.0 | 3 | 0 | 3 | 10 | 7 | 20 |
| https://raw.githubusercontent.com/Barabama/FreeNodes/main/nodes/yudou66.txt | active | 14/14 | 1.8% | 100.0% | 3.0 | 3 | 0 | 142 | 10 | 9 | 161 |
| https://raw.githubusercontent.com/Barabama/FreeNodes/main/nodes/yudou66.yaml | active | 14/14 | 1.8% | 100.0% | 3.0 | 3 | 0 | 141 | 10 | 9 | 160 |
| https://github.com/Au1rxx/free-vpn-subscriptions/raw/main/output/by-country/v2ray-base64-TW.txt | active | 14/14 | 13.8% | 100.0% | 2.1 | 4 | 0 | 11 | 8 | 6 | 25 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/SFZY666.yaml | active | 14/14 | 16.7% | 0.0% | 2.0 | 2 | 1 | 9 | 0 | 0 | 10 |
| https://raw.githubusercontent.com/xiaoji235/airport-free/refs/heads/main/v2ray/v2rayshare.txt | active | 14/14 | 14.3% | 100.0% | 2.0 | 2 | 0 | 10 | 0 | 2 | 12 |
| https://raw.githubusercontent.com/hello-world-1989/cn-news/main/end-gfw-together | active | 14/14 | 100.0% | 100.0% | 2.0 | 2 | 0 | 0 | 0 | 0 | 0 |
| https://raw.githubusercontent.com/peasoft/NoMoreWalls/master/list.yml | active | 14/14 | 0.0% | - | 1.6 | 0 | 10 | 30 | 2 | 0 | 42 |
| https://node.freeclashnode.com/uploads/{Y}/{mm}/3-{Ymd}.yaml | active | 14/14 | 36.7% | 100.0% | 1.6 | 11 | 0 | 2 | 9 | 8 | 19 |
| https://raw.githubusercontent.com/Misaka-blog/chromego_merge/main/sub/merged_proxies_new.yaml | active | 14/14 | 0.0% | - | 1.2 | 0 | 10 | 32 | 3 | 0 | 45 |
| https://raw.githubusercontent.com/Barabama/FreeNodes/main/nodes/clashmeta.txt | active | 14/14 | 8.3% | 0.0% | 1.0 | 1 | 0 | 4 | 2 | 5 | 11 |
| https://raw.githubusercontent.com/vxiaov/free_proxies/main/links.txt | active | 14/14 | 14.3% | 100.0% | 1.0 | 1 | 0 | 1 | 5 | 0 | 6 |
| https://raw.githubusercontent.com/ermaozi/get_subscribe/main/subscribe/clash.yml | active | 14/14 | 5.0% | 100.0% | 0.4 | 1 | 0 | 13 | 6 | 0 | 19 |
| https://www.ermao.net/sub/clash/ermao.net | active | 14/14 | 5.0% | 100.0% | 0.2 | 1 | 0 | 13 | 6 | 0 | 19 |
| https://raw.githubusercontent.com/go4sharing/sub/main/sub.yaml | active | 14/14 | 2.9% | 100.0% | 0.1 | 1 | 1 | 2 | 30 | 0 | 33 |
| https://raw.githubusercontent.com/DukeMehdi/FreeList-V2ray-Configs/refs/heads/main/Configs/VMESS-DukeMehdi-Configs.txt | active | 14/14 | - | - | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 |
| https://github.com/AzadNetCH/Clash/raw/refs/heads/main/AzadNet.txt | active | 14/14 | 0.0% | - | 0.0 | 0 | 0 | 1 | 16 | 0 | 17 |
| https://raw.githubusercontent.com/aiboboxx/v2rayfree/main/README.md | active | 14/14 | 0.0% | - | 0.0 | 0 | 0 | 0 | 20 | 0 | 20 |
| https://raw.githubusercontent.com/aiboboxx/v2rayfree/refs/heads/main/README.md | active | 14/14 | 0.0% | - | 0.0 | 0 | 0 | 0 | 20 | 0 | 20 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/refs/heads/main/V2RAY.txt | active | 14/14 | - | - | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 |
| https://node.freeclashnode.com/uploads/{Y}/{mm}/0-{Ymd}.yaml | active | 14/14 | 0.0% | - | 0.0 | 0 | 4 | 218 | 14 | 2 | 238 |
| https://raw.githubusercontent.com/Q3dlaXpoaQ/V2rayN_Clash_Node_Getter/main/APIs/sc0.yaml | active | 14/14 | 0.0% | - | 0.0 | 0 | 4 | 220 | 15 | 2 | 241 |
| https://raw.githubusercontent.com/Q3dlaXpoaQ/V2rayN_Clash_Node_Getter/refs/heads/main/APIs/sc0.yaml | active | 14/14 | 0.0% | - | 0.0 | 0 | 4 | 220 | 15 | 2 | 241 |
| https://node.freeclashnode.com/uploads/{Y}/{mm}/1-{Ymd}.yaml | active | 14/14 | 0.0% | - | 0.0 | 0 | 3 | 259 | 6 | 2 | 270 |
| https://raw.githubusercontent.com/Q3dlaXpoaQ/V2rayN_Clash_Node_Getter/main/APIs/sc1.yaml | active | 14/14 | 0.0% | - | 0.0 | 0 | 1 | 261 | 1 | 2 | 265 |
| https://raw.githubusercontent.com/Q3dlaXpoaQ/V2rayN_Clash_Node_Getter/refs/heads/main/APIs/sc1.yaml | active | 14/14 | 0.0% | - | 0.0 | 0 | 1 | 261 | 1 | 2 | 265 |
| https://raw.githubusercontent.com/chengaopan/AutoMergePublicNodes/master/list.yml | active | 14/14 | 0.0% | - | 0.0 | 0 | 0 | 14 | 1 | 0 | 15 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/chengaopan.yaml | active | 14/14 | 0.0% | - | 0.0 | 0 | 0 | 15 | 1 | 0 | 16 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/peasoft.yaml | active | 14/14 | 0.0% | - | 0.0 | 0 | 10 | 15 | 1 | 0 | 26 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/ripaojiedian.yaml | active | 14/14 | 0.0% | - | 0.0 | 0 | 0 | 13 | 1 | 0 | 14 |
| https://raw.githubusercontent.com/ripaojiedian/freenode/main/clash | active | 14/14 | 0.0% | - | 0.0 | 0 | 0 | 13 | 1 | 0 | 14 |
| https://raw.githubusercontent.com/Barabama/FreeNodes/main/nodes/clashmeta.yaml | active | 14/14 | 0.0% | - | 0.0 | 0 | 0 | 89 | 0 | 0 | 89 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/blue-Youtube.yaml | active | 14/14 | 0.0% | - | 0.0 | 0 | 1 | 46 | 0 | 0 | 47 |
| https://raw.githubusercontent.com/Q3dlaXpoaQ/V2rayN_Clash_Node_Getter/main/APIs/sc3.yaml | active | 14/14 | 0.0% | - | 0.0 | 0 | 0 | 14 | 0 | 0 | 14 |
| https://raw.githubusercontent.com/Q3dlaXpoaQ/V2rayN_Clash_Node_Getter/refs/heads/main/APIs/sc3.yaml | active | 14/14 | 0.0% | - | 0.0 | 0 | 0 | 14 | 0 | 0 | 14 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/ermaozi.yaml | active | 14/14 | 0.0% | - | 0.0 | 0 | 0 | 16 | 3 | 2 | 21 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/Pawdroid.yaml | active | 14/14 | 0.0% | - | 0.0 | 0 | 0 | 5 | 2 | 1 | 8 |
| https://node.freeclashnode.com/uploads/{Y}/{mm}/4-{Ymd}.yaml | active | 14/14 | - | - | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 |
| https://github.com/mermeroo/V2RAY-CLASH-BASE64-Subscription.Links/raw/refs/heads/main/SUB%20LINKS | active | 14/14 | - | - | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 |
| https://raw.githubusercontent.com/andigwandi/free-proxy/main/proxy_list.txt | active | 14/14 | - | - | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 |
| https://raw.githubusercontent.com/asgharkapk/Sub-Config-Extractor/main/output_configs/clash/Ruk1ng001.yaml | active | 14/14 | - | - | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 |
| https://raw.githubusercontent.com/asgharkapk/Sub-Config-Extractor/main/output_configs/surfboard/Barabama_ndnode.yaml | active | 14/14 | - | - | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 |
| https://raw.githubusercontent.com/asgharkapk/Sub-Config-Extractor/main/output_configs/surfboard/Ruk1ng001.yaml | active | 14/14 | - | - | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 |
| https://raw.githubusercontent.com/Barabama/FreeNodes/main/nodes/nodev2ray.txt | active | 14/14 | 0.0% | - | 0.0 | 0 | 0 | 12 | 1 | 0 | 13 |
| https://raw.githubusercontent.com/dpangestuw/Free-Proxy/main/All_proxies.txt | active | 14/14 | - | - | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 |
| https://raw.githubusercontent.com/linzjian666/chromego_extractor/main/outputs/clash_meta.yaml | active | 14/14 | - | - | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 |
| https://raw.githubusercontent.com/officialputuid/ProxyForEveryone/main/xResults/old-data/RAW.txt | active | 14/14 | - | - | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 |
| https://raw.githubusercontent.com/officialputuid/ProxyForEveryone/main/xResults/RAW.txt | active | 14/14 | - | - | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 |
| https://raw.githubusercontent.com/shahidbhutta/Clash/main/Router | active | 14/14 | - | - | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 |
| https://raw.githubusercontent.com/shahidbhutta/Clash/refs/heads/main/Router | active | 14/14 | - | - | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/changfengoss.yaml | active | 14/14 | 0.0% | - | 0.0 | 0 | 1 | 1 | 1 | 0 | 3 |
| https://raw.githubusercontent.com/SnapdragonLee/SystemProxy/master/dist/clash_config.yaml | active | 14/14 | - | - | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 |
| https://raw.githubusercontent.com/xiaoji235/airport-free/refs/heads/main/v2ray/naidounode.txt | active | 14/14 | - | - | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 |
| https://free.datiya.com/uploads/{Ymd}-v2ray.txt | active | 12/14 | - | - | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 |
| https://free.datiya.com/uploads/{Ymd}-clash.yaml | active | 11/14 | 0.0% | - | 0.0 | 0 | 0 | 13 | 1 | 0 | 14 |
| https://mihomoparty.github.io/uploads/{Y}/{mm}/2-{Ymd}.txt | cd_0824 | 6/10 |  |  | 1068.0 | 0 |  |  |  |  |  |
| https://clashbest.github.io/uploads/{Y}/{mm}/2-{Ymd}.txt | cd_0824 | 6/10 |  |  | 1068.0 | 0 |  |  |  |  |  |
| https://mihomoparty.github.io/uploads/{Y}/{mm}/4-{Ymd}.txt | cd_0824 | 6/10 |  |  | 364.8 | 0 |  |  |  |  |  |
| https://clashbest.github.io/uploads/{Y}/{mm}/2-{Ymd}.yaml | cd_0824 | 6/10 |  |  | 164.4 | 0 |  |  |  |  |  |
| https://clashbest.github.io/uploads/{Y}/{mm}/1-{Ymd}.txt | cd_0824 | 6/10 |  |  | 34.8 | 0 |  |  |  |  |  |
| https://clashbest.github.io/uploads/{Y}/{mm}/0-{Ymd}.txt | cd_0824 | 6/10 |  |  | 29.4 | 0 |  |  |  |  |  |
| https://proxypool.link/trojan/sub | cd_0824 | 7/11 |  |  | 0.5 | 0 |  |  |  |  |  |
| https://clashbest.github.io/uploads/{Y}/{mm}/0-{Ymd}.yaml | cd_0824 | 6/10 |  |  | 0.0 | 0 |  |  |  |  |  |
| https://clashbest.github.io/uploads/{Y}/{mm}/1-{Ymd}.yaml | cd_0824 | 6/10 |  |  | 0.0 | 0 |  |  |  |  |  |
| https://clashbest.github.io/uploads/{Y}/{mm}/3-{Ymd}.yaml | cd_0824 | 6/10 |  |  | 0.0 | 0 |  |  |  |  |  |
| https://clashbest.github.io/uploads/{Y}/{mm}/4-{Ymd}.yaml | cd_0824 | 6/10 |  |  | 0.0 | 0 |  |  |  |  |  |
| https://clashbest.github.io/uploads/{Y}/{mm}/{Ymd}.json | cd_0824 | 6/10 |  |  | 0.0 | 0 |  |  |  |  |  |
| https://mihomoparty.github.io/uploads/{Y}/{mm}/0-{Ymd}.yaml | cd_0824 | 6/10 |  |  | 0.0 | 0 |  |  |  |  |  |
| https://mihomoparty.github.io/uploads/{Y}/{mm}/1-{Ymd}.yaml | cd_0824 | 6/10 |  |  | 0.0 | 0 |  |  |  |  |  |
| https://mihomoparty.github.io/uploads/{Y}/{mm}/4-{Ymd}.yaml | cd_0824 | 6/10 |  |  | 0.0 | 0 |  |  |  |  |  |
| https://mihomoparty.github.io/uploads/{Y}/{mm}/{Ymd}.json | cd_0824 | 6/10 |  |  | 0.0 | 0 |  |  |  |  |  |
| https://link.rittbo.kdns.fr/sub?token=8794e5157120a9982b0ceed9dcef5de7 | cd_0823 | 0/4 |  |  | 0.0 | 0 |  |  |  |  |  |
| https://raw.githubusercontent.com/free-nodes/v2rayfree/main/v{ymd}1 | cd_0823 | 0/4 |  |  | 0.0 | 0 |  |  |  |  |  |
| https://raw.githubusercontent.com/free-nodes/v2rayfree/main/v{ymd}2 | cd_0823 | 0/4 |  |  | 0.0 | 0 |  |  |  |  |  |
| https://raw.githubusercontent.com/lagzian/SS-Collector/main/SS/trinity_clash.yaml | cd_0823 | 0/4 |  |  | 0.0 | 0 |  |  |  |  |  |
| https://raw.githubusercontent.com/lagzian/SS-Collector/main/SS/TrinityBase | cd_0823 | 0/4 |  |  | 0.0 | 0 |  |  |  |  |  |
| https://raw.githubusercontent.com/lagzian/SS-Collector/main/SS/VM_TrinityBase | cd_0823 | 0/4 |  |  | 0.0 | 0 |  |  |  |  |  |
| https://raw.githubusercontent.com/MrMohebi/xray-proxy-grabber-telegram/master/collected-proxies/clash-meta/all.yaml | cd_0823 | 0/4 |  |  | 0.0 | 0 |  |  |  |  |  |
| https://raw.githubusercontent.com/yorkLiu/FreeV2RayNode/main/v2ray.txt | cd_0823 | 0/4 |  |  | 0.0 | 0 |  |  |  |  |  |

## 聚合源（按近 N 次平均拉取数降序）
| id | 链接 | 成功率 | 重复率 | 最近 | 平均 |
|---|---|:---:|:---:|---|---|
| sinspired_scan | https://raw.githubusercontent.com/sinspired/airport/main/subs/merged/scan.txt | 14/14 | 0.0% | 20 | 19.7 |
| sinspired_col | https://raw.githubusercontent.com/sinspired/airport/main/subs/merged/col.txt | 14/14 | 0.0% | 17 | 17.0 |
| sinspired_cm | https://raw.githubusercontent.com/sinspired/airport/main/subs/merged/cm.txt | 14/14 | 0.0% | 12 | 12.1 |
