from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import base64
import urllib
import execjs
import requests
from loguru import logger
def aes_cbc_encrypt(plaintext, key, iv):
    try:
        # 将密钥和IV转换为字节
        key_bytes = key.encode('utf-8')
        iv_bytes = iv.encode('utf-8')
        plaintext_bytes = plaintext.encode('utf-8')

        # 创建AES加密器，使用CBC模式
        cipher = AES.new(key_bytes, AES.MODE_CBC, iv_bytes)

        # 对明文进行PKCS#7填充并加密
        padded_data = pad(plaintext_bytes, AES.block_size)
        encrypted_bytes = cipher.encrypt(padded_data)

        # 将加密结果进行Base64编码并返回字符串
        return base64.b64encode(encrypted_bytes).decode('utf-8')
    except Exception as e:
        print(f'加密失败: {e}')
        raise e
def get_passwd(mima):
    key = 'e10adc3949ba59ab'
    iv = 'be56e057f20f883e'
    return aes_cbc_encrypt(mima, key, iv)
def get_a(arg):
    key = 'f9357bdd0069fbcd'
    iv = '014d15ef427ff4f7'
    return aes_cbc_encrypt(arg, key, iv)
def login(username, password):
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded",
        "Origin": "https://sltrczx.scslrc.cn",
        "Referer": "https://sltrczx.scslrc.cn/web/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36",
        "X-Authorization;": "",
        "osTenantId": "2ad7bce569694baabe8ee27797ee23ee",
        "sec-ch-ua": "\"Google Chrome\";v=\"137\", \"Chromium\";v=\"137\", \"Not/A)Brand\";v=\"24\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\""
    }
    cookies = {
        "HWWAFSESID": "d508d7377ea73195be",
        "HWWAFSESTIME": "1753950904518",
        "_webtracing_session_id": "s_135006b7-a6d33490-074b1a979354cdc5"
    }
    url = "https://sltrczx.scslrc.cn/authority/sysViewLoginApi/viewUserNameLoginaes"
    passwordeasy = get_passwd(password)
    logger.debug(f"加密密码:{passwordeasy}")
    a_mingwen = {
        "type": "0",
        "username": username,
        "passwordeasy": passwordeasy,
        "osTenantId": "2ad7bce569694baabe8ee27797ee23ee"
    }
    '''
    urllib.parse.quote(string, safe='/', encoding=None, errors=None)
    作用：将字符串转换为 URL 安全的编码格式（也称为 "URL 编码" 或 "百分号编码"）。
    原理：将字符串中不符合 URL 规范的字符（如中文、空格、&、? 等）转换为 %XX 形式的十六进制表示（XX 为字符的 ASCII 码或 Unicode 码）。
    参数说明：
    string：需要编码的字符串。
    safe：指定不需要编码的字符（默认包含 /，因为 URL 中的路径分隔符通常不需要编码）。
    encoding 和 errors：指定编码方式和错误处理方式（默认使用 utf-8 编码）。
    
    
    
    urllib.parse.urlencode(query, doseq=False, safe='', encoding=None, errors=None, quote_via=quote_plus)
    作用：将字典或包含键值对的序列转换为 URL 查询字符串（即 key1=value1&key2=value2 形式），并自动对键和值进行 URL 编码。
    适用场景：常用于构造 GET 请求的查询参数部分。
    参数说明：
    query：字典或由 (key, value) 元组组成的序列。
    doseq：如果为 True，则当值为列表时，会将每个元素展开为单独的键值对（如 {'a': [1,2]} 会转为 a=1&a=2）。
    quote_via：指定编码方式（默认 quote_plus，会将空格转为 +；若用 quote，空格会转为 %20）。
    '''

    a = get_a(urllib.parse.urlencode(a_mingwen))
    logger.debug(f"生成的a:{a_mingwen}")
    data = {
        "a":a
        # "a": "+tlpM+1tbH1HKXHpJKEUjLttmo9p/E97lIJVr/zYuW7ruCGSaJpDf0l15Qf0KrUr+AvVHQPP9++fMS8ldSIAPH4mswGQfs8HpWHDj/ebnSE1hhK+vvvw4sku0T9gkrBxNSDTDEyzjLk07z6eJUWdx338ia8nHHNdAe4png80jz0="
    }
    response = requests.post(url, headers=headers, cookies=cookies, data=data)
    logger.info(response)
    logger.success(response.text)
if __name__ == '__main__':
    username = '12140545349'
    password = "xxoo123456"
    login(username, password)
