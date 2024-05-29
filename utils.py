import math as m


# 度量函数
def findAngle(x1, y1, x2, y2):
    theta = m.acos((y2 - y1) * (-y1) / (m.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2) * y1))
    degree = int(180/m.pi)*theta
    return degree

"""
歪头监控：计算 左耳（7点）和 右耳（8点）的夹角
低头监控：计算 左嘴角（9点）和 左肩膀（11点）的夹角
侧脸监控：计算 右眼内（4点）和 左耳（7点）的距离，计算 左眼内（1点）和 右耳（8点）的距离
高低肩监控：计算 左肩膀（11点）和 右肩膀（12点）的夹角            *****有的人左肩和右肩一个高一个低*****
撑桌监控：如果 左嘴角（9点）或者 右嘴角（10点）的 y 坐标 大于 左肩膀（11点）或 右肩膀（12点）的 y 坐标，视为撑桌
仰头监控：计算 鼻子（0点）和 左耳（7点）的夹角
趴桌监控：如果 左肩膀（11点）和 右肩膀（12点）的 归一化y坐标 之和大于0.75，判定为趴桌
"""
def all_detection(nose_x, nose_y,                               # 鼻子（0点）的 x 坐标 和 y 坐标
                  left_eye_inner_x, left_eye_inner_y,           # 左眼内（1点）的 x 坐标 和 y 坐标
                  right_eye_inner_x, right_eye_inner_y,         # 右眼内（4点）的 x 坐标 和 y 坐标
                  left_ear_x, left_ear_y,                       # 左耳（7点）的 x 坐标 和 y 坐标
                  right_ear_x, right_ear_y,                     # 右耳（8点）的 x 坐标 和 y 坐标
                  left_mouth_x, left_mouth_y,                   # 左嘴角（9点）的 x 坐标 和 y 坐标
                  right_mouth_x, right_mouth_y,                 # 右嘴角（10点）的 x 坐标 和 y 坐标
                  left_shoulder_x, left_shoulder_y,             # 左肩膀（11点）的 x 坐标 和 y 坐标
                  right_shoulder_x, right_shoulder_y,           # 右肩膀（12点）的 x 坐标 和 y 坐标
                  left_shoulder_x_norm, left_shoulder_y_norm,   # 归一化后的左肩膀（11点）的 x 坐标 和 y 坐标
                  right_shoulder_x_norm, right_shoulder_y_norm  # 归一化后的右肩膀（12点）的 x 坐标 和 y 坐标
                  ):
    waitou_inclination = findAngle(left_ear_x, left_ear_y, right_ear_x, right_ear_y)
    ditou_inclination = findAngle(left_mouth_x, left_mouth_y, left_shoulder_x, left_shoulder_y)
    gaodijian_inclination = findAngle(left_shoulder_x, left_shoulder_y, right_shoulder_x, right_shoulder_y)
    yangtou_inclination = findAngle(nose_x, nose_y, left_ear_x, left_ear_y)
    if waitou_inclination < 80:
        tmp = '左歪头'
    elif waitou_inclination > 100:
        tmp = '右歪头'
    elif (left_shoulder_y_norm + right_shoulder_y_norm) > 1.5:
        tmp = '趴桌'
    elif ditou_inclination < 115:
        tmp = '低头'
    elif left_ear_x < right_eye_inner_x:
        tmp = '左侧脸'
    elif right_ear_x > left_eye_inner_x:
        tmp = '右侧脸'
    elif gaodijian_inclination > 100:
        tmp = '高低肩'
    elif gaodijian_inclination < 80:
        tmp = '高低肩'
    elif (left_mouth_y or right_mouth_y) > (left_shoulder_y or right_shoulder_y):
        tmp = '撑桌'
    elif yangtou_inclination > 90:
        tmp = '仰头'
    else:
        tmp = '正脸'
    return tmp