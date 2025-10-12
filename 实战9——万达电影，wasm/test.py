import requests


headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "keep-alive",
    "MX-API": "{\"ver\":\"7.0.0\",\"sCode\":\"Wanda\",\"_mi_\":\"\",\"width\":1280,\"json\":true,\"cCode\":\"1_3\",\"check\":\"e09b9c3d2aaa90acd347883a3ecd5e75\",\"ts\":1744637832432,\"heigth\":720,\"appId\":\"3\"}",
    "Origin": "https://m.wandacinemas.com",
    "Referer": "https://m.wandacinemas.com/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-Storage-Access": "active",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
    "sec-ch-ua": "\"Google Chrome\";v=\"135\", \"Not-A.Brand\";v=\"8\", \"Chromium\";v=\"135\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\""
}
url = "https://cinema-api-prd-mx.wandafilm.com/movie/coming.api"
params = {
    "cityId": "354",
    "cinemaId": "651",
    "day": "0"
}
response = requests.get(url, headers=headers, params=params)

print(response.text)
print(response)