import cv2
import numpy as np


def detect_plate(img_path):
    
    img = cv2.imread(img_path)
    if img is None:
        raise ValueError("图片路径错误或文件损坏")

    
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower_blue = np.array([100, 50, 50])  # HSV蓝色范围下限
    upper_blue = np.array([130, 255, 255]) # HSV蓝色范围上限
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    
    
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    plates = []
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        if 2.5 < w/h < 5.0:  # 车牌宽高比特征
            plates.append((x, y, w, h))
    
    if not plates:
        return None
    
    # 返回最大区域
    x, y, w, h = max(plates, key=lambda p: p[2]*p[3])
    return img[y:y+h, x:x+w]

if __name__ == "__main__":
    import os
    os.makedirs("output", exist_ok=True)  # 自动创建输出目录
    
    # 处理input目录下所有图片
    for img_name in os.listdir("input"):
        try:
            img_path = os.path.join("input", img_name)
            plate = detect_plate(img_path)
            
            if plate is not None:
                out_path = os.path.join("output", f"plate_{img_name}")
                cv2.imwrite(out_path, plate)
                print(f"✅ 成功检测并保存: {out_path}")
            else:
                print(f"⚠️ 未检测到车牌: {img_name}")
                
        except Exception as e:
            print(f"❌ 处理失败 [{img_name}]: {str(e)}")