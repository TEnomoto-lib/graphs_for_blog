import numpy as np
import matplotlib.pyplot as plt

#円周率
PI = np.pi

# ヘヴィサイド関数のx=0での値の定義
c = 1

# Xの定義（Wolfram Alphaで「ダースベイダー」と検索した結果より）
def x_func(t):
    return ((-(58/7)*np.sin(14/9 - 16*t) - (61/11)*np.sin(14/9 - 12*t) - (43/8)*np.sin(3/2 - 10*t)
    - (108/7)*np.sin(11/7 - 8*t) - 193/9*np.sin(14/9 - 6*t) - 53/4*np.sin(4/3 - 5*t) + 18741/4*np.sin(t + 11/7) 
    + 356/5*np.sin(2*t + 47/10) + 359/5*np.sin(3*t + 11/7) + 659/47*np.sin(4*t + 33/7) + 237/7*np.sin(7*t + 11/7) 
    + 445/7*np.sin(9*t + 8/5) + 147/5*np.sin(11*t + 8/5) + 13/2*np.sin(13*t + 3/2) + 14/9*np.sin(14*t + 9/7) 
    + 3/4*np.sin(15*t + 3/5) - 3448/7) *np.heaviside(75*PI -t, c) *np.heaviside(t - 71*PI, c) + (18175/9*np.sin(t + 11/7) + 35/3*np.sin(2*t + 14/9) 
    + 1195/6*np.sin(3*t + 11/7) + 199/22*np.sin(4*t + 11/7) + 16851/7) *np.heaviside(71*PI -t, c) *np.heaviside(t - 67*PI, c) + (-27/5*np.sin(14/9 - 8*t) 
    - 23/3*np.sin(17/11 - 6*t) - 39/5*np.sin(14/9 - 4*t) + 12163/6*np.sin(t + 11/7) + 89/5*np.sin(2*t + 11/7) 
    + 595/3*np.sin(3*t + 11/7) + 367/5*np.sin(5*t + 11/7) + 116/3*np.sin(7*t + 11/7) - 19148/5) *np.heaviside(67*PI -t, c) *np.heaviside(t - 63*PI, c) 
    + (-881/7*np.sin(14/9 - 16*t) - 277/4*np.sin(14/9 - 12*t) - 117*np.sin(11/7 - 11*t) - 166*np.sin(11/7 - 10*t) 
    - 624/7*np.sin(11/7 - 9*t) - 713/5*np.sin(11/7 - 4*t) - 353/5*np.sin(11/7 - 3*t) - 13/5*np.sin(11/7 - 2*t) 
    + 199/4*np.sin(t + 11/7) + 18/5*np.sin(5*t + 37/8) + 437/10*np.sin(6*t + 8/5) + 155/12*np.sin(7*t + 5/3) 
    + 23/12*np.sin(8*t + 13/6) + 121/8*np.sin(13*t + 14/3) + 760/9*np.sin(14*t + 8/5) + 75/4*np.sin(15*t + 14/9) 
    + 797/7*np.sin(17*t + 8/5) - 5461/8) *np.heaviside(63*PI -t, c) *np.heaviside(t - 59*PI, c) + (-81/2*np.sin(3/2 - 6*t) - 209/16*np.sin(13/14 - 4*t) 
    - 103/5*np.sin(9/8 - 2*t) + 24415/7*np.sin(t + 11/7) + 1571/3*np.sin(3*t + 11/7) + 463/4*np.sin(5*t + 11/7) 
    + 428/7*np.sin(7*t + 11/7) + 172/9*np.sin(8*t + 11/8) + 95/3*np.sin(9*t + 3/2) 
    + 284/7*np.sin(10*t + 37/8) - 10097/33) *np.heaviside(59*PI -t, c) *np.heaviside(t - 55*PI, c) + (-172/3*np.sin(11/7 - 13*t) 
    - 807/7*np.sin(11/7 - 9*t) + 864/5*np.sin(t + 11/7) + 6045/7*np.sin(2*t + 11/7) + 136/3*np.sin(3*t + 14/9) 
    + 25/6*np.sin(4*t + 30/7) + 657/8*np.sin(5*t + 11/7) + 8218/33*np.sin(6*t + 11/7) + 617/5*np.sin(7*t + 33/7) 
    + 199/2*np.sin(8*t + 11/7) + 7744/29*np.sin(10*t + 11/7) + 235/4*np.sin(11*t + 14/9) + 335/6*np.sin(12*t + 33/7) 
    + 683/5*np.sin(14*t + 33/7) + 42*np.sin(15*t + 11/7) + 285/8*np.sin(16*t + 11/7) + 280/31*np.sin(17*t + 47/10) 
    + 427/4*np.sin(18*t + 11/7) + 282/5*np.sin(19*t + 11/7) + 32/5*np.sin(20*t + 14/3) 
    + 17*np.sin(21*t + 11/7) - 2441/4) *np.heaviside(55*PI -t, c) *np.heaviside(t - 51*PI, c) + (-173/3*np.sin(20/13 - 8*t) - 80/3*np.sin(2/5 - 4*t) 
    + 5601/5*np.sin(t + 11/7) + 173/8*np.sin(2*t + 3/4) + 1608/7*np.sin(3*t + 19/13) + 372/5*np.sin(5*t + 9/7) 
    + 155/7*np.sin(6*t + 3/4) + 361/4*np.sin(7*t + 3/2) + 1373/28*np.sin(9*t + 14/3) + 122/5*np.sin(10*t + 35/8) 
    + 179/10*np.sin(11*t + 29/7) + 147/10*np.sin(12*t + 12/5) + 53/4*np.sin(13*t + 13/6) 
    + 83/5*np.sin(14*t + 17/10) - 5417/8) *np.heaviside(51*PI -t, c) *np.heaviside(t - 47*PI, c) + (-249/10*np.sin(13/9 - 6*t) 
    - 2573/7*np.sin(11/7 - 4*t) - 76/3*np.sin(14/9 -t) + 2069/4*np.sin(2*t + 11/7) + 6079/9*np.sin(3*t + 11/7) 
    + 1049/9*np.sin(5*t + 11/7) + 2623/46*np.sin(7*t + 8/5) + 39/2*np.sin(8*t + 3/2) + 79/2*np.sin(9*t + 14/3) 
    + 91/5*np.sin(10*t + 33/7) + 99/4*np.sin(11*t + 8/5) + 30058/9) *np.heaviside(47*PI -t, c) *np.heaviside(t - 43*PI, c) + (-535/17*np.sin(14/9 - 10*t) 
    - 1566/7*np.sin(11/7 - 4*t) + 1435/8*np.sin(t + 8/5) + 2383/9*np.sin(2*t + 8/5) + 2861/5*np.sin(3*t + 8/5) 
    + 145/3*np.sin(5*t + 11/7) + 297/7*np.sin(6*t + 8/5) + 26/5*np.sin(7*t + 25/6) + 791/10*np.sin(8*t + 13/8) 
    + 51/5*np.sin(9*t + 32/7) + 265/6*np.sin(11*t + 8/5) + 20/3*np.sin(12*t + 9/2) - 31695/7) *np.heaviside(43*PI -t, c) *np.heaviside(t - 39*PI, c) 
    + (-151/7*np.sin(6/7 - 7*t) + 7955/2*np.sin(t + 5/3) + 411/8*np.sin(2*t + 1/9) + 4576/15*np.sin(3*t + 11/6) 
    + 107/5*np.sin(4*t + 17/5) + 110/9*np.sin(5*t + 63/31) + 55/9*np.sin(6*t + 18/5) - 4994/7) *np.heaviside(39*PI -t, c) *np.heaviside(t - 35*PI, c) 
    + (3476/5*np.sin(t + 4/3) + 433/5*np.sin(2*t + 25/6) + 579/7*np.sin(3*t + 5/3) 
    + 113/5*np.sin(4*t + 23/5) + 6084/5) *np.heaviside(35*PI -t, c) *np.heaviside(t - 31*PI, c) + (-619/7*np.sin(9/7 - 3*t) + 802*np.sin(t + 37/8) 
    + 421/5*np.sin(2*t + 11/7) - 23264/9) *np.heaviside(31*PI -t, c) *np.heaviside(t - 27*PI, c) + (-71/4*np.sin(7/9 - 9*t) - 289/9*np.sin(6/7 - 8*t)
     - 922/3*np.sin(1/10 - 3*t) - 3601/36*np.sin(5/4 - 2*t) + 30703/7*np.sin(t + 1) + 706/9*np.sin(4*t + 5/6) 
     + 265/14*np.sin(5*t + 11/5) + 278/9*np.sin(6*t + 1/8) + 341/10*np.sin(7*t + 4/5) - 605) *np.heaviside(27*PI -t, c) *np.heaviside(t - 23*PI, c) 
     + (10764/7*np.sin(t + 40/9) + 519/4*np.sin(2*t + 28/11) + 707/4*np.sin(3*t + 27/7) + 685/14*np.sin(4*t + 21/10) 
     + 355/7*np.sin(5*t + 11/3) + 128/3*np.sin(6*t + 7/5) + 96/5*np.sin(7*t + 29/9) + 272/9*np.sin(8*t + 18/17) 
     + 71/8*np.sin(9*t + 16/5) + 127/7*np.sin(10*t + 4/7) + 71/9*np.sin(11*t + 30/7) + 46/3*np.sin(12*t + 2/7) 
     - 3661/6) *np.heaviside(23*PI -t, c) *np.heaviside(t - 19*PI, c) + (-115/7*np.sin(1/7 - 13*t) - 462/13*np.sin(1/6 - 9*t) - 353/3*np.sin(6/5 - 7*t) 
     - 6463/6*np.sin(5/6 - 2*t) + 340/3*np.sin(8*t) + 22885/12*np.sin(t + 6/5) + 443/7*np.sin(3*t + 19/5) + 295/14*np.sin(4*t + 5/2) 
     + 1466/7*np.sin(5*t + 27/10) + 288/5*np.sin(6*t + 13/4) + 265/8*np.sin(10*t + 16/7) + 60/7*np.sin(11*t + 21/5) 
     + 930/19*np.sin(12*t + 16/7) - 5475/8) *np.heaviside(19*PI -t, c) *np.heaviside(t - 15*PI, c) + (3299/2*np.sin(t + 7/6) + 377/5*np.sin(2*t + 7/6) 
     + 139/6*np.sin(3*t + 2/7) + 10166/7) *np.heaviside(15*PI -t, c) *np.heaviside(t - 11*PI, c) + (-30228/19*np.sin(16/15 -t) + 200/7*np.sin(2*t + 35/12) 
     + 316/9*np.sin(3*t + 7/3) + 178/5*np.sin(4*t + 12/7) + 365/9*np.sin(5*t + 21/5) 
     + 18/7*np.sin(6*t + 11/9) - 20196/7) *np.heaviside(11*PI -t, c) *np.heaviside(t - 7*PI, c) + (-257/4*np.sin(23/24 - 15*t) - 2071/4*np.sin(1/3 - 3*t) 
     - 99793/36*np.sin(10/9 - 2*t) + 51290/7*np.sin(t + 1) + 6064/9*np.sin(4*t + 3/4) + 2497/5*np.sin(5*t + 16/9) + 2413/8*np.sin(6*t + 11/4) 
     + 5585/21*np.sin(7*t + 1) + 493/3*np.sin(8*t + 5/3) + 859/11*np.sin(9*t + 3/2) + 462/5*np.sin(10*t + 26/7) + 421/4*np.sin(11*t + 2) 
     + 735/8*np.sin(12*t + 5/2) + 63*np.sin(13*t + 8/3) + 425/7*np.sin(14*t + 71/18) - 4853/8) *np.heaviside(7*PI -t, c) *np.heaviside(t - 3*PI, c) + (-4027/7*np.sin(4/3 - 5*t) 
     + 55361/7*np.sin(t + 1) + 2324/3*np.sin(2*t + 31/16) + 705/7*np.sin(3*t + 11/9) + 2194/11*np.sin(4*t + 26/25) + 977/9*np.sin(6*t + 13/4)
      + 284*np.sin(7*t + 27/7) + 1026/7*np.sin(8*t + 7/5) + 677/8*np.sin(9*t + 19/7) 
      + 1023/8*np.sin(10*t + 5/9) - 4475/8) *np.heaviside(3*PI -t, c) *np.heaviside(t +PI, c)) *np.heaviside(np.sqrt(np.sign(np.sin(t/2))), c)

# Yの定義（Wolfram Alphaで「ダースベイダー」と検索した結果より）
def y_func(t):
    return ((-59*np.sin(14/9 - 16*t) - 5/2*np.sin(4/3 - 15*t) - 466/7*np.sin(17/11 - 14*t) - 14/5*np.sin(14/9 - 13*t) 
    - 265/12*np.sin(11/7 - 12*t) - 185/2*np.sin(11/7 - 8*t) - 38/3*np.sin(11/7 - 7*t) - 2523/8*np.sin(11/7 - 6*t) 
    - 7094/7*np.sin(11/7 - 4*t) - 451/5*np.sin(14/9 - 3*t) + 581/5*np.sin(t + 11/7) + 707/6*np.sin(2*t + 8/5) 
    + 289/36*np.sin(5*t + 4/3) + 93/7*np.sin(9*t + 12/7) + 592/9*np.sin(10*t + 13/8) + 137/9*np.sin(11*t + 14/3) 
    - 63797/8) *np.heaviside(75*PI -t, c) *np.heaviside(t - 71*PI, c) + (-311/8*np.sin(11/7 - 4*t) - 1619/5*np.sin(11/7 - 2*t) 
    - 471/4*np.sin(11/7 -t) + 107/3*np.sin(3*t + 11/7) + 4487/3) *np.heaviside(71*PI -t, c) *np.heaviside(t - 67*PI, c) + (-143/6*np.sin(11/7 - 6*t) 
    - 709/10*np.sin(11/7 - 4*t) - 3736/15*np.sin(11/7 - 2*t) + 3961/30*np.sin(t + 11/7) + 27/7*np.sin(3*t + 33/7) 
    + 145/6*np.sin(5*t + 33/7) + 52/7*np.sin(7*t + 33/7) + 37/6*np.sin(8*t + 33/7) + 19529/14) *np.heaviside(67*PI -t, c) *np.heaviside(t - 63*PI, c) 
    + (-11/5*np.sin(14/9 - 17*t) - 161/20*np.sin(14/9 - 16*t) - 52/7*np.sin(11/7 - 12*t) - 3/2*np.sin(3/2 - 11*t) 
    - 67/10*np.sin(14/9 - 10*t) - 13/6*np.sin(14/9 - 4*t) + 573*np.sin(t + 11/7) + 172/19*np.sin(2*t + 33/7) 
    + 185/6*np.sin(3*t + 11/7) + 179/7*np.sin(5*t + 11/7) + 37/9*np.sin(6*t + 11/7) + 79/5*np.sin(7*t + 11/7) 
    + 14/3*np.sin(8*t + 11/7) + 107/7*np.sin(9*t + 8/5) + 7/4*np.sin(13*t + 8/5) + 11/12*np.sin(14*t + 32/7) 
    + 27/10*np.sin(15*t + 8/5) - 4217/3) *np.heaviside(63*PI -t, c) *np.heaviside(t - 59*PI, c) + (35/3*np.sin(t + 33/7) + 550/9*np.sin(2*t + 47/10) 
    + 255/4*np.sin(3*t + 17/11) + 979/6*np.sin(4*t + 14/9) + 245/9*np.sin(5*t + 3/2) + 101/4*np.sin(6*t + 17/11) 
    + 820/11*np.sin(7*t + 3/2) + 437/7*np.sin(8*t + 3/2) + 339/7*np.sin(9*t + 14/3) 
    + 75/4*np.sin(10*t + 3/2) - 17567/5) *np.heaviside(59*PI -t, c) *np.heaviside(t - 55*PI, c) + (-25/4*np.sin(11/7 - 19*t) - 621/5*np.sin(11/7 - 5*t) 
    + 498/5*np.sin(t + 11/7) + 11/8*np.sin(2*t + 22/5) + 2609/15*np.sin(3*t + 11/7) + 149/3*np.sin(4*t + 8/5) 
    + 52/5*np.sin(6*t + 14/3) + 271/10*np.sin(7*t + 14/9) + 1112/7*np.sin(8*t + 11/7) + 557/6*np.sin(9*t + 33/7) 
    + 109/8*np.sin(10*t + 14/3) + 403/6*np.sin(11*t + 33/7) + 113/3*np.sin(12*t + 8/5) + 609/8*np.sin(13*t + 11/7) 
    + 11/8*np.sin(14*t + 9/2) + 193/7*np.sin(15*t + 11/7) + 117/10*np.sin(16*t + 11/7) + 204/5*np.sin(17*t + 33/7) 
    + 77/10*np.sin(18*t + 33/7) + 401/20*np.sin(20*t + 33/7) + 56/3*np.sin(21*t + 33/7) - 56953/7) *np.heaviside(55*PI -t, c) *np.heaviside(t - 51*PI, c) 
    + (-459/7*np.sin(1/8 - 13*t) - 459/5*np.sin(7/5 - 11*t) + 89/5*np.sin(t + 31/15) + 4109/11*np.sin(2*t + 14/3) 
    + 23*np.sin(3*t + 23/8) + 2692/23*np.sin(4*t + 40/9) + 968/13*np.sin(5*t + 9/4) + 1201/6*np.sin(6*t + 11/6) 
    + 1017/5*np.sin(7*t + 9/5) + 5035/8*np.sin(8*t + 14/3) + 1697/9*np.sin(9*t + 23/5) + 996/7*np.sin(10*t + 13/8) 
    + 166*np.sin(12*t + 4/3) + 736/5*np.sin(14*t + 28/27) - 29201/5) *np.heaviside(51*PI -t, c) *np.heaviside(t - 47*PI, c) 
    + (7611/8*np.sin(t + 11/7) + 2098/3*np.sin(2*t + 11/7) + 4549/5*np.sin(3*t + 11/7) + 3369/5*np.sin(4*t + 33/7) 
    + 484/5*np.sin(5*t + 14/3) + 125/9*np.sin(6*t + 13/8) + 402/5*np.sin(7*t + 23/5) + 267/2*np.sin(8*t + 14/3) 
    + 730/7*np.sin(9*t + 37/8) + 2056/17*np.sin(10*t + 14/3) + 35*np.sin(11*t + 12/7) - 5032) *np.heaviside(47*PI -t, c) *np.heaviside(t - 43*PI, c) 
    + (-1233/22*np.sin(7/5 - 9*t) - 566/5*np.sin(16/11 - 8*t) - 733/12*np.sin(14/9 - 7*t) - 919/7*np.sin(11/7 - 5*t) 
    - 3557/3*np.sin(14/9 - 3*t) - 2939/4*np.sin(14/9 - 2*t) + 6148/11*np.sin(t + 11/7) + 1185/7*np.sin(4*t + 3/2) 
    + 1600/13*np.sin(6*t + 8/5) + 59/5*np.sin(10*t + 9/7) + 71/9*np.sin(11*t + 13/3)
     + 164/5*np.sin(12*t + 13/8) - 41799/8) *np.heaviside(43*PI -t, c) *np.heaviside(t - 39*PI, c) + (-117/5*np.sin(4/5 - 6*t) - 145/4*np.sin(5/4 - 4*t) 
     - 1311/7*np.sin(7/5 - 2*t) + 15551/10*np.sin(t + 1/9) + 518*np.sin(3*t + 1/5) + 679/17*np.sin(5*t + 2/5) 
     + 259/6*np.sin(7*t + 5/6) - 9484/7) *np.heaviside(39*PI -t, c) *np.heaviside(t - 35*PI, c) + (-130/7*np.sin(9/8 - 4*t) - 427/4*np.sin(24/25 - 3*t)
      - 3332/3*np.sin(9/7 -t) + 932/19*np.sin(2*t + 30/7) - 32269/6) *np.heaviside(35*PI -t, c) *np.heaviside(t - 31*PI, c) + (-1119/13*np.sin(10/9 - 3*t) 
      - 1386/17*np.sin(4/3 - 2*t) - 4103/4*np.sin(9/7 -t) - 46877/9) *np.heaviside(31*PI -t, c) *np.heaviside(t - 27*PI, c) + (-7485/4*np.sin(5/9 -t) 
      + 1909/9*np.sin(2*t + 34/9) + 2861/4*np.sin(3*t + 23/5) + 11/2*np.sin(4*t + 7/2) + 111/8*np.sin(5*t + 12/7) 
      + 511/8*np.sin(6*t + 16/15) + 180/7*np.sin(7*t + 11/4) + 279/4*np.sin(8*t + 17/5) + 76/5*np.sin(9*t + 81/20) 
      - 16919/11) *np.heaviside(27*PI -t, c) *np.heaviside(t - 23*PI, c) + (-71/13*np.sin(1/2 - 11*t) - 119/6*np.sin(17/16 - 6*t) - 292/7*np.sin(10/7 - 5*t)
       - 64/13*np.sin(3/5 - 3*t) - 1493/3*np.sin(2/7 -t) + 1883/8*np.sin(2*t + 7/6) + 171/7*np.sin(4*t + 32/9) + 251/25*np.sin(7*t + 1) 
       + 35/2*np.sin(8*t + 16/7) + 117/10*np.sin(9*t + 15/4) + 43/9*np.sin(10*t + 29/8) + 43/9*np.sin(12*t + 20/13) 
       - 65269/8) *np.heaviside(23*PI -t, c) *np.heaviside(t - 19*PI, c) + (-174/5*np.sin(4/7 - 8*t) - 4532/23*np.sin(5/6 - 6*t) + 36005/17*np.sin(t + 25/9) 
       + 2164/5*np.sin(2*t + 35/9) + 1376/5*np.sin(3*t + 13/7) + 1164/5*np.sin(4*t + 28/9) + 277/3*np.sin(5*t + 19/5) 
       + 539/4*np.sin(7*t + 3/10) + 839/12*np.sin(9*t + 26/9) + 23/5*np.sin(10*t + 8/3) + 901/22*np.sin(11*t + 11/5) 
       + 163/5*np.sin(12*t + 5/9) + 135/7*np.sin(13*t + 9/2) - 11569/2) *np.heaviside(19*PI -t, c) *np.heaviside(t - 15*PI, c) + (-5801/5*np.sin(5/11 -t) 
       + 171/7*np.sin(2*t + 21/5) + 782/9*np.sin(3*t + 17/4) - 7576/5) *np.heaviside(15*PI -t, c) *np.heaviside(t - 11*PI, c) 
       + (-34/3*np.sin(1 - 4*t) - 838/7*np.sin(1/2 - 2*t) + 7788/7*np.sin(t + 2/5) + 1055/7*np.sin(3*t + 11/7) 
       + 219/10*np.sin(5*t + 19/5) + 194/7*np.sin(6*t + 49/11) - 7441/5) *np.heaviside(11*PI -t, c) *np.heaviside(t - 7*PI, c) + (-209/2*np.sin(5/6 - 8*t) 
       + 58085/14*np.sin(t + 21/8) + 5813/3*np.sin(2*t + 26/7) + 25709/7*np.sin(3*t + 10/7) + 6831/8*np.sin(4*t + 9/4) 
       + 3693/10*np.sin(5*t + 38/13) + 6453/7*np.sin(6*t + 30/7) + 1996/11*np.sin(7*t + 16/5) + 3541/22*np.sin(9*t + 5/4) 
       + 2263/29*np.sin(10*t + 35/18) + 4279/46*np.sin(11*t + 1/5) + 523/4*np.sin(12*t + 21/5) + 326/7*np.sin(13*t + 21/8) 
       + 396/7*np.sin(14*t + 21/5) + 1446/17*np.sin(15*t + 2/3) + 1971/5) *np.heaviside(7*PI -t, c) *np.heaviside(t - 3*PI, c) + (-938/5*np.sin(8/9 - 7*t) 
       + 26701/4*np.sin(t + 18/7) + 8911/33*np.sin(2*t + 7/2) + 4615/6*np.sin(3*t + 32/7) + 18102/23*np.sin(4*t + 12/5) 
       + 1129/7*np.sin(5*t + 13/4) + 473/7*np.sin(6*t + 10/7) + 671/7*np.sin(8*t + 1/14) + 7/4*np.sin(9*t + 9/2) 
       + 491/9*np.sin(10*t + 29/14) - 19490/3) *np.heaviside(3*PI -t, c) *np.heaviside(t +PI, c)) *np.heaviside(np.sqrt(np.sign(np.sin(t/2))), c)

# 媒介変数の定義
u = np.arange(0, 76*PI, 76*PI/16000)

# X, Yそれぞれの値を計算
x = x_func(u)
y = y_func(u)

# 描画用のオブジェクトを作成
fig, ax = plt.subplots()

# 描画範囲の縦横比を1:1に設定
ax.set_aspect('equal')

# グラフのタイトル
ax.set_title("Darth Vader")

# プロット
ax.plot(x, y, color='black')

# プロットした結果を表示する
plt.show()

# 画像として保存する（この場合はplt.show()をコメントアウトする）
# plt.savefig("darth_vader.png", format='png')