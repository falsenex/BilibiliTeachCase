import requests
import execjs
url = "https://api.weibotop.cn/currentitems"
resp = requests.get(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                                         "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"})
mi_str = resp.text
print(mi_str)#mi_str
file_object = open("wbth.js", mode="r")
exec_code = file_object.read()

exec_js = execjs.compile(exec_code)
call = exec_js.call("h", mi_str)
print(call)
