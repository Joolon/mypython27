#!/usr/bin/python
# -*- coding=utf-8 -*-

from Tkinter import *
import tkMessageBox
import math

win = Tk()
win.title('Simple calculator')
win.geometry('290x400')

menu = Menu(win)

win.config(menu=menu)

latest_sign_flag = 0  # 0为数字，1位操作符
operator_list = ['+', '-', '*', '/']


def sub_view_fun_1():
    tkMessageBox.showinfo('提示', '您点击了计算器')


def sub_view_fun_2():
    tkMessageBox.showinfo('提示', '您点击了标准')


def sub_view_fun_3():
    tkMessageBox.showinfo('提示', '您点击了科学')


def sub_view_fun_4():
    tkMessageBox.showinfo('提示', '您点击了日期计算')


def presscalculate(sign):
    global latest_sign_flag
    # tkMessageBox.showinfo('提示', '您点击了符号 ' + str(sign))

    if str(sign) == 'C':
        edit_input_1.delete(0, END)
        edit_input_1.insert(0, 0)
        operator_1.delete(0, END)
        operator_2.delete(0, END)
        operator_3.delete(0, END)

    elif str(sign) == 'CE':
        edit_input_1.delete(0, END)
        edit_input_1.insert(0, 0)

    elif str(sign) == 'BACK':
        edit_input_1_length = len(edit_input_1.get())
        edit_input_1.delete(edit_input_1_length - 1)

    elif str(sign) in operator_list:
        # 重置 显示框
        operator_1.delete(0, END)
        operator_1.insert(0, operator_2.get())

        operator_2.delete(0, END)
        operator_2.insert(0, edit_input_1.get())

        operator_3.delete(0, END)
        operator_3.insert(0, str(sign))

        edit_input_1.delete(0, END)

        latest_sign_flag = 1

    elif str(sign) in ['=', '1/x', '√']:
        # 重置 显示框
        operator_1.delete(0, END)
        operator_1.insert(0, operator_2.get())

        operator_2.delete(0, END)
        operator_2.insert(0, edit_input_1.get())

        operator_3.delete(0, END)
        operator_3.insert(0, str(sign))

        edit_input_1.delete(0, END)

        latest_sign_flag = 1

        result = 'NULL'

        if str(sign) == '=':
            var_1 = float(operator_1.get())
            var_2 = operator_2.get()
            var_3 = float(operator_3.get())
            if var_2 == '+':
                result = var_1 + var_3

            elif var_2 == '-':
                result = var_1 - var_3

            elif var_2 == '*':
                result = var_1 * var_3

            elif var_2 == '/':
                result = var_1 / var_3


        elif str(sign) == '√':
            var_2 = float(operator_2.get())
            var_3 = operator_3.get()
            result = math.sqrt(var_2)

        elif str(sign) == '1/x':
            var_2 = float(operator_2.get())
            var_3 = operator_3.get()
            result = 1 / var_2

        edit_input_1.delete(0, END)
        edit_input_1.insert(0, result)


def pressnum(num):
    global latest_sign_flag
    # tkMessageBox.showinfo('提示', '您点击了数字 ' + str(num))

    if latest_sign_flag == 1:
        operator_1.delete(0, END)
        operator_1.insert(0, operator_2.get())
        operator_2.delete(0, END)
        operator_2.insert(0, operator_3.get())

    if edit_input_1.get() != '' and float(edit_input_1.get()) == 0:
        edit_input_1.delete(0, END)
        edit_input_1.insert(END, str(num))
    else:
        edit_input_1.insert(END, str(num))

    operator_3.delete(0, END)
    operator_3.insert(0, edit_input_1.get())

    latest_sign_flag = 0


# 菜单
sub_switch = Menu(menu)
menu.add_cascade(label='≡', menu=sub_switch)

sub_switch.add_command(label='计算器', command=sub_view_fun_1)
sub_switch.add_command(label='  标准', command=sub_view_fun_2)
sub_switch.add_command(label='  科学', command=sub_view_fun_3)
sub_switch.add_command(label='  日期计算', command=sub_view_fun_4)

sub_view = Menu(menu)
menu.add_cascade(label='编辑(E)', menu=sub_view)
sub_view.add_command(label='重做', command=sub_view_fun_1)
sub_view.add_command(label='撤销', command=sub_view_fun_1)

sub_help = Menu(menu)
menu.add_cascade(label='帮助(H)', menu=sub_help)
sub_help.add_command(label='使用手册', command=sub_view_fun_1)
sub_help.add_command(label='联系我们', command=sub_view_fun_1)

space_bar = Label(win)
space_bar.pack(side=TOP, fill=X)

operator_value_1 = StringVar()
operator_1 = Entry(win, textvariable=operator_value_1, font=('Arial', 20), justify=RIGHT)
operator_1.place(x=10, y=0, width=85, height=25)

operator_value_2 = StringVar()
operator_2 = Entry(win, textvariable=operator_value_2, font=('Arial', 20), justify=RIGHT)
operator_2.place(x=102, y=0, width=85, height=25)

operator_value_3 = StringVar()
operator_3 = Entry(win, textvariable=operator_value_3, font=('Arial', 20), justify=RIGHT)
operator_3.place(x=195, y=0, width=85, height=25)

input_value_1 = StringVar()
edit_input_1 = Entry(win, textvariable=input_value_1, font=('Arial', 18), justify=RIGHT)
edit_input_1.place(x=10, y=35, width=270, height=30)

# 软键盘
padxV = 10
padyV = 10
widthV = 50
heightV = 50
button_1_1 = Button(text='MC', padx=padxV, pady=padyV, command=lambda: presscalculate('MC'))
button_1_2 = Button(text='MR', padx=padxV, pady=padyV, command=lambda: presscalculate('MR'))
button_1_3 = Button(text='MS', padx=padxV, pady=padyV, command=lambda: presscalculate('MS'))
button_1_4 = Button(text='M+', padx=padxV, pady=padyV, command=lambda: presscalculate('M+'))
button_1_5 = Button(text='M-', padx=padxV, pady=padyV, command=lambda: presscalculate('M-'))

button_2_1 = Button(text='←', padx=padxV, pady=padyV, command=lambda: presscalculate('BACK'))
button_2_2 = Button(text='CE', padx=padxV, pady=padyV, command=lambda: presscalculate('CE'))
button_2_3 = Button(text='C', padx=padxV, pady=padyV, command=lambda: presscalculate('C'))
button_2_4 = Button(text='±', padx=padxV, pady=padyV, command=lambda: presscalculate('ADD_SUB_COMBINE'))
button_2_5 = Button(text='√', padx=padxV, pady=padyV, command=lambda: presscalculate('√'))

button_3_1 = Button(text='7', padx=padxV, pady=padyV, command=lambda: pressnum('7'))
button_3_2 = Button(text='8', padx=padxV, pady=padyV, command=lambda: pressnum('8'))
button_3_3 = Button(text='9', padx=padxV, pady=padyV, command=lambda: pressnum('9'))
button_3_4 = Button(text='/', padx=padxV, pady=padyV, command=lambda: presscalculate('/'))
button_3_5 = Button(text='//', padx=padxV, pady=padyV, command=lambda: presscalculate('//'))

button_4_1 = Button(text='4', padx=padxV, pady=padyV, command=lambda: pressnum('4'))
button_4_2 = Button(text='5', padx=padxV, pady=padyV, command=lambda: pressnum('5'))
button_4_3 = Button(text='6', padx=padxV, pady=padyV, command=lambda: pressnum('6'))
button_4_4 = Button(text='*', padx=padxV, pady=padyV, command=lambda: presscalculate('*'))
button_4_5 = Button(text='1/x', padx=padxV, pady=padyV, command=lambda: presscalculate('1/x'))

button_5_1 = Button(text='1', padx=padxV, pady=padyV, command=lambda: pressnum('1'))
button_5_2 = Button(text='2', padx=padxV, pady=padyV, command=lambda: pressnum('2'))
button_5_3 = Button(text='3', padx=padxV, pady=padyV, command=lambda: pressnum('3'))
button_5_4 = Button(text='-', padx=padxV, pady=padyV, command=lambda: presscalculate('-'))
button_5_5 = Button(text='=', padx=padxV, pady=padyV, command=lambda: presscalculate('='))

button_6_1 = Button(text='0', padx=padxV, pady=padyV, command=lambda: pressnum('0'))
button_6_2 = Button(text='.', padx=padxV, pady=padyV, command=lambda: pressnum('.'))
button_6_3 = Button(text='+', padx=padxV, pady=padyV, command=lambda: presscalculate('+'))

button_1_1.place(x=10, y=65, width=widthV, height=heightV)
button_1_2.place(x=65, y=65, width=widthV, height=heightV)
button_1_3.place(x=120, y=65, width=widthV, height=heightV)
button_1_4.place(x=175, y=65, width=widthV, height=heightV)
button_1_5.place(x=230, y=65, width=widthV, height=heightV)

button_2_1.place(x=10, y=120, width=widthV, height=heightV)
button_2_2.place(x=65, y=120, width=widthV, height=heightV)
button_2_3.place(x=120, y=120, width=widthV, height=heightV)
button_2_4.place(x=175, y=120, width=widthV, height=heightV)
button_2_5.place(x=230, y=120, width=widthV, height=heightV)

button_3_1.place(x=10, y=175, width=widthV, height=heightV)
button_3_2.place(x=65, y=175, width=widthV, height=heightV)
button_3_3.place(x=120, y=175, width=widthV, height=heightV)
button_3_4.place(x=175, y=175, width=widthV, height=heightV)
button_3_5.place(x=230, y=175, width=widthV, height=heightV)

button_4_1.place(x=10, y=230, width=widthV, height=heightV)
button_4_2.place(x=65, y=230, width=widthV, height=heightV)
button_4_3.place(x=120, y=230, width=widthV, height=heightV)
button_4_4.place(x=175, y=230, width=widthV, height=heightV)
button_4_5.place(x=230, y=230, width=widthV, height=heightV)

button_5_1.place(x=10, y=285, width=widthV, height=heightV)
button_5_2.place(x=65, y=285, width=widthV, height=heightV)
button_5_3.place(x=120, y=285, width=widthV, height=heightV)
button_5_4.place(x=175, y=285, width=widthV, height=heightV)
button_5_5.place(x=230, y=285, width=widthV, height=105)

button_6_1.place(x=10, y=340, width=105, height=heightV)
button_6_2.place(x=120, y=340, width=widthV, height=heightV)
button_6_3.place(x=175, y=340, width=widthV, height=heightV)

win.mainloop()
