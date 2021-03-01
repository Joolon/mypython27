#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = "Jolon"

from Tkinter import *

root = Tk()

def callback():
    print 'called the menu'

toobar = Frame(root)
b = Button(toobar,text='new',width=6,command=callback())
b.pack(side=LEFT,padx=2,pady=2)

c = Button(toobar,text='new',width=6,command=callback())
c.pack(side=LEFT,padx=2,pady=2)

toobar.pack(side=TOP,fill=X)
root.mainloop()