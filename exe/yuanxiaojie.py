#!/usr/bin/python
# coding:gbk
# -*- coding: utf-8 -*-

# turtle ��python��һ�������еĻ���ͼ��ĺ�����
from turtle import *
import time
import sys

#################################### �ʺ��� #######################################
print

la = [2, 16, 30, 76]  # �ָ�
lb = [13, 27, 41, 44, 52, 60, 69]  # ����
lc = [14, 28, 42, 45, 53, 61, 70]  # �ո�

print "To ��С�ã�"
print '    ',

time.sleep(1)
getting = [
    'Ҳ', '��', '��', '��', '��', '��', '��', 'ֻ', '��', 'һ', '��', '��', '˵', '��',
    'Ҳ', '��', '��', 'ǣ', '��', '��', 'ͷ', 'ֻ', '��', 'һ', '��', '��', 'į', '��',
    'Ҳ', '��', '��', '��', '�', '��', 'ĭ', 'ֻ', '��', 'һ', '��', '��', 'ŵ', '��',
    '��', '��', '��',
    '��', 'ƽ', '��', '��', '��', '��', '��', ',',
    '��', 'ƽ', '��', '��', '��', '��', '��', '��',
    '��', '��', '��', '��', '��', '��', '��', '��', '��',
    '��', '��', '��', 'Ԫ', '��', '��', '��', 'ף', '��', '��', '��', 'Բ', 'Բ', '��', '��', '��', '��', '��', '��', '��', '��'
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
print '                            �������� ռΰ��'
print '                            �������� 2021��2��26��'
print
time.sleep(2)
#################################################################################


pen_color = "#CDC5BF"  # black
fill_color_1 = 'hotpink'  # 'hotpink'  # red
fill_color_2 = "green"  # green

setup(600, 700, 100, 100)  # �����ĸ߶ȡ���ȡ���ʼxy��λ��
bgcolor("black")

pensize(1)  # ���ʵĴ�ϸ
speed(5)  # ���ʵ��ٶȣ���Χ0-10

# time.sleep(2)  # �ȴ�2����
pencolor("#CDC5BF")  # ������ɫ
penup()  # ���𻭱�
# fd(90)  # ��ǰ�������е�����
seth(90)  # ��ʱ����ת�ĽǶ�
fd(240)  # ��ǰ�������е�����
seth(0)
pendown()

speed(5)  # ���ʵ��ٶȣ���Χ0-10
begin_fill()
fillcolor(fill_color_1)

seth(90)  # ��ʱ����ת�ĽǶ�
circle(10, 270, 8)  # �� �뾶�ͽǶȻ�Բ
circle(50, 30)  # �� �뾶�ͽǶȻ�Բ

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

pensize(4)  # ��֦
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
fd(500)  # ���� ����

# time.sleep(1)
# bgpic(r'src/3.gif')  # ����ͼƬ
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
