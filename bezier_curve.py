from curses.ascii import BS
import matplotlib.pyplot as plt
import numpy as np

step = 0.001

# kの階乗 (k!)
def factorial(k):
    ktmp = 1
    for i in range(k, 2, -1):
        ktmp *= i
    return ktmp

# 二項係数 nCk
def binomial(n, k):
    return factorial(n)/(factorial(n - k)*factorial(k))

# ベジェ曲線
def bezier(B_points):
    t = np.arange(0, 1, step)
    B_size = len(B_points)
    Bc = 0
    for i in range(0, B_size, 1):
        Bc += binomial(B_size-1, i) * (t**i) * ((1 - t)**(B_size - 1 - i))*B_points[i]
    return Bc

# 制御点のXY座標
Bx = [0, 0.5, 3, 4]
By = [0, 1, 3, 0]

# ベジェ曲線を計算
Lx = bezier(Bx)
Ly = bezier(By)

# 描画用のオブジェクトを作成
fig, ax = plt.subplots()

# 描画範囲の縦横比を1:1に設定
ax.set_aspect('equal')

# プロット
ax.plot(Lx, Ly, color='red', linewidth=3)

# ハンドルのプロット
for i in range(0, int(len(Bx)/2), 1):
    ax.plot([Bx[2*i], Bx[2*i + 1]], [By[2*i],By[2*i + 1]], color='blue', linewidth=1)

# 制御点のプロット
for i in range(0, len(Bx), 1):
    ax.plot([Bx[i]], [By[i]], color='blue', marker='o', markersize=4)

# 描画
plt.show()