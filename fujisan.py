import numpy as np
import matplotlib.pyplot as plt

# サンプリングの間隔（どれだけ細かくグラフの点を打つか）
step = 0.01

# 描画する各関数のXの範囲
t_top = np.arange(-1, 1, step)
t_left = np.arange(-6, -1, step)
t_right = np.arange(1, 6, step)
u = np.arange(-2, 2, step)

# f(x)（|x|≦1）の定義
def f_top(x):
    return x**4 - x**2 + 6
# f(x)（|x|>1）の定義
def f_side(x):
    return 12/(np.abs(x) + 1)
# g(x)（|x|≦2）の定義
def g(x):
    return np.cos(2*np.pi*x)/2 + 7/2    

# 描画用のオブジェクトの作成
fig, ax = plt.subplots()

# グラフの描画範囲と縦横比を設定
ax.set_xlim(-6, 6)
ax.set_ylim(0, 7)
ax.set_aspect('equal')

# グラフのタイトル
ax.set_title("Mount Fuji")

# 関数をプロット
ax.plot(u, g(u), color="black")
ax.plot(t_top, f_top(t_top), color="blue")
ax.plot(t_left, f_side(t_left), color="blue")
ax.plot(t_right, f_side(t_right), color="blue")

# プロットした結果を表示
plt.show()

# 画像として保存（この場合はplt.show()をコメントアウトする）
# plt.savefig('shizuoka.png',format='png')