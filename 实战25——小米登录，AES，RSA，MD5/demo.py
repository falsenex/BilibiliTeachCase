#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：pythonProject 
@File    ：demo.py
@IDE     ：PyCharm 
@Author  ：haozaispider
@Date    ：2025/6/30 上午11:42 
'''
import execjs
import requests


headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    # "EUI": "eAgpuLO74fU8n+/NO8uoNiv+KcbPyi8EbcTDlFlN2+hmFsKpJXNgI/YTgLy7HVpc5z0agtQsXWXYMvNfm0sFUVo76yS8/4GB0Ajj7CsePG4076kHxC3znlwIhkhLhVT2icQKr5YLTBYdsPGhEXynzDqLs4fTVBR5vmZcLV37svk=.dXNlcg==",
    "Origin": "https://account.xiaomi.com",
    "Pragma": "no-cache",
    "Referer": "https://account.xiaomi.com/fe/service/login/password?_locale=zh_CN&sid=passport&qs=%253F_locale%253Dzh_CN&callback=https%3A%2F%2Faccount.xiaomi.com&_sign=2%26V1_passport%26x0slRayyS8cW7cG2GEXdLdeYk6A%3D&serviceParam=%7B%22checkSafePhone%22%3Afalse%2C%22checkSafeAddress%22%3Afalse%2C%22lsrp_score%22%3A0.0%7D&showActiveX=false&theme=&needTheme=false&bizDeviceType=",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0",
    "X-Requested-With": "XMLHttpRequest",
    "sec-ch-ua": "\"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"138\", \"Microsoft Edge\";v=\"138\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\""
}
cookies = {
    "deviceId": "wb_993675ec-cd35-447b-af57-9f82e32fc8c9",
    "pass_ua": "web",
    "uLocale": "zh_CN"
}
url = "https://account.xiaomi.com/pass/serviceLoginAuth2"

data = {
    "bizDeviceType": "",
    "needTheme": "false",
    "theme": "",
    "showActiveX": "false",
    "serviceParam": "{\"checkSafePhone\":false,\"checkSafeAddress\":false,\"lsrp_score\":0.0}",
    "callback": "https://account.xiaomi.com",
    "qs": "%3F_locale%3Dzh_CN",
    "sid": "passport",
    "_sign": "2&V1_passport&x0slRayyS8cW7cG2GEXdLdeYk6A=",
    # "user": "TNz53jhQANxiWH64u4M0Og==",
    "cc": "+86",
    # "hash": "CB0495E9A9B008C797261E9BA4B5228F",
    "_json": "true",
    "policyName": "miaccount",
    "captCode": ""
}
paras = execjs.compile(open('demo.js', 'r', encoding='utf-8').read()).call('get_paras',{"user": "12140545349"})
hash = execjs.compile(open('demo.js', 'r', encoding='utf-8').read()).call('get_passwd','xxoo123456')
data["user"] = paras["encryptedParams"]["user"]
data["hash"] = hash
headers["EUI"] = paras["EUI"]
response = requests.post(url, headers=headers, cookies=cookies, data=data)
print(response.text)
print(response)
