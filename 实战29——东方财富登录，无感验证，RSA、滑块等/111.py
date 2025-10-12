import ddddocr
from loguru import logger
import requests
from io import BytesIO
from PIL import Image
from captcha_recognizer.recognizer import Recognizer
# 下载打乱后的切片背景图
url = "https://smartvcode2.eastmoney.com/12/resources/e02b_160/2/93/9320570c756a16054ee526f5a394e29a/bg/84db6a01.jpg"
response = requests.get(url)
original_img = Image.open(BytesIO(response.content))
# 切片大小
slice_width = 12
slice_height = 80
# 顺序还原映射（JS a() 逻辑复现）
def build_index():
    order = "6_11_7_10_4_12_3_1_0_5_2_9_8".split("_")
    order = list(map(int, order))
    result = []
    for r in range(52):
        idx = 2 * order[int((r % 26) / 2)] + (r % 2)
        if (int(r / 2) % 2) == 0:
            idx += -1 if (r % 2) else 1
        if r >= 26:
            idx += 26
        result.append(idx)
    return result
mapping = build_index()
# 创建新图像用于拼接（宽度 312，高度 160）
canvas = Image.new("RGB", (26 * slice_width, 2 * slice_height))
for i in range(52):
    src_index = mapping[i]
    row = 0 if i < 26 else 1
    src_row = 0 if src_index < 26 else 1
    src_col = src_index % 26

    # 切片区域
    left = src_col * slice_width
    upper = src_row * slice_height
    right = left + slice_width
    lower = upper + slice_height

    # 粘贴区域
    dst_left = (i % 26) * slice_width
    dst_upper = row * slice_height

    # 裁剪并粘贴
    part = original_img.crop((left, upper, right, lower))
    canvas.paste(part, (dst_left, dst_upper))

# 保存还原后的图
canvas.save("restored.jpg")
canvas.show()

def get_distince(bg_img, sl_img):
    det = ddddocr.DdddOcr(det=True, ocr=True)
    with open(sl_img, 'rb') as f:
        target_bytes = f.read()
    with open(bg_img, 'rb') as f:
        background_bytes = f.read()
    res = det.slide_match(target_bytes, background_bytes)
    logger.debug(f"获取的缺口距离是==>>{res['target'][0]}")

    return res['target'][0]
def get_distincce1(bg_img):
    recognizer = Recognizer()
    box, confidence = recognizer.identify_gap(source=bg_img, verbose=False)
    print(confidence)
    print( box[0])
    return box[0]



if __name__ == '__main__':
    get_distince("restored.jpg", "89ee15d4.png")
    get_distincce1("restored.jpg")
    # "appid=201802274651|ctxid=bb1e0ec71fe247e2763fc0492abf0b80|type=slide|u=175|d=0,0,0:0,1,42:1,1,74:6,1,91:13,1,107:19,2,122:24,2,138:28,3,154:30,3,166:34,3,178:38,3,195:41,3,210:43,3,227:48,3,242:57,3,258:64,3,274:68,3,290:73,3,306:78,3,322:82,3,338:85,3,349:90,3,362:94,3,378:97,3,394:103,3,410:106,3,427:109,3,443:112,3,467:114,3,490:117,3,507:119,3,522:122,3,538:123,3,548:124,3,563:127,3,587:129,3,602:132,3,618:133,3,629:136,3,642:137,3,659:140,3,682:142,3,698:143,3,723:145,3,739:146,3,754:149,3,778:150,3,810:151,3,851:152,3,867:153,3,899:154,3,923:155,3,955:157,3,986:158,3,1018:159,3,1067:160,3,1098:161,3,1124:162,3,1179:163,3,1218:164,3,1250:165,3,1275:166,3,1314:167,3,1403:168,3,1427:169,3,1467:170,3,1514:171,3,1554:172,3,1611:173,3,1635:174,3,1691:175,3,1763:175,3,2291|a=12340545349|p=xxoo123456|t=2291|r=0.4254656702257261"
