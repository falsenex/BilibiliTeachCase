#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：pythonProject 
@File    ：demo.py
@IDE     ：PyCharm 
@Author  ：haozaispider
@Date    ：2025/6/20 下午3:47 
'''
import execjs
import requests

def get_public_key():
    headers = {
        "Accept": "*/*",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Origin": "https://login.189.cn",
        "Pragma": "no-cache",
        "Referer": "https://login.189.cn/web/login",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
        "sec-ch-ua": "\"Google Chrome\";v=\"137\", \"Chromium\";v=\"137\", \"Not/A)Brand\";v=\"24\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\""
    }
    cookies = {
        "JSESSIONID": "D491050C496251088D4655289E348725",
        "U4r4xthJCQN5O": "60HZt5Kfa8uuXCgGHg88k2HVeU1crTZDRIsFzzyYMQtM2kZsuRhkjoCFIV8T.KjWEDpr0105lBgaCpiePOaHV_1A",
        "sajssdk_2015_cross_new_user": "1",
        "zhizhendata2015jssdkcross": "%7B%22distinct_id%22%3A%22MTk3OWJiMTc1ZmU4OWEtMDg4Yzc3NjU3Y2E5ZjctMjYwMTFlNTEtMjA3MzYwMC0xOTc5YmIxNzVmZjIzNWY%3D%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22login_type%22%3A%22%22%2C%22utms%22%3A%7B%7D%2C%22%24device_id%22%3A%221979bb175fe89a-088c77657ca9f7-26011e51-2073600-1979bb175ff235f%22%7D",
        "ECS_ReqInfo_login1": "U2FsdGVkX1%2Bt3I5YYHHrlovJR8OWCUf73WRe8IzV%2Bs6UTOOteyr4bM8YIst%2B2%2BJgWDiqQKojyOBwgbI8UnTKBQ%3D%3D",
        "EcsCaptchaKey": "4rOaQgq1uOY9GB24jRRbR3vcN1XKpJroJzsoQykafYbXe8QHyt6v1A%3D%3D",
        "U4r4xthJCQN5P": "06rkBGOs3zn_dgMtz6YJVj0HNsNCYaC80W4hwtqz002RRPxb.2D3mI_pwNgvNdJaY0hSgW7P4yUdQHVZSW3RSu9rhFV7751lM0anQKCMYa.P88w86l9OpSQ6lztI90mWtXMM49SKoZItVSKiiWqSISFcVxysBoCVS5GOqkfB5dLNHz9Xc7ydnjM..tJusVSw9aKwAd0nzxhJkOH4G1nj83HxPlhsOkge7F_yUaHzX6jxm4bKp0AVGmMGt0XEUbrbpyGr8BDSh1gWFa_IkmIiXrSuNH2eqRjGAhGV8Cq31DGiBiOaT35J3FA.KRbkeDrIw.7wr25d190jb8szGABmjhhdDmvqw8vrfn6_2qWukFaifq3SZW.VNeed8eqpVTonLVu4YfWyYmBKB5.F.N05359HPfbDYUva3lNw1PwHV9.a_COGVouW8EIDBiUU9moebd0scmF6_cATahd3ciEvRjG"
    }
    url = "https://login.189.cn/web/login/ajax"
    data = {
        "m": "getPubKey"
    }
    response = requests.post(url, headers=headers, cookies=cookies, data=data)
    return response.text
headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://login.189.cn",
    "Pragma": "no-cache",
    "Referer": "https://login.189.cn/web/login",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest",
    "sec-ch-ua": "\"Google Chrome\";v=\"137\", \"Chromium\";v=\"137\", \"Not/A)Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\""
}
cookies = {
    "JSESSIONID": "D491050C496251088D4655289E348725",
    "U4r4xthJCQN5O": "60HZt5Kfa8uuXCgGHg88k2HVeU1crTZDRIsFzzyYMQtM2kZsuRhkjoCFIV8T.KjWEDpr0105lBgaCpiePOaHV_1A",
    "sajssdk_2015_cross_new_user": "1",
    "zhizhendata2015jssdkcross": "%7B%22distinct_id%22%3A%22MTk3OWJiMTc1ZmU4OWEtMDg4Yzc3NjU3Y2E5ZjctMjYwMTFlNTEtMjA3MzYwMC0xOTc5YmIxNzVmZjIzNWY%3D%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22login_type%22%3A%22%22%2C%22utms%22%3A%7B%7D%2C%22%24device_id%22%3A%221979bb175fe89a-088c77657ca9f7-26011e51-2073600-1979bb175ff235f%22%7D",
    "ECS_ReqInfo_login1": "U2FsdGVkX1%2Bt3I5YYHHrlovJR8OWCUf73WRe8IzV%2Bs6UTOOteyr4bM8YIst%2B2%2BJgWDiqQKojyOBwgbI8UnTKBQ%3D%3D",
    "EcsCaptchaKey": "4rOaQgq1uOY9GB24jRRbR3vcN1XKpJroJzsoQykafYbXe8QHyt6v1A%3D%3D",
    "U4r4xthJCQN5P": "0Rq7OX3pi.v1qbD.rURE17PMgMelmJnHF9ryGDaOyq4AINSZ.ifIvUTU2cuAWrePq6gAdojlBWB7UvSSVA3TvgDJZbx0h60rdlvJbiFqHBvxCVBVklsWZ896mvabKdid2RtOy_dkap7FPwU1pnfGXiJzKkN_OesiOK9Uwp3ALcEMOpK2tHoOA_yQJHTJtOC1v8ftdhxgLwT110efu4lAT73Cf.EASPJW5Sq2umseP5cZrh62KR05IZkoP1IUzPWkXV30GJab68L0C1PMGk6DOELpIayzEHV.bgJpe8bplCDOaXHIn52klaayuulS6asZu7M8JAnDHoFKQvRpRHT7d0lkmyDiJu1v56_6ta0ABsigu3QEvqjaFkIj1gQIW3tvcxg00I_lBDklUCJp2xnoS.jAb.ZcmcUCfLIWoouBzbc1zEMxIC0.fJRWrYJk67yxkXd9pUicdXct13glLcp4nQa"
}
url = "https://login.189.cn/web/pwd/validate"
public_key = get_public_key()
uPwd = execjs.compile(open('demo.js', 'r',encoding='utf-8').read()).call('get_pwd', 'xxoo123456', public_key)
data = {
    "uName": "12140545349",
    "uType": "203",
    # "uPwd": "042145fb9910519041d29e20902b786f4282f4e9b896032b370ed86e6bd4bf0831200e39d77259e6186e0e1ce5f9fb8c5c4d511e48bb64f20d769862c3dc786995365c5fe30a620ba09661d1275fc401b7ddef31f60e49cff7e3877c055d8d1cc0d7367ac1e9dcafe1af8bef6471151c6c",
    "isRandomPwd": "false"
}
data["uPwd"] = uPwd
response = requests.post(url, headers=headers, cookies=cookies, data=data)

print(response.text)
print(response)