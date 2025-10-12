import base64
import io
import random

import ddddocr
import execjs
from PIL import Image
from loguru import logger
from requests import Session
session = Session()
def slider1(gap_img,sl_img):
    det = ddddocr.DdddOcr(det=True, ocr=True)
    with open(sl_img, 'rb') as f:
        target_bytes = f.read()
    with open(gap_img, 'rb') as f:
        background_bytes = f.read()
    res = det.slide_match(target_bytes, background_bytes)
    print(res)
    return res['target'][0]

def get_loginId(length=32, base=16):
    characters = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    available_chars = characters[:base]  # Select characters based on the base

    if length:
        return ''.join(random.choice(available_chars) for _ in range(length))
    else:
        # Emulate the GUID/UUID logic from the JavaScript code (if length is 0)
        o = [None] * 36
        o[8] = o[13] = o[18] = o[23] = "-"
        o[14] = "4"
        for e in range(36):
            if o[e] is None:
                n = random.randint(0, 15)  # Equivalent to 0 | 16 * Math.random()
                if e == 19:
                    n = (n & 0x3) | 0x8  # Equivalent to 3 & n | 8 (forces version to 4 and variant to RFC4122)
                o[e] = characters[n]  # use full character set to allow hex + more
        return ''.join(o)
def get_slide_img(loginId):
    url = "https://m.ctyun.cn/alogic-ctyun/user/SlideVerify"
    data = {
        "loginId": loginId,
    }
    response = session.post(url, data=data)
    print(response.json())
    return response.json()
def paste_image_on_background(small_image_path, output_path, top, background_color=(0, 0, 0, 0)):
    """
    将一个61×61的PNG图片粘贴到一个61×200的背景图上，小图片距离背景图上边框67像素，保留透明通道。

    参数:
    small_image_path (str): 小图片的路径
    output_path (str): 输出图片的路径
    background_color (tuple): 背景图的颜色，默认为白色 (R, G, B, A)
    """
    # 打开小图片，确保包含Alpha通道
    try:
        small_img = Image.open(small_image_path).convert("RGBA")
    except Exception as e:
        logger.error(f"打开图片失败: {e}")
        return False

    # 确保小图片尺寸是61×61
    if small_img.size != (50, 50):
        logger.warning(f"警告: 小图片尺寸不是61×61，当前尺寸为{small_img.size}，将尝试调整大小。")
        small_img = small_img.resize((50, 50), Image.Resampling.LANCZOS)

    # 创建新的带透明通道的背景图
    background = Image.new('RGBA', (50, 200), background_color)

    # 计算粘贴位置（距离上边框XX像素）
    position = (0, top)  # (left, top)

    # 粘贴小图片到背景图上，保留透明通道
    background.paste(small_img, position, small_img)

    # 保存结果，确保保存为PNG格式以保留透明通道
    try:
        if not output_path.lower().endswith('.png'):
            output_path += '.png'
        background.save(output_path, "PNG")
        logger.success(f"图片已成功保存到: {output_path}")
        return True
    except Exception as e:
        logger.error(f"保存图片失败: {e}")
        return False
def get_distance(img_json):
    original_image_data = base64.b64decode(img_json["data"]["shadeImage"])
    original_image = Image.open(io.BytesIO(original_image_data))
    original_image.save("bg.png")
    # 还原拼图图片
    jigsaw_image_data = base64.b64decode(img_json["data"]["cutoutImage"])
    jigsaw_image = Image.open(io.BytesIO(jigsaw_image_data))
    jigsaw_image.save("slide.png")
    paste_image_on_background("slide.png", "new_slide.png", int(img_json["data"]["y"]))
    res = slider1('bg.png','new_slide.png')
    return res,img_json["data"]['y']
def get_slide_img_verify_result(loginId,x_y_json):
    url = "https://m.ctyun.cn/alogic-ctyun/user/VerifySlideVerify"
    params = {
        "referrer": "wap",
        "mainVersion": "300031500",
        # "comParam_curTime": params_json['params']['comParam_curTime'],
        # "comParam_seqCode": params_json['params']['comParam_seqCode'],
        # "comParam_signature": params_json['params']['comParam_signature'],
        "isCheck": "true",
        "locale": "zh-cn"
    }
    data = {
        "loginId": loginId,
        'x':x_y_json['x'],
        'y':x_y_json['y']
    }
    response = session.post(url, params=params, data=data)
    logger.info(f'滑块验证结果：{response.json()}')

if __name__ == '__main__':
    loginId = get_loginId()
    img_json = get_slide_img(loginId)
    distance, y = get_distance(img_json)
    x_y_json = execjs.compile(open('验证码.js', 'r', encoding='utf-8').read()).call('get_x_y', loginId, distance, y)
    get_slide_img_verify_result(loginId,x_y_json)

