# sub-sift 运行报告

- 运行时间: 2026-09-06 04:07:56 CST
- 主清单订阅链接数: 177
- 本次实际拉取: 154（冷却/禁用跳过: 23）
- 拉取成功: 151，失败: 3
- 有效节点数（筛选后去重前）: 44231
- 输出节点数（去重后）: 12347
- GeoIP 数据源: mmdb: data/GeoLite2-Country.mmdb
- 输出文件: output/v2ray.txt, output/plain.txt

## 主清单（active → 冷却 → disabled；组内按 avg 降序）
| 链接 | 状态 | 成功率 | 有效率 | 重复率 | 平均 | 最近 | 无效 | 非加密 | 排除协议 | 排除地区 | 排除合计 |
| --- | :---: | :---: | :---: | :---: | --- | --- | --- | --- | --- | --- | --- |
| https://raw.githubusercontent.com/ebrasha/free-v2ray-public-list/refs/heads/main/all_extracted_configs.txt | active | 29/30 | 28.7% | 97.8% | 7722.9 | 8235 | 2347 | 8332 | 5010 | 4814 | 20503 |
| https://raw.githubusercontent.com/DukeMehdi/FreeList-V2ray-Configs/refs/heads/main/Configs/VLESS-DukeMehdi-Configs.txt | active | 30/30 | 35.4% | 99.8% | 6359.4 | 6501 | 1735 | 6004 | 0 | 4105 | 11844 |
| https://raw.githubusercontent.com/sakha1370/OpenRay/main/output/all_valid_proxies.txt | active | 30/30 | 29.3% | 94.2% | 3660.2 | 3726 | 846 | 3762 | 384 | 4014 | 9006 |
| https://raw.githubusercontent.com/mheidari98/.proxy/main/all | active | 30/30 | 19.6% | 98.3% | 3004.8 | 4351 | 514 | 6978 | 4040 | 6309 | 17841 |
| https://raw.githubusercontent.com/sevcator/5ubscrpt10n/main/mini/m1n1-5ub-14.txt | active | 30/30 | 23.3% | 81.2% | 2259.8 | 2260 | 326 | 3635 | 0 | 3459 | 7420 |
| https://raw.githubusercontent.com/sevcator/5ubscrpt10n/main/mini/m1n1-5ub-19.txt | active | 30/30 | 20.4% | 77.1% | 1939.0 | 1939 | 397 | 2856 | 0 | 4331 | 7584 |
| https://raw.githubusercontent.com/Leon406/SubCrawler/master/sub/share/vless | active | 30/30 | 23.5% | 52.5% | 1882.8 | 2085 | 236 | 2256 | 0 | 4287 | 6779 |
| https://raw.githubusercontent.com/DukeMehdi/FreeList-V2ray-Configs/refs/heads/main/Configs/TROJAN-DukeMehdi-Configs.txt | active | 30/30 | 56.0% | 64.6% | 1587.0 | 1593 | 79 | 304 | 0 | 871 | 1254 |
| https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/main/all_configs.txt | active | 30/30 | 20.2% | 100.0% | 1531.1 | 1615 | 349 | 2790 | 789 | 2448 | 6376 |
| https://raw.githubusercontent.com/liMilCo/v2r/main/configs.txt | active | 29/30 | 19.5% | 93.6% | 1404.3 | 1556 | 438 | 3558 | 873 | 1573 | 6442 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/soroushmirzaei.yaml | active | 29/30 | 3.4% | 97.6% | 1395.4 | 1445 | 198 | 25699 | 1948 | 12951 | 40796 |
| https://raw.githubusercontent.com/xiaoji235/airport-free/main/v2ray.txt | active | 30/30 | 19.9% | 100.0% | 831.9 | 1382 | 186 | 2038 | 1177 | 2149 | 5550 |
| https://raw.githubusercontent.com/xiaoji235/airport-free/refs/heads/main/v2ray/clashnodecc.txt | active | 30/30 | 20.0% | 100.0% | 825.4 | 1380 | 186 | 2030 | 1168 | 2145 | 5529 |
| https://clashgithub.com/wp-content/uploads/rss/{Ymd}.txt | active | 24/30 | 32.9% | 100.0% | 399.0 | 507 | 127 | 280 | 516 | 111 | 1034 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/anaer.yaml | active | 29/30 | 15.9% | 11.7% | 331.0 | 343 | 61 | 923 | 0 | 830 | 1814 |
| https://raw.githubusercontent.com/mahdibland/SSAggregator/master/sub/sub_merge_yaml.yml | active | 30/30 | 8.3% | 100.0% | 325.6 | 338 | 4 | 1333 | 1842 | 552 | 3731 |
| https://raw.githubusercontent.com/mahdibland/V2RayAggregator/master/sub/sub_merge_yaml.yml | active | 30/30 | 8.3% | 100.0% | 325.6 | 338 | 4 | 1333 | 1842 | 552 | 3731 |
| https://raw.githubusercontent.com/ALIILAPRO/v2rayNG-Config/main/sub.txt | active | 30/30 | 18.6% | 100.0% | 269.0 | 327 | 109 | 1003 | 0 | 318 | 1430 |
| https://raw.githubusercontent.com/free-nodes/clashfree/main/clash{Ymd}.yml | active | 24/30 | 33.2% | 100.0% | 250.6 | 508 | 125 | 283 | 511 | 105 | 1024 |
| https://raw.githubusercontent.com/NiceVPN123/NiceVPN/main/utils/pool/output.yaml | active | 30/30 | 6.1% | 100.0% | 226.0 | 226 | 10 | 2034 | 1189 | 268 | 3501 |
| https://raw.githubusercontent.com/NiceVPN123/NiceVPN/main/Clash.yaml | active | 30/30 | 6.2% | 100.0% | 225.0 | 225 | 10 | 1963 | 1177 | 268 | 3418 |
| https://github.com/Au1rxx/free-vpn-subscriptions/raw/main/output/by-country/v2ray-base64-US.txt | active | 30/30 | 32.3% | 96.0% | 220.2 | 151 | 0 | 181 | 30 | 105 | 316 |
| https://github.com/Au1rxx/free-vpn-subscriptions/raw/main/output/by-country/v2ray-base64-JP.txt | active | 30/30 | 52.8% | 97.5% | 215.7 | 200 | 0 | 162 | 13 | 4 | 179 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/coldwater-10.yaml | active | 30/30 | 11.6% | 7.3% | 200.4 | 205 | 2 | 458 | 0 | 1095 | 1555 |
| https://github.com/Au1rxx/free-vpn-subscriptions/raw/main/output/by-country/v2ray-base64-SG.txt | active | 30/30 | 79.4% | 100.0% | 197.4 | 204 | 0 | 30 | 23 | 0 | 53 |
| https://raw.githubusercontent.com/anaer/Sub/main/clash.yaml | active | 30/30 | 19.3% | 96.3% | 196.7 | 273 | 39 | 308 | 0 | 792 | 1139 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/trial.yaml | active | 30/30 | 20.0% | 30.5% | 149.8 | 151 | 6 | 157 | 289 | 153 | 605 |
| https://raw.githubusercontent.com/MhdiTaheri/V2rayCollector/main/sub/mix | active | 30/30 | 14.2% | 100.0% | 146.1 | 162 | 10 | 591 | 144 | 231 | 976 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/_previous.yaml | active | 30/30 | 20.4% | 25.7% | 105.0 | 105 | 3 | 53 | 188 | 166 | 410 |
| https://raw.githubusercontent.com/Q3dlaXpoaQ/V2rayN_Clash_Node_Getter/main/APIs/sc2.yaml | active | 30/30 | 0.0% | - | 104.0 | 0 | 1 | 220 | 0 | 0 | 221 |
| https://raw.githubusercontent.com/Q3dlaXpoaQ/V2rayN_Clash_Node_Getter/refs/heads/main/APIs/sc2.yaml | active | 30/30 | 0.0% | - | 104.0 | 0 | 1 | 220 | 0 | 0 | 221 |
| https://raw.githubusercontent.com/ts-sf/fly/main/clash | active | 30/30 | 46.5% | 33.3% | 94.7 | 93 | 10 | 14 | 1 | 82 | 107 |
| https://raw.githubusercontent.com/liMilCo/v2r/main/base64/2.txt | active | 30/30 | 18.4% | 100.0% | 90.0 | 86 | 17 | 168 | 54 | 143 | 382 |
| https://proxypool.link/trojan/sub | active | 22/30 | 98.1% | 66.7% | 87.7 | 204 | 0 | 0 | 0 | 4 | 4 |
| https://raw.githubusercontent.com/xtoolkit/TVC/main/subscriptions/meta/mix | active | 30/30 | 22.0% | 82.4% | 77.4 | 85 | 16 | 108 | 4 | 174 | 302 |
| https://raw.githubusercontent.com/F0rc3Run/F0rc3Run/refs/heads/main/splitted-by-protocol/vless.txt | active | 30/30 | 26.5% | 100.0% | 75.0 | 69 | 1 | 64 | 0 | 126 | 191 |
| https://raw.githubusercontent.com/barry-far/V2ray-config/main/Sub2.txt | active | 30/30 | 13.2% | 100.0% | 71.2 | 64 | 20 | 46 | 99 | 257 | 422 |
| https://github.com/crackbest/V2ray-Config/raw/refs/heads/main/config.txt | active | 30/30 | 16.7% | 100.0% | 69.1 | 76 | 13 | 135 | 56 | 175 | 379 |
| https://raw.githubusercontent.com/crackbest/V2ray-Config/refs/heads/main/config.txt | active | 30/30 | 16.7% | 100.0% | 69.1 | 76 | 13 | 135 | 56 | 175 | 379 |
| https://raw.githubusercontent.com/Q3dlaXpoaQ/V2rayN_Clash_Node_Getter/main/APIs/sc0.yaml | active | 30/30 | 21.8% | 100.0% | 58.6 | 63 | 4 | 104 | 14 | 104 | 226 |
| https://raw.githubusercontent.com/Q3dlaXpoaQ/V2rayN_Clash_Node_Getter/refs/heads/main/APIs/sc0.yaml | active | 30/30 | 21.8% | 100.0% | 58.6 | 63 | 4 | 104 | 14 | 104 | 226 |
| https://node.freeclashnode.com/uploads/{Y}/{mm}/2-{Ymd}.yaml | active | 30/30 | 4.6% | 99.0% | 57.1 | 104 | 7 | 1494 | 260 | 390 | 2151 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/clashfree.yaml | active | 30/30 | 10.1% | 64.3% | 56.0 | 56 | 31 | 210 | 237 | 20 | 498 |
| https://github.com/Au1rxx/free-vpn-subscriptions/raw/main/output/by-country/v2ray-base64-HK.txt | active | 30/30 | 78.4% | 87.9% | 55.0 | 91 | 0 | 9 | 14 | 2 | 25 |
| https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/main/BLACK_VLESS_RUS_mobile.txt | active | 30/30 | 19.8% | 100.0% | 53.4 | 16 | 11 | 18 | 0 | 36 | 65 |
| https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/main/Base64/BLACK_VLESS_RUS_mobile_base64.txt | active | 30/30 | 25.5% | 100.0% | 52.9 | 36 | 5 | 22 | 19 | 59 | 105 |
| https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/main/Base64/BLACK_VLESS_RUS_base64.txt | active | 30/30 | 31.1% | 100.0% | 48.0 | 37 | 3 | 21 | 0 | 58 | 82 |
| https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/main/BLACK_VLESS_RUS.txt | active | 30/30 | 22.2% | 100.0% | 47.3 | 10 | 0 | 10 | 0 | 25 | 35 |
| https://node.freeclashnode.com/uploads/{Y}/{mm}/0-{Ymd}.yaml | active | 30/30 | 21.2% | 100.0% | 45.8 | 62 | 4 | 108 | 14 | 104 | 230 |
| https://raw.githubusercontent.com/acymz/AutoVPN/main/data/V2.txt | active | 30/30 | 13.5% | 100.0% | 37.1 | 51 | 12 | 95 | 121 | 98 | 326 |
| https://raw.githubusercontent.com/Arefgh72/v2ray-proxy-pars-tester/main/output/github_all.txt | active | 30/30 | 1.2% | 100.0% | 35.7 | 79 | 0 | 2888 | 3550 | 158 | 6596 |
| https://raw.githubusercontent.com/ts-sf/fly/main/v2 | active | 30/30 | 13.4% | 100.0% | 30.3 | 27 | 11 | 131 | 1 | 31 | 174 |
| https://raw.githubusercontent.com/Ruk1ng001/freeSub/main/clash.yaml | active | 30/30 | 26.8% | 59.1% | 28.6 | 22 | 0 | 26 | 24 | 10 | 60 |
| https://raw.githubusercontent.com/Barabama/FreeNodes/main/nodes/blues.txt | active | 30/30 | 20.0% | 29.6% | 27.0 | 27 | 3 | 83 | 1 | 21 | 108 |
| https://raw.githubusercontent.com/PangTouY00/Auto_proxy/main/Long_term_subscription_num | active | 30/30 | 7.8% | 100.0% | 25.7 | 17 | 10 | 16 | 130 | 44 | 200 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/snakem982.yaml | active | 30/30 | 36.9% | 100.0% | 24.0 | 24 | 1 | 6 | 22 | 12 | 41 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/zhangkaiitugithub.yaml | active | 30/30 | 36.9% | 100.0% | 24.0 | 24 | 1 | 6 | 22 | 12 | 41 |
| https://github.com/Au1rxx/free-vpn-subscriptions/raw/main/output/by-country/v2ray-base64-KR.txt | active | 30/30 | 44.4% | 100.0% | 23.1 | 24 | 0 | 12 | 18 | 0 | 30 |
| https://raw.githubusercontent.com/hans-thomas/v2ray-subscription/refs/heads/master/servers.txt | active | 30/30 | 28.9% | 100.0% | 20.2 | 13 | 0 | 6 | 11 | 15 | 32 |
| https://raw.githubusercontent.com/snakem982/proxypool/main/source/clash-meta-2.yaml | active | 30/30 | 28.6% | 66.7% | 19.3 | 18 | 0 | 27 | 13 | 5 | 45 |
| https://raw.githubusercontent.com/peasoft/NoMoreWalls/master/list.meta.yml | active | 30/30 | 7.7% | 100.0% | 18.4 | 12 | 10 | 8 | 124 | 1 | 143 |
| https://raw.githubusercontent.com/peasoft/NoMoreWalls/master/snippets/nodes.meta.yml | active | 30/30 | 7.7% | 100.0% | 18.4 | 12 | 10 | 8 | 124 | 1 | 143 |
| https://raw.githubusercontent.com/LoneKingCode/free-proxy-db/main/proxies/all.txt | active | 30/30 | 4.7% | 83.3% | 18.1 | 18 | 2 | 191 | 113 | 61 | 367 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/yudou.yaml | active | 30/30 | 25.8% | 82.4% | 17.0 | 17 | 0 | 36 | 5 | 8 | 49 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/tssf.yaml | active | 30/30 | 19.8% | 50.0% | 16.0 | 16 | 7 | 39 | 14 | 5 | 65 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/aiboboxx.yaml | active | 30/30 | 2.1% | 26.7% | 15.0 | 15 | 19 | 635 | 24 | 23 | 701 |
| https://raw.githubusercontent.com/Surfboardv2ray/v2ray-worker-sub/refs/heads/master/Eternity.txt | active | 30/30 | 7.5% | 20.0% | 15.0 | 15 | 0 | 4 | 152 | 29 | 185 |
| https://raw.githubusercontent.com/ovmvo/SubShare/main/sub/permanent/mihomo.yaml | active | 30/30 | 20.0% | 100.0% | 14.1 | 5 | 4 | 4 | 9 | 3 | 20 |
| https://www.xrayvip.com/free.txt | active | 30/30 | 12.2% | 100.0% | 13.9 | 12 | 2 | 5 | 2 | 77 | 86 |
| https://raw.githubusercontent.com/MatinGhanbari/v2ray-configs/main/subscriptions/v2ray/subs/sub2.txt | active | 30/30 | 8.7% | 16.7% | 12.0 | 12 | 0 | 108 | 17 | 1 | 126 |
| https://raw.githubusercontent.com/shaoyouvip/free/refs/heads/main/all.yaml | active | 30/30 | 45.5% | 80.0% | 11.5 | 10 | 0 | 5 | 5 | 2 | 12 |
| https://raw.githubusercontent.com/mahdibland/ShadowsocksAggregator/master/Eternity.yml | active | 30/30 | 3.5% | 100.0% | 9.5 | 7 | 0 | 59 | 126 | 9 | 194 |
| https://raw.githubusercontent.com/mgit0001/test_clash/main/heima.txt | active | 30/30 | 32.0% | 100.0% | 8.0 | 8 | 0 | 6 | 11 | 0 | 17 |
| https://raw.githubusercontent.com/mgit0001/test_clash/refs/heads/main/heima.txt | active | 30/30 | 32.0% | 100.0% | 8.0 | 8 | 0 | 6 | 11 | 0 | 17 |
| https://raw.githubusercontent.com/ggborr/FREEE-VPN/main/3v2 | active | 26/30 | - | - | 7.8 | 0 | 0 | 0 | 0 | 0 | 0 |
| https://raw.githubusercontent.com/Barabama/FreeNodes/main/nodes/ndnode.txt | active | 30/30 | 50.0% | 0.0% | 7.0 | 7 | 0 | 6 | 1 | 0 | 7 |
| https://raw.githubusercontent.com/vxiaov/free_proxies/main/clash/clash.provider.yaml | active | 30/30 | 26.9% | 100.0% | 7.0 | 7 | 0 | 8 | 11 | 0 | 19 |
| https://raw.githubusercontent.com/zhangkaiitugithub/passcro/main/speednodes.yaml | active | 30/30 | 58.3% | 100.0% | 7.0 | 7 | 0 | 1 | 3 | 1 | 5 |
| https://raw.githubusercontent.com/xiaoji235/airport-free/refs/heads/main/v2ray/v2rayshare.txt | active | 30/30 | 8.7% | 100.0% | 6.5 | 2 | 0 | 8 | 9 | 4 | 21 |
| https://raw.githubusercontent.com/justVisiting992/xray-Config-Collector/main/clash.yaml | active | 30/30 | 0.3% | 100.0% | 6.1 | 3 | 31 | 517 | 405 | 158 | 1111 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/_pool.yaml | active | 30/30 | 2.6% | 0.0% | 6.0 | 6 | 0 | 141 | 73 | 8 | 222 |
| https://raw.githubusercontent.com/actionsfz/v2ray/master/all.yaml | active | 30/30 | 7.1% | 100.0% | 6.0 | 6 | 0 | 40 | 8 | 31 | 79 |
| https://raw.githubusercontent.com/actionsfz/v2ray/refs/heads/master/all.yaml | active | 30/30 | 7.1% | 100.0% | 6.0 | 6 | 0 | 40 | 8 | 31 | 79 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/xrayvip.yaml | active | 30/30 | 25.0% | 50.0% | 6.0 | 6 | 0 | 4 | 3 | 11 | 18 |
| https://github.com/Au1rxx/free-vpn-subscriptions/raw/main/output/by-country/v2ray-base64-TW.txt | active | 30/30 | 12.1% | 100.0% | 5.9 | 7 | 0 | 0 | 10 | 41 | 51 |
| https://raw.githubusercontent.com/peacefish/nodefree/main/sub/proxy_cf.yaml | active | 30/30 | 3.2% | 100.0% | 5.8 | 2 | 3 | 48 | 9 | 1 | 61 |
| https://raw.githubusercontent.com/Shjpr9/Subs/refs/heads/main/sub.txt | active | 30/30 | 3.5% | 40.0% | 5.0 | 5 | 15 | 90 | 0 | 34 | 139 |
| https://raw.githubusercontent.com/F0rc3Run/F0rc3Run/refs/heads/main/splitted-by-protocol/trojan.txt | active | 30/30 | 21.1% | 100.0% | 4.3 | 4 | 2 | 0 | 0 | 13 | 15 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/ttvg.yaml | active | 30/30 | 22.2% | 75.0% | 4.0 | 4 | 0 | 4 | 1 | 9 | 14 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/hkaa0.yaml | active | 30/30 | 0.1% | 100.0% | 4.0 | 4 | 0 | 6144 | 10 | 0 | 6154 |
| https://raw.githubusercontent.com/F0rc3Run/F0rc3Run/refs/heads/main/splitted-by-protocol/vmess.txt | active | 30/30 | 0.0% | - | 3.9 | 0 | 4 | 40 | 0 | 0 | 44 |
| https://raw.githubusercontent.com/Barabama/FreeNodes/main/nodes/nodefree.txt | active | 30/30 | 13.0% | 100.0% | 3.0 | 3 | 0 | 3 | 10 | 7 | 20 |
| https://raw.githubusercontent.com/mfbpn/tg_mfbpn_sub/main/trial.yaml | active | 30/30 | 2.5% | 0.0% | 3.0 | 3 | 0 | 114 | 0 | 1 | 115 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/mahdibland.yaml | active | 30/30 | 1.5% | 33.3% | 3.0 | 3 | 0 | 35 | 159 | 2 | 196 |
| https://raw.githubusercontent.com/Barabama/FreeNodes/main/nodes/v2rayshare.txt | active | 30/30 | 13.0% | 100.0% | 3.0 | 3 | 0 | 3 | 10 | 7 | 20 |
| https://raw.githubusercontent.com/Barabama/FreeNodes/main/nodes/wenode.txt | active | 30/30 | 13.0% | 100.0% | 3.0 | 3 | 0 | 3 | 10 | 7 | 20 |
| https://raw.githubusercontent.com/Barabama/FreeNodes/main/nodes/yudou66.txt | active | 30/30 | 1.8% | 100.0% | 3.0 | 3 | 0 | 142 | 10 | 9 | 161 |
| https://raw.githubusercontent.com/Barabama/FreeNodes/main/nodes/yudou66.yaml | active | 30/30 | 1.8% | 100.0% | 3.0 | 3 | 0 | 141 | 10 | 9 | 160 |
| https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/main/BLACK_SS+All_RUS.txt | active | 30/30 | 3.1% | 100.0% | 2.6 | 2 | 11 | 24 | 26 | 1 | 62 |
| https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/main/Base64/BLACK_SS+All_RUS_base64.txt | active | 29/30 | 1.4% | 100.0% | 2.5 | 1 | 1 | 22 | 43 | 4 | 70 |
| https://raw.githubusercontent.com/Pawdroid/Free-servers/refs/heads/main/sub | active | 30/30 | 5.0% | 100.0% | 2.4 | 1 | 0 | 5 | 0 | 14 | 19 |
| https://raw.githubusercontent.com/Pawdroid/Free-servers/main/sub | active | 30/30 | 5.0% | 100.0% | 2.4 | 1 | 0 | 5 | 0 | 14 | 19 |
| https://raw.githubusercontent.com/free18/v2ray/main/c.yaml | active | 30/30 | 0.0% | - | 2.2 | 0 | 3 | 285 | 0 | 0 | 288 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/SFZY666.yaml | active | 30/30 | 16.7% | 0.0% | 2.0 | 2 | 1 | 9 | 0 | 0 | 10 |
| https://raw.githubusercontent.com/hello-world-1989/cn-news/main/end-gfw-together | active | 30/30 | 100.0% | 100.0% | 2.0 | 2 | 0 | 0 | 0 | 0 | 0 |
| https://raw.githubusercontent.com/Q3dlaXpoaQ/V2rayN_Clash_Node_Getter/main/APIs/sc3.yaml | active | 30/30 | 3.3% | 100.0% | 1.5 | 1 | 3 | 26 | 0 | 0 | 29 |
| https://raw.githubusercontent.com/Q3dlaXpoaQ/V2rayN_Clash_Node_Getter/refs/heads/main/APIs/sc3.yaml | active | 30/30 | 3.3% | 100.0% | 1.5 | 1 | 3 | 26 | 0 | 0 | 29 |
| https://node.freeclashnode.com/uploads/{Y}/{mm}/3-{Ymd}.yaml | active | 30/30 | 3.3% | 100.0% | 1.4 | 1 | 3 | 26 | 0 | 0 | 29 |
| https://raw.githubusercontent.com/firefoxmmx2/v2rayshare_subcription/main/subscription/clash_sub.yaml | active | 30/30 | 3.3% | 100.0% | 1.4 | 1 | 3 | 26 | 0 | 0 | 29 |
| https://raw.githubusercontent.com/asgharkapk/Sub-Config-Extractor/main/output_configs/mixed/Leon406/SubCrawler/sub/share/a11.yaml | active | 30/30 | 3.1% | 66.7% | 1.0 | 3 | 0 | 39 | 53 | 1 | 93 |
| https://raw.githubusercontent.com/Barabama/FreeNodes/main/nodes/clashmeta.txt | active | 30/30 | 8.3% | 0.0% | 1.0 | 1 | 0 | 4 | 2 | 5 | 11 |
| https://www.ermao.net/sub/clash/ermao.net | active | 30/30 | 0.0% | - | 1.0 | 0 | 0 | 14 | 6 | 0 | 20 |
| https://raw.githubusercontent.com/ermaozi/get_subscribe/main/subscribe/clash.yml | active | 29/30 | 0.0% | - | 1.0 | 0 | 0 | 14 | 6 | 0 | 20 |
| https://raw.githubusercontent.com/vxiaov/free_proxies/main/links.txt | active | 29/30 | 14.3% | 100.0% | 1.0 | 1 | 0 | 1 | 5 | 0 | 6 |
| https://raw.githubusercontent.com/chengaopan/AutoMergePublicNodes/master/list.yml | active | 30/30 | 0.0% | - | 0.5 | 0 | 10 | 8 | 11 | 0 | 29 |
| https://raw.githubusercontent.com/go4sharing/sub/main/sub.yaml | active | 30/30 | 14.3% | 100.0% | 0.4 | 1 | 0 | 2 | 4 | 0 | 6 |
| https://raw.githubusercontent.com/HakurouKen/free-node/main/public | active | 30/30 | 0.0% | - | 0.4 | 0 | 0 | 1 | 15 | 0 | 16 |
| https://raw.githubusercontent.com/Misaka-blog/chromego_merge/main/sub/merged_proxies_new.yaml | active | 30/30 | 0.0% | - | 0.3 | 0 | 10 | 8 | 11 | 0 | 29 |
| https://raw.githubusercontent.com/peasoft/NoMoreWalls/master/list.yml | active | 30/30 | 0.0% | - | 0.2 | 0 | 10 | 7 | 8 | 0 | 25 |
| https://raw.githubusercontent.com/Delta-Kronecker/V2ray-Config/main/config/clash.yaml | active | 30/30 | - | - | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 |
| https://raw.githubusercontent.com/DukeMehdi/FreeList-V2ray-Configs/refs/heads/main/Configs/VMESS-DukeMehdi-Configs.txt | active | 30/30 | - | - | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 |
| https://github.com/AzadNetCH/Clash/raw/refs/heads/main/AzadNet.txt | active | 30/30 | 0.0% | - | 0.0 | 0 | 0 | 1 | 16 | 0 | 17 |
| https://raw.githubusercontent.com/aiboboxx/v2rayfree/main/README.md | active | 30/30 | 0.0% | - | 0.0 | 0 | 0 | 0 | 20 | 0 | 20 |
| https://raw.githubusercontent.com/aiboboxx/v2rayfree/refs/heads/main/README.md | active | 30/30 | 0.0% | - | 0.0 | 0 | 0 | 0 | 20 | 0 | 20 |
| https://raw.githubusercontent.com/roosterkid/openproxylist/refs/heads/main/V2RAY.txt | active | 30/30 | - | - | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 |
| https://node.freeclashnode.com/uploads/{Y}/{mm}/1-{Ymd}.yaml | active | 30/30 | 0.0% | - | 0.0 | 0 | 4 | 253 | 1 | 0 | 258 |
| https://raw.githubusercontent.com/Q3dlaXpoaQ/V2rayN_Clash_Node_Getter/main/APIs/sc1.yaml | active | 30/30 | 0.0% | - | 0.0 | 0 | 3 | 255 | 1 | 0 | 259 |
| https://raw.githubusercontent.com/Q3dlaXpoaQ/V2rayN_Clash_Node_Getter/refs/heads/main/APIs/sc1.yaml | active | 30/30 | 0.0% | - | 0.0 | 0 | 3 | 255 | 1 | 0 | 259 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/chengaopan.yaml | active | 30/30 | 0.0% | - | 0.0 | 0 | 0 | 15 | 1 | 0 | 16 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/peasoft.yaml | active | 30/30 | 0.0% | - | 0.0 | 0 | 10 | 15 | 1 | 0 | 26 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/ripaojiedian.yaml | active | 30/30 | 0.0% | - | 0.0 | 0 | 0 | 13 | 1 | 0 | 14 |
| https://raw.githubusercontent.com/ripaojiedian/freenode/main/clash | active | 30/30 | 0.0% | - | 0.0 | 0 | 0 | 6 | 8 | 0 | 14 |
| https://raw.githubusercontent.com/Barabama/FreeNodes/main/nodes/clashmeta.yaml | active | 30/30 | 0.0% | - | 0.0 | 0 | 0 | 89 | 0 | 0 | 89 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/blue-Youtube.yaml | active | 30/30 | 0.0% | - | 0.0 | 0 | 1 | 46 | 0 | 0 | 47 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/Pawdroid.yaml | active | 30/30 | 0.0% | - | 0.0 | 0 | 0 | 5 | 2 | 1 | 8 |
| https://node.freeclashnode.com/uploads/{Y}/{mm}/4-{Ymd}.yaml | active | 30/30 | - | - | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 |
| https://github.com/mermeroo/V2RAY-CLASH-BASE64-Subscription.Links/raw/refs/heads/main/SUB%20LINKS | active | 30/30 | - | - | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 |
| https://raw.githubusercontent.com/andigwandi/free-proxy/main/proxy_list.txt | active | 30/30 | - | - | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 |
| https://raw.githubusercontent.com/asgharkapk/Sub-Config-Extractor/main/output_configs/clash/Ruk1ng001.yaml | active | 30/30 | - | - | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 |
| https://raw.githubusercontent.com/asgharkapk/Sub-Config-Extractor/main/output_configs/surfboard/Barabama_ndnode.yaml | active | 30/30 | - | - | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 |
| https://raw.githubusercontent.com/asgharkapk/Sub-Config-Extractor/main/output_configs/surfboard/Ruk1ng001.yaml | active | 30/30 | - | - | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 |
| https://raw.githubusercontent.com/Barabama/FreeNodes/main/nodes/nodev2ray.txt | active | 30/30 | 0.0% | - | 0.0 | 0 | 0 | 12 | 1 | 0 | 13 |
| https://raw.githubusercontent.com/dpangestuw/Free-Proxy/main/All_proxies.txt | active | 30/30 | - | - | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 |
| https://raw.githubusercontent.com/linzjian666/chromego_extractor/main/outputs/clash_meta.yaml | active | 30/30 | - | - | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 |
| https://raw.githubusercontent.com/officialputuid/ProxyForEveryone/main/xResults/old-data/RAW.txt | active | 30/30 | - | - | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 |
| https://raw.githubusercontent.com/officialputuid/ProxyForEveryone/main/xResults/RAW.txt | active | 30/30 | - | - | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 |
| https://raw.githubusercontent.com/shahidbhutta/Clash/main/Router | active | 30/30 | - | - | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 |
| https://raw.githubusercontent.com/shahidbhutta/Clash/refs/heads/main/Router | active | 30/30 | - | - | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/changfengoss.yaml | active | 30/30 | 0.0% | - | 0.0 | 0 | 1 | 1 | 1 | 0 | 3 |
| https://raw.githubusercontent.com/SnapdragonLee/SystemProxy/master/dist/clash_config.yaml | active | 30/30 | - | - | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 |
| https://raw.githubusercontent.com/xiaoji235/airport-free/refs/heads/main/v2ray/naidounode.txt | active | 30/30 | - | - | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 |
| https://raw.githubusercontent.com/sinspired/airport/main/subs/ermaozi.yaml | active | 29/30 | 0.0% | - | 0.0 | 0 | 0 | 16 | 3 | 2 | 21 |
| https://free.datiya.com/uploads/{Ymd}-v2ray.txt | active | 16/30 | - | - | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 |
| https://free.datiya.com/uploads/{Ymd}-clash.yaml | active | 15/30 | - | - | 0.0 | 0 | 0 | 0 | 0 | 0 | 0 |
| https://mihomoparty.github.io/uploads/{Y}/{mm}/2-{Ymd}.txt | disabled | 6/18 |  |  | 593.3 | 0 |  |  |  |  |  |
| https://clashbest.github.io/uploads/{Y}/{mm}/2-{Ymd}.txt | disabled | 6/18 |  |  | 593.3 | 0 |  |  |  |  |  |
| https://mihomoparty.github.io/uploads/{Y}/{mm}/4-{Ymd}.txt | disabled | 6/18 |  |  | 202.7 | 0 |  |  |  |  |  |
| https://clashbest.github.io/uploads/{Y}/{mm}/2-{Ymd}.yaml | disabled | 6/18 |  |  | 91.3 | 0 |  |  |  |  |  |
| https://clashbest.github.io/uploads/{Y}/{mm}/1-{Ymd}.txt | disabled | 6/18 |  |  | 19.3 | 0 |  |  |  |  |  |
| https://clashbest.github.io/uploads/{Y}/{mm}/0-{Ymd}.txt | disabled | 6/18 |  |  | 16.3 | 0 |  |  |  |  |  |
| https://clashbest.github.io/uploads/{Y}/{mm}/0-{Ymd}.yaml | disabled | 6/18 |  |  | 0.0 | 0 |  |  |  |  |  |
| https://clashbest.github.io/uploads/{Y}/{mm}/1-{Ymd}.yaml | disabled | 6/18 |  |  | 0.0 | 0 |  |  |  |  |  |
| https://clashbest.github.io/uploads/{Y}/{mm}/3-{Ymd}.yaml | disabled | 6/18 |  |  | 0.0 | 0 |  |  |  |  |  |
| https://clashbest.github.io/uploads/{Y}/{mm}/4-{Ymd}.yaml | disabled | 6/18 |  |  | 0.0 | 0 |  |  |  |  |  |
| https://clashbest.github.io/uploads/{Y}/{mm}/{Ymd}.json | disabled | 6/18 |  |  | 0.0 | 0 |  |  |  |  |  |
| https://mihomoparty.github.io/uploads/{Y}/{mm}/0-{Ymd}.yaml | disabled | 6/18 |  |  | 0.0 | 0 |  |  |  |  |  |
| https://mihomoparty.github.io/uploads/{Y}/{mm}/1-{Ymd}.yaml | disabled | 6/18 |  |  | 0.0 | 0 |  |  |  |  |  |
| https://mihomoparty.github.io/uploads/{Y}/{mm}/4-{Ymd}.yaml | disabled | 6/18 |  |  | 0.0 | 0 |  |  |  |  |  |
| https://mihomoparty.github.io/uploads/{Y}/{mm}/{Ymd}.json | disabled | 6/18 |  |  | 0.0 | 0 |  |  |  |  |  |
| https://link.rittbo.kdns.fr/sub?token=8794e5157120a9982b0ceed9dcef5de7 | disabled | 0/12 |  |  | 0.0 | 0 |  |  |  |  |  |
| https://raw.githubusercontent.com/free-nodes/v2rayfree/main/v{ymd}1 | disabled | 0/12 |  |  | 0.0 | 0 |  |  |  |  |  |
| https://raw.githubusercontent.com/free-nodes/v2rayfree/main/v{ymd}2 | disabled | 0/12 |  |  | 0.0 | 0 |  |  |  |  |  |
| https://raw.githubusercontent.com/lagzian/SS-Collector/main/SS/trinity_clash.yaml | disabled | 0/12 |  |  | 0.0 | 0 |  |  |  |  |  |
| https://raw.githubusercontent.com/lagzian/SS-Collector/main/SS/TrinityBase | disabled | 0/12 |  |  | 0.0 | 0 |  |  |  |  |  |
| https://raw.githubusercontent.com/lagzian/SS-Collector/main/SS/VM_TrinityBase | disabled | 0/12 |  |  | 0.0 | 0 |  |  |  |  |  |
| https://raw.githubusercontent.com/MrMohebi/xray-proxy-grabber-telegram/master/collected-proxies/clash-meta/all.yaml | disabled | 0/12 |  |  | 0.0 | 0 |  |  |  |  |  |
| https://raw.githubusercontent.com/yorkLiu/FreeV2RayNode/main/v2ray.txt | disabled | 0/12 |  |  | 0.0 | 0 |  |  |  |  |  |

## 聚合源（按近 N 次平均拉取数降序）
| id | 链接 | 成功率 | 重复率 | 最近 | 平均 |
|---|---|:---:|:---:|---|---|
| sinspired_scan | https://raw.githubusercontent.com/sinspired/airport/main/subs/merged/scan.txt | 30/30 | 0.0% | 20 | 18.6 |
| sinspired_col | https://raw.githubusercontent.com/sinspired/airport/main/subs/merged/col.txt | 30/30 | 0.0% | 17 | 16.9 |
| sinspired_cm | https://raw.githubusercontent.com/sinspired/airport/main/subs/merged/cm.txt | 30/30 | 0.0% | 13 | 14.1 |
