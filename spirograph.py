import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import ArtistAnimation

PI = np.pi

# 描画用オブジェクトを作成
fig, ax = plt.subplots()

# 描画範囲を1:1に設定
ax.set_aspect('equal')

# プロットを貯めるためのリスト
artists = []

# アニメーションのコマ数
step = 360

# 円の半径
r_o = 10
r_i = 7
r_p = 2.8

# 外側の円をプロット
theta_circle = np.arange(0, 2*PI, 2*PI/step)
x_fix = r_o*np.cos(theta_circle)
y_fix = r_o*np.sin(theta_circle)
ax.plot(x_fix, y_fix, color='black')

# X, Yの定義
def x_func(u):
    return (r_o - r_i)*np.cos(u) + r_p*np.cos(u*(r_o - r_i)/r_i)
def y_func(u):
    return (r_o - r_i)*np.sin(u) - r_p*np.sin(u*(r_o - r_i)/r_i)

# スピログラフをプロット
theta_mov = np.arange(0, r_i*2*PI, r_i*2*PI/step)
x_mov = x_func(theta_mov)
y_mov = y_func(theta_mov)
ax.plot(x_mov, y_mov, color='blue')

# 動く部分（内側の円とペンを挿す位置）をプロット
for t in range(step):
    theta = r_i*2*PI*t/step
    
    # 内側の円をプロット
    x_c = (r_o - r_i)*np.cos(theta) + r_i*np.cos(theta_circle)
    y_c = (r_o - r_i)*np.sin(theta) + r_i*np.sin(theta_circle)
    plt_c = ax.plot(x_c, y_c, color='black')

    # 内側の円の中心からペンの位置までの線分をプロット
    x_l = [(r_o - r_i)*np.cos(theta), x_func(theta)]
    y_l = [(r_o - r_i)*np.sin(theta), y_func(theta)]
    plt_l = ax.plot(x_l, y_l, color='red')

    # ペンの位置をプロット
    x_p = x_func(theta)
    y_p = y_func(theta)
    plt_p = ax.plot([x_p], [y_p], color='red', marker='o', markersize=8)
    
    # プロットをまとめて追加
    artists.append((plt_c + plt_l + plt_p))

# アニメーションを作成
anim = ArtistAnimation(fig, artists, interval=30)

# gitアニメとして保存（imagemagicを使用）
# anim.save('hypocycloid_2.gif',writer='imagemagick', fps=30)

# 描画
plt.show()
