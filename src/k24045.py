import numpy as np
import cv2
import os # ディレクトリ操作のため
from my_module.K21999.lecture05_camera_image_capture import MyVideoCapture

def lecture05_01():

    # カメラキャプチャ実行
    app = MyVideoCapture()
    app.run()

    # 画像をローカル変数に保存
    google_img_path = 'images/google.png'
    google_img = cv2.imread(google_img_path)

    # google.png が読み込めたか確認
    if google_img is None:
        print(f"エラー: {google_img_path} が読み込めません。")
        print("カレントディレクトリに 'images/google.png' が存在するか確認してください。")
        return

    # カメラからキャプチャした画像を取得
    # capture_img : cv2.Mat = cv2.imread('images/camera_capture.png') # 動作テスト用なので提出時にこの行を消すこと
    capture_img = app.get_img()

    # キャプチャ画像が取得できたか確認
    if capture_img is None:
        print("エラー: カメラ画像がキャプチャされませんでした。")
        print("カメラのプレビューウィンドウで 'q' キーを押して終了しましたか？")
        return

    # 画像サイズを取得
    g_hight, g_width, g_channel = google_img.shape
    c_hight, c_width, c_channel = capture_img.shape
    print(f"Google画像サイズ: {google_img.shape}")
    print(f"キャプチャ画像サイズ: {capture_img.shape}")

    # キャプチャ画像をgoogle画像と同じサイズにリサイズ
    print("キャプチャ画像をGoogle画像サイズにリサイズします...")
    resized_capture_img = cv2.resize(capture_img, (g_width, g_hight))

    print("Google画像の白色部分をキャプチャ画像で置き換えます...")
    # google画像の白色ピクセルをリサイズしたキャプチャ画像で置き換え
    for y in range(g_hight):
        for x in range(g_width):
            # ピクセル値 (B, G, R) を取得
            b, g, r = google_img[y, x]
            
            # もし白色(B=255, G=255, R=255)だったら置き換える
            # OpenCVはBGRの順であることに注意
            if (b, g, r) == (255, 255, 255):
                # リサイズしたキャプチャ画像のピクセルで置き換え
                google_img[y, x] = resized_capture_img[y, x]

    # 出力先ディレクトリの確認/作成
    output_dir = 'output_images'
    os.makedirs(output_dir, exist_ok=True)
    
    # 書き込み処理
    output_path = os.path.join(output_dir, 'composite_image.png')
    cv2.imwrite(output_path, google_img)
    print(f"合成画像を {output_path} に保存しました。")

    # (オプション) 結果を表示
    cv2.imshow('Composite Image', google_img)
    print("合成画像を表示しました。任意のキーを押すと終了します。")
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print("処理が完了しました。")
