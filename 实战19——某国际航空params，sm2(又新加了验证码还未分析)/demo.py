from loguru import logger
import requests
import json
import execjs


headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Connection": "keep-alive",
    "Content-Type": "application/json",
    "Origin": "https://www.airchina.com.cn",
    "Referer": "https://www.airchina.com.cn/flight/oneway/szx-hgh/2025-06-06",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "Sgm-Context": "114111441112441230;114111441112441230",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36 Edg/137.0.0.0",
    "X-Device-Token": "tak01j5DZ5VFTYM5MQZEVOVXK6WB7ISVS5VHN4C4UJHMEN4HLH6YUIUV3T3GP4KXMWOAO5TZN7PBBWPADIZLVTUHC254VND26JK4NKKGT47NOQ3ERMQ6BY4R4FMOANLLLJCGHVIYUBBDILMMRTU3RRQVTJYQGINO5E",
    "X-Locale": "zh-CN",
    "sec-ch-ua": "\"Microsoft Edge\";v=\"137\", \"Chromium\";v=\"137\", \"Not/A)Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\""
}
cookies = {
    "HWWAFSESTIME": "1749046799508",
    "HWWAFSESID": "2c69f8b7fef6197375",
    "ariauseGraymode": "false",
    "arialoadData": "true",
    "ariawapChangeViewPort": "false",
    "_gcl_au": "1.1.966318956.1749046807",
    "_ga": "GA1.1.1098330176.1749046808",
    "TKAEQLILOIB0YIMO": "tak01j5DZ5VFTYM5MQZEVOVXK6WB7ISVS5VHN4C4UJHMEN4HLH6YUIUV3T3GP4KXMWOAO5TZN7PBBWPADIZLVTUHC254VND26JK4NKKGT47NOQ3ERMQ6BY4R4FMOANLLLJCGHVIYUBBDILMMRTU3RRQVTJYQGINO5E",
    "_ga_CGYVD7S4G4": "GS2.1.s1749046807$o1$g1$t1749047802$j60$l0$h0"
}

params_json = {
    "Trip": [
        {
            "Date": "2025-06-11",
            "Dep": "SZX",
            "Arrival": "HGH"
        }
    ],
    "Passenger": {
        "adult": 1,
        "child": 0,
        "baby": 0
    },
    "notchType": None,
    "aimPrice": None,
    "RequestParameterSecurityIdentificationBit": True
}
params = execjs.compile(open('demo.js', 'r', encoding='utf-8').read()).call('get_params',params_json)
logger.info(f"parama==>{params}")
url = "https://www.airchina.com.cn/gateway/api/flight/list"
data = {
    # "params": "326c030336e2cc6c73629fcde0d2adb040f61e41158fec9ae2521a98a64ffec345f80f0e5f1be259136c9dab632b89696762a797dae9d5da2ed1deae1bd4b819d10fa0b8c81e9112ecc9c34fd08809625de45a4093ae78252d941d78b4807657779174b89f34dfe1c259c8b354112420c88dfa01b276580987b3e27552dc4f9c92c1e52be8e92a5a062963d625512e5de94479fe21a6b9a6975d06f376fb4959995ac438265fe8026b0c7203a1f76e87c62fef5c82f3a6d6e334e9908d449b04557c25367e33f02a649cb6bdb4ac36db52d1ed7ba71f7a63340e67b60ae720f82b6b8da5362d70096f44a813dd616ae5535fc6a3ed59ca8abfdb21f9a3f825da8bb9c52091525fa6ef94235c09798f5b8e3806e4965ada3a269a0ebeb51b68d36a2958208a4192d47fda58365cfc69788f6470b45172b0c63c139237b677475c817abddd2e1e74e612ffb0c033d9f9accf33b57b077bc6c9845680e0b75fe50d622e39d968f93faf0fc162cbe5c8cc8600eed08fcd2a5a11b8de9888e26731bc69d42c0d8f6123",
    "RequestParameterEncryptionIdentificationBit": True
}
data['params'] = params
data = json.dumps(data, separators=(',', ':'))
response = requests.post(url, headers=headers, cookies=cookies, data=data)
logger.success(response.text)