import time
import random
import base64
import zlib
import ddddocr
import re
import json
import hashlib
import gzip
from urllib.parse import quote
from curl_cffi import requests
from loguru import logger
from Crypto.Cipher import AES
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
from Crypto.Util.Padding import pad
import uuid


class CSdnSlider:
    def __init__(self):
        self.headers = {
            "Accept": "text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Pragma": "no-cache",
            "Referer": "https://passport.csdn.net/login?code=applets",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; JiSu) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.3.1.7 Safari/537.36",
            "X-Req-Token": "1c143bd3c9d257735d840bd81ce06f28",
            "X-Requested-With": "XMLHttpRequest"
        }
        
        # RSA公钥
        self.public_key = """-----BEGIN PUBLIC KEY-----
                MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCaaTUpL2aaZMcf3xluTrCga+WF
                2H9n/yKVAugdGJfTfvkCaGxX5HM16rgvHrsmiveAQYBEUkWN5mIJuM6bZS/tltzy
                Kaykrfj/uM1ayyU51NGyH//t3PhZpDb6For00DadsNSyBlh5WFcxc9ufNODC88Fw
                gD7adZD/yxSk/mAvRwIDAQAB
                -----END PUBLIC KEY-----"""
        
        # 初始化保护对象
        self.captcha_protect_data = {
            "name": "captcha_protect",
            "clickTimes": 0,
            "moveTimes": 0,
            "touchTimes": 0,
            "start_time": int(time.time() * 1000),
            "clickArr": [],
            "iswebdriver": False,
            "isphantom": False,
            "iscallPhantom": False,
            "ischrome": True,
            "outerWidth": 1536,
            "outerHeight": 824,
            "innerWidth": 410,
            "innerHeight": 566,
            "fpv": self.guid2(),
            "isMobile": False,
            "location_host": 'passport.csdn.net',
            "userAgent": 'Mozilla/5.0 (Windows NT 10.0; JiSu) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.3.1.7 Safari/537.36',
            "iscookieEnabled": True
        }
        
        self.wlocation = {
            "host": "passport.csdn.net",
            "href": "https://passport.csdn.net/login?code=applets",
            "userAgent": "Mozilla/5.0 (Windows NT 10.0; JiSu) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.3.1.7 Safari/537.36",
            "platform": "Win32",
            "language": "zh-CN",
            "time": int(time.time() * 1000)
        }

    def guid2(self):
        """生成32位十六进制字符串"""
        def hex_part():
            return hex(int((1 + random.random()) * 65536))[3:]
        
        return ''.join([hex_part() for _ in range(8)])

    def signature(self):
        """生成签名"""
        guid_16 = self.guid2()[:16]
        md5_hash = hashlib.md5((guid_16 + "shyundun").encode()).hexdigest()[:16]
        return guid_16 + md5_hash

    def guid(self):
        """生成带连字符的GUID"""
        def hex_part():
            return hex(int((1 + random.random()) * 65536))[3:]
        
        return f"{hex_part()}{hex_part()}-{hex_part()}-{hex_part()}-{hex_part()}-{hex_part()}{hex_part()}{hex_part()}"

    def rsa_encrypt(self, text):
        """RSA加密"""
        rsa_key = RSA.import_key(self.public_key)
        cipher = PKCS1_v1_5.new(rsa_key)
        encrypted = cipher.encrypt(text.encode('utf-8'))
        return base64.b64encode(encrypted).decode('utf-8')

    def aes_encrypt(self, text, key, iv):
        """AES加密"""
        cipher = AES.new(key.encode('utf-8'), AES.MODE_CBC, iv.encode('utf-8'))
        padded_text = pad(text.encode('utf-8'), AES.block_size)
        encrypted = cipher.encrypt(padded_text)
        return base64.b64encode(encrypted).decode('utf-8')

    def aes_encrypt_key(self, fpv, data):
        """使用密钥的AES加密"""
        md5_hash = hashlib.md5(fpv.encode()).hexdigest()
        key = md5_hash[:16]
        iv = md5_hash[16:]
        return self.aes_encrypt(data, key, iv)

    def aes_encrypt_fpv(self, fpv_all, data):
        """使用fpv的AES加密"""
        md5_hash = hashlib.md5(fpv_all.encode()).hexdigest()
        key = md5_hash[:16]
        iv = md5_hash[16:]
        return self.aes_encrypt(data, key, iv)

    def gzip_compress(self, data):
        """gzip压缩并base64编码"""
        if isinstance(data, str):
            data = data.encode('utf-8')
        compressed = gzip.compress(data)
        return base64.b64encode(compressed).decode('utf-8')

    def captcha_protect(self):
        """生成captcha_protect参数"""
        self.captcha_protect_data["end_time"] = int(time.time() * 1000)
        self.captcha_protect_data["guid"] = self.guid()
        
        md5_input = f"{self.captcha_protect_data['name']}_{self.captcha_protect_data['fpv']}"
        md5_hash = hashlib.md5(md5_input.encode()).hexdigest()
        
        rsa_encrypted = self.rsa_encrypt(md5_hash)
        aes_encrypted = self.aes_encrypt_key(md5_hash, json.dumps(self.captcha_protect_data))
        
        combined = rsa_encrypted + "captcha_protect" + aes_encrypted
        return quote(self.gzip_compress(combined))

    def get_params(self):
        """获取验证码请求参数"""
        return {
            'captcha_protect': self.captcha_protect(),
            'fpv': self.gzip_compress(self.captcha_protect_data['fpv']),
            'isUpgrade': 'false',
            'type': self.gzip_compress('slide_pic'),
            'wlocation': self.gzip_compress(json.dumps(self.wlocation)),
            'fpv_all': self.captcha_protect_data['fpv'],
            'Token': self.signature()
        }

    def get_verify_params(self, fpv_all, data_slide):
        """获取验证参数"""
        return {
            'captcha_protect': self.captcha_protect(),
            'body': self.aes_encrypt_fpv(fpv_all, self.gzip_compress(json.dumps(data_slide))),
            'fpv': self.rsa_encrypt(fpv_all),
            'isUpgrade': 'false',
            'refreshTimes': '0',
            'type': 'slide',
            'wlocation': self.gzip_compress(json.dumps(self.wlocation)),
            'Token': self.signature()
        }

    def jys_data(self, gzip_str):
        """解压gzip数据"""
        gzip_data = base64.b64decode(gzip_str)
        uncompressed_data = zlib.decompress(gzip_data, zlib.MAX_WBITS | 16).decode('utf-8')
        return uncompressed_data

    def generate_slide_track(self, distance, start_x=100, base_y=375, total_time=3000):
        """
        生成滑块滑动轨迹数组
        :param distance: 滑动总距离（像素）
        :param start_x: 起始x坐标（默认100）
        :param base_y: 基础y坐标（默认375，模拟轻微抖动）
        :param total_time: 总滑动时间（毫秒，默认3000ms）
        :return: 轨迹数组
        """
        track = []
        current_x = start_x
        end_x = start_x + distance  # 目标结束x坐标
        current_time = int(time.time() * 1000)  # 起始时间戳（毫秒）
        elapsed_time = 0  # 已消耗时间（毫秒）

        # 第一阶段：初始点（t=1）
        track.append({
            "x": current_x,
            "y": base_y + random.randint(-1, 1),  # 轻微初始抖动
            "t": 1,
            "time": current_time
        })

        # 轨迹分段（模拟人手滑动规律：加速→匀速→减速→微调）
        # 1. 加速阶段（占总距离30%，时间25%）
        accelerate_dist = int(distance * 0.3)
        accelerate_time = int(total_time * 0.25)
        # 2. 匀速阶段（占总距离50%，时间40%）
        uniform_dist = int(distance * 0.5)
        uniform_time = int(total_time * 0.4)
        # 3. 减速阶段（占总距离15%，时间25%）
        decelerate_dist = int(distance * 0.15)
        decelerate_time = int(total_time * 0.25)
        # 4. 微调阶段（剩余距离，剩余时间）
        adjust_dist = distance - (accelerate_dist + uniform_dist + decelerate_dist)
        adjust_time = total_time - (accelerate_time + uniform_time + decelerate_time)

        # 生成各阶段轨迹点
        stages = [
            ("accelerate", accelerate_dist, accelerate_time, 1, 3),  # 阶段名、距离、时间、最小步长、最大步长
            ("uniform", uniform_dist, uniform_time, 2, 4),
            ("decelerate", decelerate_dist, decelerate_time, 1, 2),
            ("adjust", adjust_dist, adjust_time, 0, 1)  # 微调可能有0步长（停顿）
        ]

        for stage_name, stage_dist, stage_time, min_step, max_step in stages:
            if stage_dist <= 0 or stage_time <= 0:
                continue

            # 计算阶段内的点数量（至少2个点）
            points_count = max(2, int(stage_time / 10))  # 平均每10ms一个点
            step_dist_list = []
            remaining_dist = stage_dist
            remaining_points = points_count

            # 分配每个点的x增量（保证总和为stage_dist）
            for i in range(points_count - 1):
                # 步长随阶段变化：加速阶段步长递增，减速阶段步长递减
                if stage_name == "accelerate":
                    step = min(max_step, min_step + (max_step - min_step) * (i / points_count))
                elif stage_name == "decelerate":
                    step = max(min_step, max_step - (max_step - min_step) * (i / points_count))
                else:  # uniform/adjust
                    step = random.uniform(min_step, max_step)

                step = int(step)
                step = min(step, remaining_dist - (remaining_points - i - 1) * min_step)  # 避免超量
                step_dist_list.append(step)
                remaining_dist -= step
                remaining_points -= 1
            step_dist_list.append(remaining_dist)  # 最后一个点补全剩余距离

            # 分配每个点的时间间隔（总和为stage_time）
            interval_list = []
            remaining_time = stage_time
            remaining_points = points_count
            for i in range(points_count - 1):
                # 时间间隔：加速阶段小，减速阶段大
                if stage_name == "accelerate":
                    interval = random.randint(5, 15)
                elif stage_name == "decelerate":
                    interval = random.randint(15, 30)
                elif stage_name == "adjust":
                    interval = random.randint(50, 200)  # 微调阶段停顿更长
                else:  # uniform
                    interval = random.randint(10, 20)

                interval = min(interval, remaining_time - (remaining_points - i - 1) * 5)  # 避免超量
                interval_list.append(interval)
                remaining_time -= interval
                remaining_points -= 1
            interval_list.append(remaining_time)

            # 生成阶段内的轨迹点
            for step, interval in zip(step_dist_list, interval_list):
                current_x += step
                # y轴轻微抖动（±1~2像素）
                current_y = base_y + random.randint(-2, 2)
                # 确保y值在合理范围（避免抖动过大）
                current_y = max(370, min(385, current_y))
                elapsed_time += interval
                track.append({
                    "x": current_x,
                    "y": current_y,
                    "t": 2,  # 滑动过程中t=2
                    "time": interval  # 间隔时间（毫秒）
                })

        # 最后阶段：结束点（t=3）
        end_time = current_time + elapsed_time
        track.append({
            "x": end_x,
            "y": base_y + random.randint(-1, 1),  # 回归基础y值
            "t": 3,
            "time": end_time
        })

        return track

    def get_cookie(self):
        """获取CSDN网站的cookies"""
        url = "https://passport.csdn.net/login"
        params = {
            "code": "applets"
        }
        response = requests.get(url, headers=self.headers, params=params)
        cookies = response.cookies.get_dict()
        return cookies

    def get_yzm(self, cookies):
        """获取验证码信息"""
        url = "https://passport.csdn.net/cdn_cgi_bs_captcha/convert"
        params = {
            "callback": f"callback_{int(time.time()*1000)}",
            "_": f"{int(time.time()*1000) - random.randint(20,50)}"
        }
        
        # 获取参数
        params_v = self.get_params()
        # 拿到全局的fpv相当于令牌
        fpv_all = params_v.pop('fpv_all')
        x_req_token = params_v.pop('Token')
        # 更新headers Token
        self.headers['X-Req-Token'] = x_req_token
        params = dict(params, **params_v)
        
        response = requests.get(url, headers=self.headers, cookies=cookies, params=params, impersonate='chrome101')
        # logger.debug(f'获取滑块信息gzip:{response.text}')
        body = re.findall('"body":"(.*?)"', response.text)[0]
        config_data = self.jys_data(body)
        config_data = json.loads(config_data)
        logger.success(f'解压缩结果:{config_data}')
        return config_data, fpv_all

    def get_distance(self, config_data, cookies):
        """计算滑块距离"""
        background_img = requests.get('https://passport.csdn.net' + config_data['background'], headers=self.headers, cookies=cookies).content
        targetImage = requests.get('https://passport.csdn.net' + config_data['targetImage'], headers=self.headers, cookies=cookies).content
        slide = ddddocr.DdddOcr(show_ad=False)
        res = slide.slide_match(background_img, targetImage, simple_target=True)
        distance = res.get('target')[0]
        logger.success(f'缺口距离:{distance}')
        return distance

    def verify(self, distance, fpv_all, cookies, config_data):
        """执行滑块验证"""
        logger.critical(f"轨迹：{self.generate_slide_track(distance)}")
        data_sliend = {
            "tracks": self.generate_slide_track(distance),
            "params": {
                "moveblockleft": distance,
                "randomKey": config_data['randomKey']
            }
        }
        
        data = self.get_verify_params(fpv_all, data_sliend)
        x_req_token = data.pop('Token')
        url = "https://passport.csdn.net/cdn_cgi_bs_captcha/verify"
        params = {
            "callback": f"callback_{int(time.time()*1000)}"
        }
        self.headers['X-Req-Token'] = x_req_token
        response = requests.post(url, headers=self.headers, cookies=cookies, params=params, data=data)
        logger.success(f'CSDN验证滑块验证结果:{response.text}')
        return response.text

    def run(self):
        """主函数"""
        try:
            cookies = self.get_cookie()
            config_data, fpv_all = self.get_yzm(cookies)
            distance = self.get_distance(config_data, cookies)
            result = self.verify(distance, fpv_all, cookies, config_data)
            return result
        except Exception as e:
            logger.error(f"运行出错: {e}")
            return None


if __name__ == '__main__':
    slider = CSdnSlider()
    slider.run()
