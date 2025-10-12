# import requests
#
#
# headers = {
#     "Accept": "application/json, text/plain, */*",
#     "Accept-Language": "zh-CN,zh;q=0.9",
#     "Connection": "keep-alive",
#     "Content-Type": "application/x-www-form-urlencoded",
#     "Origin": "https://login.dangdang.com",
#     "Referer": "https://login.dangdang.com/",
#     "Sec-Fetch-Dest": "empty",
#     "Sec-Fetch-Mode": "cors",
#     "Sec-Fetch-Site": "same-origin",
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36",
#     "sec-ch-ua": "\"Chromium\";v=\"136\", \"Google Chrome\";v=\"136\", \"Not.A/Brand\";v=\"99\"",
#     "sec-ch-ua-mobile": "?0",
#     "sec-ch-ua-platform": "\"Windows\""
# }
# cookies = {
#     "__permanent_id": "20250512210452215207919356244452060",
#     "__visit_id": "20250512210452311386734370226159540",
#     "__out_refer": "",
#     "__trace_id": "20250512212642538158635739667360112",
#     "JSESSIONID": "7D0FCF0F4A4162CA62B285C9499A4427",
#     "__rpm": "%7Clogin_page...1747056423476"
# }
# url = "https://login.dangdang.com/api/customer/loginapi/getSlidingVerifyCode"
# data = {
#     "t": "1747056423549",
#     "ct": "pc",
#     "permanent_id": "20250512210452215207919356244452060",
#     "requestId": "2505122104555730qkfDX0_ac96",
#     "situation": "login",
#     "sign": "/TmR2OJSzgleH6+2MKQFz5qY2AI510u9Jkbe83J11rz/S7cSeLAnsTAxI/TFCipk"
# }
# response = requests.post(url, headers=headers, cookies=cookies, data=data)
#
# print(response.text)
# print(response)
import cv2
import time
import json
import random
import base64
import ddddocr
import hashlib

import execjs
import requests
from loguru import logger
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
permanent_id = execjs.compile(open('test.js', 'r',encoding='utf-8').read()).call('G')
print(permanent_id)
def get_time_stamp():
    return int(time.time()) * 1000
import requests
url = "https://login.dangdang.com/api/customer/loginapi/getRankey"
# 校验 t -> {"statusCode":"1","errorCode":"1","errorMsg":"时间戳过期","requestId":null,"rankey":null}
data = {
    "t": get_time_stamp(),
    "permanent_id": permanent_id,
}
response = requests.post(url,
                         # headers=headers,
                        data=data
                        ).json()
print(response)