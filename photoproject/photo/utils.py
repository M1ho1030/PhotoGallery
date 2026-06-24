import cv2
import numpy as np
 
def vhs_effect(img):
    h, w = img.shape[:2]
 
    # --- ① 色ズレ---
    b, g, r = cv2.split(img)
    b = np.roll(b, 5, axis=1)
    r = np.roll(r, -5, axis=0)
    img = cv2.merge([b, g, r])
 
    # --- ② 横方向ゆがみ---
    distorted = np.zeros_like(img)
    for i in range(h):
        shift = int(np.sin(i / 20.0) * 2 + np.random.randn() * 0.5)
        distorted[i] = np.roll(img[i], shift, axis=0)
    img = distorted
 
    # --- ③ スキャンライン---
    for i in range(0, h, 2):
        img[i:i+1, :] = img[i:i+1, :] * 0.95
 
    # ベースノイズ
    noise = np.random.normal(1, 40, img.shape).astype(np.int16)
 
    # 粒ノイズ（ランダムドット）
    salt = np.random.randint(5, 40, img.shape).astype(np.int16)
    mask = np.random.rand(h, w, 3) < 0.04
    noise[mask] = salt[mask]
    img = img.astype(np.int16) + noise
    img = np.clip(img, 0, 255).astype(np.uint8)
 
    # --- 解像度劣化 ---
    small = cv2.resize(img, (w//4, h//4))
    img = cv2.resize(small, (w, h))
 
    # --- 横方向ぼかし ---
    kernel = np.ones((1,5)) / 4
    img = cv2.filter2D(img, -1, kernel)
 
    # --- 色にじみ ---
    blur = cv2.GaussianBlur(img, (9,9), 0)
    img = cv2.addWeighted(img, 0.7, blur, 0.3, 0)
 
    # --- ⑤ 明るさムラ ---
    gradient = np.tile(np.linspace(0.95, 1.05, w), (h, 1))
    gradient = cv2.merge([gradient, gradient, gradient])
    img = np.clip(img * gradient, 0, 255).astype(np.uint8)
 
    # --- ⑦ コントラスト低下---
    img = cv2.convertScaleAbs(img, alpha=0.9, beta=5)
 
    # --- ⑧ 黄ばみ---
    yellow = np.full_like(img, (0, 3, 13))  # BGR
    img = cv2.add(img, yellow)
 
    # --- ⑨ ラインノイズ ---
    for _ in range(3):
        y = np.random.randint(0, h)
        img[y:y+2, :] = 155 * np.random.rand(1, w, 3)
 
    # --- ⑩ たまに画面ズレ ---
    if np.random.rand() > 0.9:
        img = np.roll(img, np.random.randint(-20, 20), axis=1)
 
    return img