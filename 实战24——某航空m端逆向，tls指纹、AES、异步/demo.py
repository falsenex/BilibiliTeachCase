#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：pythonProject 
@File    ：demo.py
@IDE     ：PyCharm 
@Author  ：haozaispider
@Date    ：2025/6/24 上午11:07 
'''
import execjs
# import requests
from curl_cffi import requests
import json
from loguru import logger

def get_data(mingwen_data):
    # 发送请求
    response = requests.post(
        'http://localhost:3000/api/encrypt',
        json=mingwen_data
    )
    return response.json()
def get_decrypt_data(miwen_data):
    response = requests.post(
        'http://localhost:3000/api/decrypt',
        json=miwen_data
    )
    return response.json()
headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-Type": "application/json",
    "M-CEAIR-ENCRYPTED": "true",
    "Origin": "https://m.ceair.com",
    "Pragma": "no-cache",
    "Referer": "https://m.ceair.com/mapp/reserve/flightList?newParam=%7B%22tripType%22%3A0,%22depCode%22%3A%22SIA%22,%22arrCode%22%3A%22UYN%22,%22dt%22%3A%221%22,%22at%22%3A%221%22,%22depN%22%3A%22%E8%A5%BF%E5%AE%89%22,%22arrN%22%3A%22%E6%A6%86%E6%9E%97%22,%22flightDate%22%3A%2220250624%22,%22carryChd%22%3Afalse,%22carryInf%22%3Afalse,%22productType%22%3A%22CASH%22,%22curIndex%22%3A0,%22memberLabel%22%3A%22%22,%22zoneCode%22%3A%22STRANGE_SHOPPING%22,%22isTax%22%3Afalse,%22interTax%22%3Atrue%7D&yjr_common_code=",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36 Edg/137.0.0.0",
    "X-CEAIR-OS": "M",
    # "X-Tingyun": "c=B|SLo-Zt9rm8k;x=27972d61ae514390",
    "ceair-token;": "",
    "sec-ch-ua": "\"Microsoft Edge\";v=\"137\", \"Chromium\";v=\"137\", \"Not/A)Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?1",
    "sec-ch-ua-platform": "\"Android\"",
    # "transactionId": "05202506240306245168"
}
X_Tingyun = execjs.compile(open("demo.js", "r", encoding="utf-8").read()).call("get_X_Tingyun")
logger.debug(f"获取的X_Tingyun: {X_Tingyun}")
transactionId = execjs.compile(open("demo.js", "r", encoding="utf-8").read()).call("get_transactionId")
logger.debug(f"获取的transactionId: {transactionId}")
headers["transactionId"] = transactionId
headers["X-Tingyun"] = X_Tingyun
cookies = {
    "language": "zh_CN",
    "acw_tc": "0aef82d717507338705378809e007db740da42379e5399b3c90d4c079317e2",
    "SERVERID": "1baa25caad917b8d89569fc585640086|1750734300|1750731998",
    "ssxmod_itna": "QqGxgDn7qeqYqqeKuDU2DQqQIkG=8DzxC5iOD+xQ5DODLxn+qGdqRD9jKRWxWqrcDetjgDxX3hKDD51DBwxXiDnqD8XDQeDv4Z4hb4SjahDNAQzSB4willhziu9ezyC/CgAwUK0aDbqGkqBGtq4iiOx0rD0eDPxDYDGbFD7PDoxDraFYDjBYp7fEwYF4DKx0kDYvKpY3DWgYieeoxDG5xyb0q3axDEBBpZh8o8DD1qCoqQBYD9p4Ds2wuR4DCN5=x1zg2oukTY8fEDCKDj28pVEhQr/OIPRkYPcWrhDIqQOHbPCDOdQDlM4pxDez7D170cDKDneZ4h=7Y4eWY/IB3vwtHS4xTCDNfT52vD54Oj2U375nrN/riF+if08YAxjx4f0K5n8CGxeD",
    "ssxmod_itna2": "QqGxgDn7qeqYqqeKuDU2DQqQIkG=8DzxC5iOD+xQ5DODLxn+qGdqRD9jKRWxWqrcDetjgDxX3hKDDviD83ehihCiio4kixj+w3tRR7GHfF6xGNKkM/=C9Upom=YC0YRz1GOnRHHyIRy9ac80OG=Q0DNvPAbq9KbixOW1ATNVenb4axqrInWToD"
}
url = "https://m.ceair.com/m-base/sale/shoppingv2"
mingwen_data = {
    "currentQueryType": "FLIGHT_LIST",
    "currentSegIndex": 0,
    "selectedRoutes": [],
    "productType": "CASH",
    "routes": [
        {
            "arrCode": "SZX",
            "depCode": "BJS",
            "flightDate": "20250625",
            "arrCodeType": "1",
            "depCodeType": "1",
            "depCityName": "北京",
            "arrCityName": "深圳",
            "segIndex": 0
        }
    ],
    "tripType": "OW",
    "cabinGrade": "",
    "zoneCode": "STRANGE_SHOPPING",
    "salesChannel": "7701",
    "moduleX": "mShopping",
    "os": "M",
    "appVersion": "99.0.0",
    "transactionId": transactionId
}
req = get_data(mingwen_data)["encryptedData"]
logger.info(f"请求的加密数据: {req}")
data = {
    "req": req
}
refer__1036 = execjs.compile(open("demo.js", "r", encoding="utf-8").read()).call("get_refer__1036",data)
logger.debug(f"获取的refer__1036: {refer__1036}")
params = {
    "refer__1036": refer__1036,
}
data = json.dumps(data, separators=(',', ':'))
response = requests.post(url, headers=headers, cookies=cookies, params=params, data=data)
logger.warning(f"请求成功密文数据：{response.json()}")
result = get_decrypt_data(response.json())
logger.success(f"请求成功明文数据：{result}")


