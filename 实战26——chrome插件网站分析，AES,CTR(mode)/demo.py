import execjs
import requests
import json


headers = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "no-cache",
    "content-type": "application/json; charset=UTF-8",
    "origin": "https://www.crxsoso.com",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://www.crxsoso.com/",
    "sec-ch-ua": "\"Google Chrome\";v=\"137\", \"Chromium\";v=\"137\", \"Not/A)Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36"
}
url = "https://api.crxsoso.com/chrome/category"
data_obj = {
    "name": "productivity-workflow",
    "size": 48
}
data_str = execjs.compile(open('demo.js', 'r',encoding='utf-8').read()).call('get_data',data_obj)
data = {
    "data": data_str
}
data = json.dumps(data, separators=(',', ':'))
response = requests.post(url, headers=headers, data=data)

print(response.text)
print(response)