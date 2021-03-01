#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = "Jolon"

from Tkinter import *

button = Button(text='SundyButton', padx=10, pady=10)
button.config(cursor='gumby')
button.config(bd=8, relief=RAISED)
button.config(fg='yellow', bg='green')
button.config(font=('Helvetica', 18, 'bold italic'))
button.pack()
button.mainloop()
