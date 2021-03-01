#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = "Jolon"

from Tkinter import *
import tkMessageBox  # tk消息组件：弹出窗体

root = Tk()
Label(root, text='First Grid').grid(row=0)
Label(root, text='Second Grid').grid(row=1)

e1 = Entry(root)
e2 = Entry(root)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

Button(root, text='OK').grid(row=2)
# root.mainloop()

statusBar = Label(root, text='Ln20', bd=1, relief=SUNKEN, anchor=W)
statusBar.pack(side=BOTTOM, fill=X)  # X轴填充

root.mainloop()
