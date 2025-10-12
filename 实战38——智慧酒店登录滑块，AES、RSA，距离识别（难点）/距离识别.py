import os

import cv2


def identify_gap(bg, tp, out):
    '''
    bg: 背景图片
    tp: 缺口图片
    out:输出图片
    '''
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


def get_slide_distance(bg_path, slide_path):
    '''
    识别滑块具体位置，返回位置比例: 位置/图片宽度
    使用的时候再乘以实际图片宽度即可
    '''
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
    result_path = os.path.join(os.path.dirname(bg_path), "./PictureTemp/result.png")
    cv2.imwrite(result_path, bg_img)
    return max_loc[0]
