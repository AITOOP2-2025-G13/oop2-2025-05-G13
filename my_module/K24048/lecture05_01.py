import numpy as np
import cv2
from my_module.K24048.lecture05_camera_image_capture import MyVideoCapture

def lecture05_01():

    # カメラキャプチャ実行
    app = MyVideoCapture()
    app.run()

    # 画像をローカル変数に保存
    google_img : cv2.Mat = cv2.imread('images/google.png')
    capture_img : cv2.Mat = app.get_img()

    g_hight, g_width, g_channel = google_img.shape
    c_hight, c_width, c_channel = capture_img.shape
    print(google_img.shape)
    print(capture_img.shape)

    for x in range(g_width):
        for y in range(g_hight):
            g, b, r = google_img[y, x]
            # もし白色(255,255,255)だったら置き換える
            if (b, g, r) == (255, 255, 255):
                # キャプチャ画像をグリッド状に配置するための座標計算
                capture_x = x % c_width
                capture_y = y % c_hight
                # キャプチャ画像のピクセル値で置換
                google_img[y, x] = capture_img[capture_y, capture_x]


    # 書き込み処理
    # implement me
    cv2.imwrite('output_images/lecture05_01_k24048.png', google_img)
    print ("画像の書き込みが完了しました。")