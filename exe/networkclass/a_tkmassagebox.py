#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = "Jolon"

from Tkinter import *
import tkMessageBox  # tk消息组件：弹出窗体

root = Tk()


def callback():
    if tkMessageBox.askyesno('sundy', 'Hi Sundy'):
        print 'cliked yes'
    else:
        print 'clicked no'


button = Button(root, text='button1', command=callback)
button.pack()
root.mainloop()
