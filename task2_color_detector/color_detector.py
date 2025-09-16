import cv2
import numpy as np
import os

def generate_test_images():
    """生成测试图片到test_images目录"""
    os.makedirs("test_images", exist_ok=True)
    
    colors = {
        'red': [0, 0, 255],     # OpenCV使用BGR格式
        'green': [0, 255, 0],
        'blue': [255, 0, 0]
    }
    
    for name, color in colors.items():
        img = np.zeros((100, 100, 3), dtype=np.uint8)
        img[:, :] = color
        cv2.imwrite(f"test_images/{name}.jpg", img)
    print("测试图片已生成到 test_images/")

def detect_color(image_path):
    """
    检测图片主颜色（核心函数）
    :param image_path: 图片路径
    :return: (颜色名称, 平均HSV值)
    """
    img = cv2.imread(image_path)
    if img is None:
        raise ValueError(f"图片读取失败，请检查路径: {image_path}")
    
    # 转换为HSV颜色空间
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    avg_hsv = np.mean(hsv, axis=(0, 1)).astype(int)
    hue = avg_hsv[0]  # 色相分量

    # 颜色判定逻辑
    if hue < 10 or hue > 170:  # 红色在HSV环的两端
        color = "红色"
    elif 35 <= hue <= 85:     # 绿色范围
        color = "绿色"
    elif 100 <= hue <= 130:   # 蓝色范围
        color = "蓝色"
    else:
        color = "未知颜色"
    
    return color, avg_hsv

if __name__ == "__main__":
    # 首次运行时生成测试图片
    if not os.path.exists("test_images"):
        generate_test_images()

    # 交互式检测
    print("HRT任务1.2 - 颜色检测器")
    print("可用测试图片:", os.listdir("test_images"))
    
    try:
        # 默认检测红色图片，也可手动输入其他图片名
        image_name = input("输入测试图片名（如red.jpg）：").strip() or "red.jpg"
        image_path = os.path.join("test_images", image_name)
        
        color, hsv = detect_color(image_path)
        print("\n检测结果:")
        print(f"颜色: {color}")
        print(f"HSV平均值: {hsv}")
        
    except Exception as e:
        print(f"错误: {e}")