#!/usr/bin/python
# -*- coding: utf-8 -*-


from Tkinter import *
import hashlib
import time


init_window_name = Tk()
init_window_name.title("花好月圆_v_1.1.1.1")           #窗口名

# listb = Listbox(init_window_name)  # 创建两个列表组件
# listb.insert(0,'aaa')
# listb.insert(0,'bbb')

# li     = ['C','python','php','html','SQL','java']
# movie  = ['CSS','jQuery','Bootstrap']
listb  = Listbox(init_window_name)          #  创建两个列表组件
# listb2 = Listbox(init_window_name)
# for item in li:                 # 第一个小部件插入数据
#     listb.insert(0,item)




la = [2, 16, 30, 76]  # 分隔
lb = [13, 27, 41, 44, 52, 60, 69]  # 换行
lc = [14, 28, 42, 45, 53, 61, 70]  # 空格

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


for i in la:
    w1 = Message(init_window_name, text=i, width=100)
    w1.pack()
    time.sleep(1)

init_window_name.mainloop()
# init_window_name.mainloop()

