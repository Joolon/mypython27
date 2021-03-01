#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = "Jolon"

from Tkinter import *


rootW = Tk()

label = Label(rootW, text='Hello world')
label.config(cursor='gumby')  # 配置外观（有哪些可以配置查看API文档）
label.config(width=80,height=10,fg='yellow',bg='darkgreen')
label.config(font=('times','28','bold'))
label.pack()

rootW.mainloop()