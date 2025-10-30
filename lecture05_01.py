import numpy as np
import cv2
from my_module.K24047.lecture05_camera_image_capture import MyVideoCapture

def lecture05_01():
    # カメラキャプチャ実行
    app = MyVideoCapture()
    app.run()

    # キャプチャ画像を取得（保存せずにメモリ上で扱う）
    capture_img: cv2.Mat = app.get_img()
    if capture_img is None:
        raise ValueError("カメラ画像が取得できませんでした")

    # Google検索画面画像を読み込み
    google_img: cv2.Mat = cv2.imread('images/google.png')
    if google_img is None:
        raise FileNotFoundError("google.pngが見つかりません")

    g_height, g_width, _ = google_img.shape
    c_height, c_width, _ = capture_img.shape

    # 白色領域をカメラ画像で置換（グリッド状に並べる）
    for y in range(g_height):
        for x in range(g_width):
            b, g, r = google_img[y, x]
            if (b, g, r) == (255, 255, 255):
                cy = y % c_height
                cx = x % c_width
                google_img[y, x] = capture_img[cy, cx]

    # 加工後の画像を保存
    cv2.imwrite('lecture05_01_K24047.png', google_img)

    # カメラ画像（元画像）を保存
    cv2.imwrite('output_images/camera_capture.png', capture_img)

if __name__ == "__main__":
    lecture05_01()