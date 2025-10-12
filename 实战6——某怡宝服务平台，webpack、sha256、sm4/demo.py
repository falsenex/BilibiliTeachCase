import time
import execjs
import requests
import json

from loguru import logger

_timestamp = int(time.time())
header_params = execjs.compile(open('demo.js','r',encoding='utf-8').read()).call('get_header_params')
headers = {
    "Accept": "application/json",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "keep-alive",
    "Content-Type": "application/json",
    "Origin": "https://fuwu.nhsa.gov.cn",
    "Referer": "https://fuwu.nhsa.gov.cn/nationalHallSt/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
    # "X-Tingyun": "c=B|4Nl_NnGbjwY;x=cb47b49f55724ea6",
    "channel": "web",
    "contentType": "application/x-www-form-urlencoded",
    "sec-ch-ua": "\"Chromium\";v=\"134\", \"Not:A-Brand\";v=\"24\", \"Google Chrome\";v=\"134\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    # "x-tif-nonce": "D8p7Xpff",
    "x-tif-paasid": "undefined",
    # "x-tif-signature": "2bb476510eaa122dca476274f98e5b394b073d210dae89687c0002f5f8107748",
    # "x-tif-timestamp": "1743603496"
}
headers['x-tif-nonce'] = header_params['x-tif-nonce']
headers['x-tif-signature'] = header_params['x-tif-signature']
headers['X-Tingyun'] = header_params['X-Tingyun']
headers['x-tif-timestamp'] = str(header_params['x-tif-timestamp'])
cookies = {
    "acw_tc": "276aedf017436031380502349e6c241380c84e404752c2c108c9a55b06753e"
}
url = "https://fuwu.nhsa.gov.cn/ebus/fuwu/api/nthl/api/CommQuery/queryFixedHospital"
data1 = {
    "data": {
        "addr": "",
        "regnCode": "110000",
        "medinsName": "",
        "medinsLvCode": "",
        "medinsTypeCode": "",
        "outMedOpenFlag": "",
        "pageNum": 4,
        "pageSize": 10,
        "queryDataSource": "es"
    },
    "appCode": "T98HPCGN5ZVVQBS8LZQNOAEXVI9GYHKQ",
    "version": "1.0.0",
    "encType": "SM4",
    "signType": "SM2",
    "timestamp": _timestamp
}
signData = execjs.compile(open('test.js','r',encoding='utf-8').read()).call('get_payload_signData',data1)
data2 = {**data1,**{"signData": signData}}
print(data2)
encData = execjs.compile(open('test.js','r',encoding='utf-8').read()).call('get_payload_encData',data2)
data = {
    "data": {
        "data": {
            'encData':encData
            # "encData": "3DFBCA4667B978F639BB23B95DCE4CC74CE34C33DC32F1068E9E23CA546C9EA8CCD20943B4DAE96380B41164D761DE9742C84A985FE3BABC31CB352556BB87C9C1495DB24A29AB6BC3A85AB7FCA00F33C56677481A67C67F739EE2C7D589054DC373615B5DDB33C24C5B31E61CB7643E8CCAA19EAE1FD36157CF9869E3A3753ED0B4E7BB97C60BF8E5275CAFCAFD1E13E384C10195003FD638576645B5EF45EA"
        },
        "appCode": "T98HPCGN5ZVVQBS8LZQNOAEXVI9GYHKQ",
        "version": "1.0.0",
        "encType": "SM4",
        "signType": "SM2",
        "timestamp": _timestamp,
        'signData': signData,
        # "signData": "lWIb40HBdD/KEyg8M3Zz9tuj5+LNG0Ei8p9e91fa6t6OfZEZDg4EXsPVz03zNkq4qcVM31lEALYAlqaiLMlRjA=="
    }
}
data = json.dumps(data, separators=(',', ':'))
response = requests.post(url, headers=headers, cookies=cookies, data=data)
logger.info('密文数据==》》' + str(response.json()['data']['data']['encData']))
mingwen = execjs.compile(open('test.js','r',encoding='utf-8').read()).call('decrypt_data',response.json())
logger.info('明文数据==>>' + str(mingwen))