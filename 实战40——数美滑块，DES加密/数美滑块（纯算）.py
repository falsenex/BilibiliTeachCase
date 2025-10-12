#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import base64
import json
from Crypto.Cipher import DES
import datetime
import json
import os
import random
import string
import time
import cv2
import execjs
import requests
from loguru import logger


class ShuMeiSlide:
    """数美滑块验证码破解类"""

    def __init__(self, organization="d6tpAY1oV0Kv5jRSgxQr"):
        """
        初始化数美滑块验证码破解器

        Args:
            organization (str): 组织标识符，默认值为 "d6tpAY1oV0Kv5jRSgxQr"
        """
        self.organization = organization
        self.captchaUuid = None
        self.base_url = 'https://castatic.fengkongcloud.cn'
        self.headers = {
            "Accept": "*/*",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Origin": "https://www.ishumei.com",
            "Pragma": "no-cache",
            "Referer": "https://www.ishumei.com/trial/captcha.html",
            "Sec-Fetch-Dest": "script",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "cross-site",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36 Edg/139.0.0.0",
            "sec-ch-ua": "\"Not;A=Brand\";v=\"99\", \"Microsoft Edge\";v=\"139\", \"Chromium\";v=\"139\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\""
        }

    @staticmethod
    def des_encrypt(text, key):
        """
        DES加密计算

        Args:
            text: 要加密的文本或字典。可以是字符串或字典类型
            key (str): 加密密钥，DES要求密钥长度必须为8字节

        Returns:
            str: Base64编码的加密结果，方便传输和存储
        """
        # 1. 创建DES加密器实例
        # DES.new()用于创建加密器对象
        # 参数1: 密钥，必须转换为字节流，且长度固定为8字节
        # 参数2: 加密模式，这里使用ECB模式(电子密码本模式)
        # ECB模式是最简单的DES加密模式，将明文分成固定大小的块独立加密
        cipher = DES.new(key.encode('utf-8'), DES.MODE_ECB)

        # 2. 处理明文数据，统一转换为字节流
        if type(text) == str:
            # 如果输入是字符串，直接转换为字节流
            text = text.encode()
        else:
            # 如果输入是字典，先序列化为JSON字符串
            # separators参数移除多余空格，ensure_ascii=False确保中文正确处理
            # 最后再转换为字节流
            text = json.dumps(text, separators=(',', ':'), ensure_ascii=False).encode()

        # 3. 明文填充处理
        # DES算法要求明文必须是8字节的整数倍
        block_size = 8  # DES的块大小固定为8字节
        while len(text) % block_size:
            # 如果不是8的倍数，用空字节('\0')填充至8的倍数
            text += b'\0'

        # 4. 执行加密操作
        # cipher.encrypt()接收字节流，返回加密后的字节流
        encrypted_text = cipher.encrypt(text)

        # 5. 加密结果处理
        # 加密后的字节流无法直接作为文本处理，使用Base64编码转换为字符串
        # 便于在网络传输或存储时使用
        return base64.b64encode(encrypted_text).decode('utf-8')

    def generate_captcha_uuid(self):
        """生成验证码UUID"""
        self.captchaUuid = datetime.datetime.now().strftime("%Y%m%d%H%M%S") + ''.join(
            random.choice(string.ascii_letters + string.digits) for _ in range(18))
        return self.captchaUuid

    def get_img(self):
        """
        获取验证码图片信息

        Returns:
            dict: 包含背景图和滑块图信息的字典
        """
        if not self.captchaUuid:
            self.generate_captcha_uuid()

        url = "https://captcha1.fengkongcloud.cn/ca/v1/register"
        params = {
            "organization": self.organization,
            "captchaUuid": self.captchaUuid,
            "appId": "default",
            "data": "{}",
            "lang": "zh-cn",
            "model": "slide",
            "channel": "default",
            "rversion": "1.0.4",
            "callback": f"sm_{int(time.time() * 1000)}",
            "sdkver": "1.1.3"
        }
        response = requests.get(url, headers=self.headers, params=params)
        register_obj = json.loads(response.text[17:-1])
        logger.debug(register_obj)
        return register_obj['detail']

    def save_img(self, bg_url, slice_url):
        """
        保存验证码图片到本地

        Args:
            bg_url (str): 背景图片URL
            slice_url (str): 滑块图片URL
        """
        with open('bg.jpg', "wb") as f:
            f.write(requests.get(bg_url).content)
            f.close()
        with open('slice.png', "wb") as f1:
            f1.write(requests.get(slice_url).content)
            f1.close()
        logger.success('图片保存成功！！！')

    def identify_gap(self, bg, tp, out):
        """
        识别滑块缺口位置（备用方法）

        Args:
            bg (str): 背景图片路径
            tp (str): 缺口图片路径
            out (str): 输出图片路径

        Returns:
            int: 缺口的X坐标
        """
        # 读取背景图片和缺口图片
        bg_img = cv2.imread(bg)  # 背景图片
        tp_img = cv2.imread(tp)  # 缺口图片

        # 识别图片边缘
        bg_edge = cv2.Canny(bg_img, 100, 200)
        tp_edge = cv2.Canny(tp_img, 100, 200)

        # 转换图片格式
        bg_pic = cv2.cvtColor(bg_edge, cv2.COLOR_GRAY2RGB)
        tp_pic = cv2.cvtColor(tp_edge, cv2.COLOR_GRAY2RGB)

        # 缺口匹配
        res = cv2.matchTemplate(bg_pic, tp_pic, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)  # 寻找最优匹配

        # 绘制方框
        th, tw = tp_pic.shape[:2]
        tl = max_loc  # 左上角点的坐标
        br = (tl[0] + tw, tl[1] + th)  # 右下角点的坐标
        cv2.rectangle(bg_img, tl, br, (0, 0, 255), 2)  # 绘制矩形
        cv2.imwrite(out, bg_img)  # 保存在本地

        # 返回缺口的X坐标
        return tl[0]

    def get_slide_distance(self, bg_path, slide_path):
        """
        识别滑块具体位置

        Args:
            bg_path (str): 背景图片路径
            slide_path (str): 滑块图片路径

        Returns:
            int: 滑块位置的X坐标
        """
        bg_img = cv2.imread(bg_path)
        sd_img = cv2.imread(slide_path)
        bg_gray = cv2.cvtColor(bg_img, cv2.COLOR_BGR2GRAY)
        bg_gray = cv2.GaussianBlur(bg_gray, (5, 5), 0)
        bg_edge = cv2.Canny(bg_gray, 30, 100)
        rgb_bg_gray = cv2.cvtColor(bg_edge, cv2.COLOR_GRAY2RGB)

        sd_gray = cv2.cvtColor(sd_img, cv2.COLOR_BGR2GRAY)
        sd_gray = cv2.GaussianBlur(sd_gray, (5, 5), 0)
        sd_edge = cv2.Canny(sd_gray, 30, 100)
        rgb_sd_gray = cv2.cvtColor(sd_edge, cv2.COLOR_GRAY2RGB)
        result = cv2.matchTemplate(rgb_bg_gray, rgb_sd_gray, cv2.TM_CCORR_NORMED)
        _, _, _, max_loc = cv2.minMaxLoc(result)
        cv2.rectangle(bg_img, (max_loc[0], max_loc[1]), (max_loc[0] + 110, max_loc[1] + 110),
                      (0, 255, 0), 2)
        result_path = os.path.join(os.path.dirname(bg_path), "./result.png")
        cv2.imwrite(result_path, bg_img)
        return max_loc[0]

    def get_params(self, distance, track_list, passtime, register_data):
        """
        构建验证参数

        Args:
            distance (int): 滑动距离
            track_list (list): 轨迹数组
            passtime (int): 通过时间
            register_data (dict): 注册数据

        Returns:
            dict: 验证参数字典
        """
        # _0x12302b = "sshummei"
        _0x12c64a = distance  # 滑动距离
        _0x13468f = track_list  # 轨迹数组
        gg = self.des_encrypt(_0x12c64a / 300, "5129c2c2")
        hg = self.des_encrypt(_0x13468f, "be221ccf")
        th = self.des_encrypt(passtime, "231a540d")  # 时间差
        qt = self.des_encrypt(300, "38def2c1")
        lf = self.des_encrypt(150, "7a8c235d")
        fm = self.des_encrypt(1, "a571b7e5")
        sl = self.des_encrypt(0, "146ca9d6")
        bq = self.des_encrypt(-1, "177ad29c")
        ny = self.des_encrypt('default', "c9c6928e")
        to = self.des_encrypt('default', "539c5813")
        yh = self.des_encrypt("zh-cn", "727c3c8c")
        bs = self.des_encrypt("11", "2b301f03")
        rid = register_data['rid']
        rversion = "1.0.4"
        sdkver = "1.1.3"
        protocol = "185"
        ostype = "web"
        request_params = {
            "bs": bs,
            "yh": yh,
            "to": to,
            "rversion": rversion,
            "sdkver": sdkver,
            "ny": ny,
            "organization": self.organization,
            "rid": rid,
            "fm": fm,
            "qt": qt,
            "act.os": "web_pc",
            "lf": lf,
            "bq": bq,
            "captchaUuid": self.captchaUuid,
            "th": th,
            "gg": gg,
            "sl": sl,
            "callback": "sm_1757039518857",
            "protocol": protocol,
            "ostype": ostype,
            "hg": hg
        }
        logger.warning(request_params)
        return request_params

    def get_random_tracks(self, distance):
        """
        生成滑动轨迹

        Args:
            distance (int): 目标滑动距离

        Returns:
            list: 轨迹点列表，每个点包含[x, y, 时间]
        """
        tracks = []

        y = 0
        v = 0
        t = 1
        current = 0
        mid = distance * 3 / 4
        exceed = 20
        z = t

        tracks.append([0, 0, 1])

        while current < (distance + exceed):
            if current < mid / 2:
                a = 15
            elif current < mid:
                a = 20
            else:
                a = -30
            a /= 2
            v0 = v
            s = v0 * t + 0.5 * a * (t * t)
            current += int(s)
            v = v0 + a * t

            y += random.randint(-5, 5)
            z += 100 + random.randint(0, 10)

            tracks.append([min(current, (distance + exceed)), y, z])

        while exceed > 0:
            exceed -= random.randint(0, 5)
            y += random.randint(-5, 5)
            z += 100 + random.randint(0, 10)
            tracks.append([min(current, (distance + exceed)), y, z])

        return tracks

    def verify(self, distance, tracks, passtime, register_data):
        """
        提交验证请求

        Args:
            distance (int): 滑动距离
            tracks (list): 轨迹数据
            passtime (int): 通过时间
            register_data (dict): 注册数据

        Returns:
            bool: 验证是否成功
        """
        verify_headers = self.headers.copy()
        verify_headers["Referer"] = "https://www.ishumei.com/"

        url = "https://captcha1.fengkongcloud.cn/ca/v2/fverify"
        params = self.get_params(distance, tracks, passtime, register_data)
        response = requests.get(url, headers=verify_headers, params=params)
        logger.debug(f"验证结果: {response.text}")
        result = json.loads(response.text[17:-1])
        if result["riskLevel"] == 'PASS':
            logger.success('验证成功！！！')
            return True
        else:
            logger.error(result["riskLevel"])
            return False

    def run(self):
        """
        执行完整的验证码破解流程

        Returns:
            bool: 破解是否成功
        """
        try:
            # 生成验证码UUID
            self.generate_captcha_uuid()

            # 获取验证码图片信息
            img_detail = self.get_img()

            # 保存图片到本地
            self.save_img(self.base_url + img_detail['bg'], self.base_url + img_detail['fg'])

            # 计算滑动距离
            distance = self.get_slide_distance('bg.jpg', 'slice.png')
            distance = int(distance / 2)

            # 生成滑动轨迹
            tracks = self.get_random_tracks(distance)

            # 生成随机通过时间
            passtime = random.randint(1000, 1200)

            # 提交验证
            return self.verify(distance, tracks, passtime, img_detail)

        except Exception as e:
            logger.error(f"验证码破解过程中出现错误: {e}")
            return False


if __name__ == '__main__':
    # 创建数美滑块验证码破解器实例
    captcha_solver = ShuMeiSlide()

    # 执行10次验证码破解测试
    for i in range(10):
        logger.info(f"开始第 {i + 1} 次验证码破解...")
        success = captcha_solver.run()
        if success:
            logger.info(f"第 {i + 1} 次验证码破解成功")
        else:
            logger.info(f"第 {i + 1} 次验证码破解失败")

