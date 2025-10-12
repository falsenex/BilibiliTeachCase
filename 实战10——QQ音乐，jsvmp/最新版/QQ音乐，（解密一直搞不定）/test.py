import base64
import requests

cookies = {
    'ts_refer': 'cn.bing.com/',
    'ts_uid': '9834888193',
    'pgv_pvid': '4614023088',
    'fqm_pvqid': 'b0ecafa7-a2aa-4429-a8e8-4d38be610dde',
    'fqm_sessionid': '4df9817b-dc10-4902-917d-62e3cd905816',
    'pgv_info': 'ssid=s4044287357',
}

headers = {
    'accept': 'application/octet-stream',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'cache-control': 'no-cache',
    'content-type': 'text/plain',
    'origin': 'https://y.qq.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://y.qq.com/',
    'sec-ch-ua': '"Not;A=Brand";v="99", "Microsoft Edge";v="139", "Chromium";v="139"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36 Edg/139.0.0.0',
    # 'cookie': 'ts_refer=cn.bing.com/; ts_uid=9834888193; pgv_pvid=4614023088; fqm_pvqid=b0ecafa7-a2aa-4429-a8e8-4d38be610dde; fqm_sessionid=4df9817b-dc10-4902-917d-62e3cd905816; pgv_info=ssid=s4044287357',
}

params = {
    '_': '1754991072327',
    'encoding': 'ag-1',
    'sign': 'zzc50e04d3pzb2e9lscjlyedxcq32r0ebq44e33705',
}

data = '/iLuw0O49zlCT5opIn99755OHKWNHLEF5JE6v+dXjwPgRO+MzeqGmqRg8hiPcu1Qbo89kX26IaYxwrsorLhya07KEacTdWyST7HJiRdUM7JbDQjxN9wkrp/EE3Z5qWzWMW6wogay9JRTjY177FRC5x5CTGmyHXKQnrdFxT1+/aSUgDztM/8RU4TKrk6tkVO/sk0tqLOjNS24jJwMRTE3j+ksv9xDP2jDZpeNt43I8ks2d0CZbWgXtD/6z8kHREiHr4coah5hoGZnEm32O4JZIGDXUL8ZYE39OC4ctSlv0npJa7Js0qb9rdnyKfDYR+aX4OIV5L0mwgcdcU8h08FguL4ajrHd2ct3bDrGRVmXcGFKEaZqLV95YgN7yOnCowryxqj2sYjZa3FwP5cwDtkOzR8CAs1CNt+SFQLTPq66Do58Rys/cHPIzBYtc8RXkVe6V5XNt8R82cqjlw=='

response = requests.post('https://u6.y.qq.com/cgi-bin/musics.fcg', params=params, cookies=cookies, headers=headers, data=data)
print(base64.b64encode(response.content).decode('utf-8'))