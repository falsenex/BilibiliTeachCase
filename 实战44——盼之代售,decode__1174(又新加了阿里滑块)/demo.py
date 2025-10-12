import requests,re,time
import json,execjs
from loguru import logger
requests = requests.Session()
requests.headers = headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-Type": "application/json",
    "Origin": "https://www.pzds.com",
    "PZOs": "windows",
    "PZPlatform": "pc",
    "PZTimestamp": "1760025778808",
    "PZVersion": "1.0.0",
    "PZVersionCode": "1",
    "Pragma": "no-cache",
    "Random": "725627",
    "Referer": "https://www.pzds.com/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "Sign": "240fa355cc3ebabcdda1c301ba3f930c",
    "Skey": "CLIENT",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36",
    "channelInfo": "{\"channelCode\":null,\"tag\":null,\"channelType\":null,\"searchWord\":\"null\",\"adExtras\":\"\",\"urlParam\":\"\"}",
    "sec-ch-ua": "\"Google Chrome\";v=\"137\", \"Chromium\";v=\"137\", \"Not/A)Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "x-oss-forbid-overwrite": "true"
}
url = "https://api.pzds.com/api/web-client/v2/public/goodsPublic/page"
params = {
    "decode__1174": "28178cb220-kS865TgTRTp_PrTETj6ZQxTwTldTHU7SPTBPTSzl4a3opP1DZ8JSTWEW7f0iiZhG/2kDjcTl6T_TY67r80D6MlTm6HlTBf6Tq06MiTuTOcJwTOyToTlG7Tg6lvTDTH0TrximIRT7Y6JGXGyl2xPy96J/06PVbgdVGMgV8H66lT2UVP145ggyV72U4tgiYgPS3T"
}
# cookies = execjs.compile(open('./decode_1174.js', 'r',encoding='utf-8').read()).call('get_cookies')
# cookies['tfstk'] = "gl-KEDfDpfcniVVUpQ0iqs0XItHioVvF6BJbq_f3PCd9hKPhPg4le_19a6bhAHAJwIJP4pfhZCI1e1zWwLkFF_OWw_YnSmveLgSSiQnmmpk4db8k9y_CCY6VEJMGRtfz-lsSijmi9s3p6gOknboC5d1NeTaCFQisfT11F9aBN1_1htVCVgOSBG6Vd_N5Ow611T11NgsWNdMOU16CVgOWCABrN62dZJ182egisIkmwwZ7VhBd5VvC1XYvf9QFGptLVuMVpwCXd1hBq6I55L7J48rRypT2atOQObCyXdtBlIGg-6TAeKYJdDZ1xHJBlatjaz9Fx6I6AEe7VdIdtQKJ_WhOGHJ60G_icxp6bBveXL2SVOAc1p-C2mMVvM1CXO-o_k1J5Uth8gPIw_-9CHTR4j-DDBS7isBuRAHTzz7CQcgbcf24s4xhBsDgSzzPSOWOiAHTzz7CQOCmIc4zzNXN.",
cookies = {
    "_c_WBKFRo": "yKQQqjuKhqtJiFhFemjnrUmAEM8g4TmuqESjXcS1",
    "_nb_ioWEgULi": "",
    "Hm_lvt_8e2c03f98f8af83cf09317d232baf903": "1760021847,1760097168,1760189368",
    "Hm_lpvt_8e2c03f98f8af83cf09317d232baf903": "1760190628",
    "acw_tc": "0a06110717601906317035610e4337f29343c1096c866d3206d31a2926d286",
    "tfstk": "gl-KEDfDpfcniVVUpQ0iqs0XItHioVvF6BJbq_f3PCd9hKPhPg4le_19a6bhAHAJwIJP4pfhZCI1e1zWwLkFF_OWw_YnSmveLgSSiQnmmpk4db8k9y_CCY6VEJMGRtfz-lsSijmi9s3p6gOknboC5d1NeTaCFQisfT11F9aBN1_1htVCVgOSBG6Vd_N5Ow611T11NgsWNdMOU16CVgOWCABrN62dZJ182egisIkmwwZ7VhBd5VvC1XYvf9QFGptLVuMVpwCXd1hBq6I55L7J48rRypT2atOQObCyXdtBlIGg-6TAeKYJdDZ1xHJBlatjaz9Fx6I6AEe7VdIdtQKJ_WhOGHJ60G_icxp6bBveXL2SVOAc1p-C2mMVvM1CXO-o_k1J5Uth8gPIw_-9CHTR4j-DDBS7isBuRAHTzz7CQcgbcf24s4xhBsDgSzzPSOWOiAHTzz7CQOCmIc4zzNXN.",
    "ssxmod_itna": "1-YqGxuDgGDtd7qYIPYQA4QK4Cq47FsRx0dGMD3qiQGgDYq7=GFKDC27KRGaebuh0_Gwx8DWqD8KjwG21DBq4rrDnqD80DQeDvexuB44MCAhDrAiztexm1e=BAgqwNkVzD2P=omsUxlNYRykdD2kSxFbDCPDExGkKmn4_DiiOx0rD0eDPxDYDG4Do2YDnO4DjxDdkK3Ep9oDbxi3k4iaDGeDe6OpDYyeDD5a3zh3kSGxeBoxDG5x=siIYDGiRzL_M8RP_806iD2ID7v3DlPr_wjXwHtxEzM91qkTa40kRq0Op8_fQz2QzUfE0beqitqWe53bD45bDxKgDtGoK0DB7Qi7orODQD4q0787DoO=Gxm_DDiEmceo07e4o_gONlEN/o_YcGIieenmx7Ggm5r7GtSq_BGP0h1jKzBqdDPs7GwY4k_G59r_mmqhDxD",
    "ssxmod_itna2": "1-YqGxuDgGDtd7qYIPYQA4QK4Cq47FsRx0dGMD3qiQGgDYq7=GFKDC27KRGaebuh0_Gwx8DWqD8KjwGrrDGbe4YxH0jx4DL7eohLroU2YD/QzPIILKGe9igPA5jUjwywdstrCuOoeziOVK7i7CoTFdnHOmODrq/51imB_7O0D_2Pei8GpA2px5fvrO3KQbpp_YnyCyOmxlrYmK1BpAx2Au=04j=iGR/yOYjoET_SLUOmLpOx84b7xO2CRuEOwRDAqWqxrn_6_0Z3GZb8IQbAniqw_vd=R07tcmreRC6LK=RKq2=iI4_o8Uc87B2RFFD1w/9KtU_uAW7UPG7m9KG97YHIAyUbE4WwtwN4qEWY1/YjKPmjFw9v5xn93ek7YEIqEnGsfm4fThjDwGGse54oqEz770Rdrucn9iTq_Yayb86AqhInPrvTTexvPrifWco87eQAWFDm8mxmSSlSr7uFO8O7o_kWSulBawK8KaCpxHtI5=0OYcerPE8dOKGsPYQjA5c8HHgzPp5P3GGqE893hgwhLwnL5oup0u5XMv7u5waITIhKZ52fsSmGb=KMY8rO8iu9_1vWwHMeCela01s76KN76qBOSm7ikvBwDozsnl9F002Y/lqmnOb__qbGxWbHS5LnDOjt9qYm_4jndO3bDgbWYqb0_qQ4rfHVFX4TB4m7S2BNmtrmIQNWVYP8a9Q5t0cW3HyOjD7rAief2l1s1xOBDdDeY4_DxGh8YIjqZ0NBP/0_0eO7KRewADD"
}
logger.success(f"成功获取cookie信息{cookies}")
data = {
    "order": "ASC",
    "sort": None,
    "page": 6,
    "pageSize": 21,
    "action": {
        "gameId": "12",
        "goodsCatalogueId": 6,
        "merchantMark": None,
        "keywords": [],
        "searchWords": [],
        "searchPropertyIds": [],
        "unionGameIds": [],
        "goodsSearchActions": []
    }
}
data = json.dumps(data, separators=(',', ':'))
response = requests.post(url,
                         params=params,
                         data=data,cookies=cookies)
print(response.text)
_waf_bd8ce2ce37 = re.findall('{"_waf_bd8ce2ce37":"(.*?)"}',response.text)[0]
_waf_a86dfdc5f2 = int(time.time()*1000)
logger.info(f"成功获取_waf_bd8ce2ce37,_waf_a86dfdc5f2分别是：{_waf_bd8ce2ce37}，{_waf_a86dfdc5f2}")
params_header = execjs.compile(open("./decode_1174.js", "r", encoding="utf-8").read()).call('get_decode__1174',_waf_bd8ce2ce37,_waf_a86dfdc5f2,data)
header = {
    'PZTimestamp' : params_header['headers']['Timestamp'],
    'Random' : params_header['headers']['Random'],
    'Sign' : params_header['headers']['strMd5'],
}
requests.headers.update(header)
params = {
    "u_atoken": "365c97441cc71c0bd52cef70686fdf99",
    "u_asession": "01VVY01Pn07t-JVBZVw4Tc2etwY6kKbBtQBBVD10Y3h7Js-VMe1LQVRZG3xAfc9_t5VW_67TPbsWn6CLJQxHMS-myPlBJUEqctiaTooWaXr7I",
    "u_asig": "052xQEGc2kXC4VgME_yGJJ0_neSl3VsNfzSgYlOi_HYQt14nCf6zfgpZc1_RpezXHGKsYnDDTnfmF701xFSgFq0RJ_4eW0aUabZ-I5IrcfYTVd_feJfasPSAXzq5tjI-aCB5kGCO9k4n9rzqDyGnzP8unn6q0pLr_gDnY-8XBKF_ymdMbWFIxCNRWB6W-dI7wWA7fjSJR91dw4Bu1YW3-hRh_21n0W-myc2bQMlMlHmXPqV6Pwlqu-WUwSogsOUKKT9OSeg36EKVDdHfi9EjTspXFGRQ7fDVp1JsmCp9FCBkW7bwalKy10KstQfSzer_dCbiiqrhN3-lX1yglInruEbg",
    "decode__1174": params_header['decode__1174']
}
response = requests.post(url, params=params, data=data,cookies=cookies)
logger.success(response.text)