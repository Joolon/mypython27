#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = "Jolon"

from Tkinter import *


def callback():
    print 'called the menu'


rootW = Tk()

# 添加菜单栏
menu = Menu(rootW)
rootW.config(menu=menu)

# 在菜单栏上添加子菜单
fileMenu = Menu(menu)
menu.add_cascade(label='File', menu=fileMenu)  # 添加菜单

fileMenu.add_command(label='New', command=callback)  # 给菜单添加命令（即是可选项）
fileMenu.add_command(label='Open...', command=callback)
fileMenu.add_separator()  # 添加分割线
fileMenu.add_command(label='Exit', command=callback)

# 在菜单栏上添加子菜单
helpMenu = Menu(menu)
menu.add_cascade(label='Help', menu=helpMenu)
helpMenu.add_command(label='About...', command=callback)

rootW.mainloop()
