#!/usr/bin/python
# coding:gbk
# -*- coding: utf-8 -*-

# turtle 是python中一个很流行的绘制图像的函数库
from turtle import *
import time
import sys

#################################### 问候语 #######################################
print

la = [2, 16, 30, 76]  # 分隔
lb = [13, 27, 41, 44, 52, 60, 69]  # 换行
lc = [14, 28, 42, 45, 53, 61, 70]  # 空格

print "To 陈小婷："
print '    ',

time.sleep(1)
getting = [
    '也', '许', '，', '天', '荒', '地', '老', '只', '是', '一', '种', '传', '说', '；',
    '也', '许', '，', '牵', '手', '白', '头', '只', '是', '一', '种', '寂', '寞', '；',
    '也', '许', '，', '相', '濡', '以', '沫', '只', '是', '一', '种', '承', '诺', '。',
    '可', '是', '，',
    '在', '平', '凡', '的', '尘', '世', '间', ',',
    '在', '平', '淡', '的', '日', '子', '里', '，',
    '对', '你', '的', '心', '永', '不', '改', '变', '！',
    '今', '天', '是', '元', '宵', '节', '，', '祝', '你', '团', '团', '圆', '圆', '，', '甜', '甜', '蜜', '蜜', '！', '！', '！'
]
for i in range(91):
    if i in lc:
        print '    ',

    if i - 1 in la:
        time.sleep(1)
    elif i - 1 in lb:
        time.sleep(2)
    else:
        time.sleep(0.1)

    sys.stdout.write(getting[i])

    if i in lb:
        print

print
time.sleep(0.8)
print
print '                            ———— 占伟龙'
print '                            ———— 2021年2月26日'
print
time.sleep(2)
#################################################################################


pen_color = "#CDC5BF"  # black
fill_color_1 = 'hotpink'  # 'hotpink'  # red
fill_color_2 = "green"  # green

setup(600, 700, 100, 100)  # 画布的高度、宽度、起始xy的位置
bgcolor("black")

pensize(1)  # 画笔的粗细
speed(5)  # 画笔的速度，范围0-10

# time.sleep(2)  # 等待2秒钟
pencolor("#CDC5BF")  # 画笔颜色
penup()  # 提起画笔
# fd(90)  # 向前方向运行的像素
seth(90)  # 逆时针旋转的角度
fd(240)  # 向前方向运行的像素
seth(0)
pendown()

speed(5)  # 画笔的速度，范围0-10
begin_fill()
fillcolor(fill_color_1)

seth(90)  # 逆时针旋转的角度
circle(10, 270, 8)  # 按 半径和角度画圆
circle(50, 30)  # 按 半径和角度画圆

for i in range(10):
    fd(1)
    left(10)

circle(40, 40)

for i in range(6):
    fd(1)
    left(3)

circle(80, 40)

for i in range(20):
    fd(0.5)
    left(5)

circle(80, 45)

for i in range(10):
    fd(2)
    left(1)

circle(80, 25)

for i in range(20):
    fd(1)
    left(4)

circle(50, 50)

time.sleep(0.1)

circle(120, 55)

speed(0)

seth(-90)
fd(70)

right(150)
fd(20)

left(140)
circle(140, 90)

left(30)
circle(160, 100)

left(130)
fd(25)

penup()
right(150)
circle(40, 80)
pendown()

left(115)
fd(60)

penup()
left(180)
fd(60)
pendown()

end_fill()

right(120)
circle(-50, 50)
circle(-20, 90)

speed(1)
fd(75)

speed(0)
circle(90, 110)

penup()
left(162)
fd(185)
left(170)
pendown()
circle(200, 10)
circle(100, 40)
circle(-52, 115)
left(20)

pensize(4)  # 树枝
pencolor("#6B8E23")

circle(100, 20)
circle(300, 20)
speed(1)
fd(250)

penup()
speed(0)
left(180)
fd(250)
circle(-300, 7)
right(80)
circle(200, 5)
pendown()

left(60)
begin_fill()
fillcolor(fill_color_2)
circle(-80, 100)
right(90)
fd(10)
left(20)
circle(-63, 127)
end_fill()

penup()
left(50)
fd(20)
left(180)

pendown()
circle(200, 25)

penup()
right(150)

fd(180)

right(40)
pendown()
begin_fill()
fillcolor(fill_color_2)
circle(-100, 80)
right(150)
fd(10)
left(60)
circle(-80, 98)
end_fill()

penup()
left(60)
fd(13)
left(180)

pendown()
speed(1)
circle(-200, 23)

penup()
speed(10)
fd(500)  # 移走 海龟

# time.sleep(1)
# bgpic(r'src/3.gif')  # 插入图片
# time.sleep(1)

bgcolor("white")
time.sleep(0.8)
bgcolor("black")
time.sleep(0.5)
bgcolor("white")
time.sleep(0.3)
bgcolor("black")
time.sleep(0.2)
bgcolor("white")
time.sleep(0.1)
bgcolor("black")



exitonclick()
