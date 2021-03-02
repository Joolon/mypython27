#!/usr/bin/python
# -*- coding=utf-8 -*-

from Tkinter import *
import tkMessageBox
import math


class Calculator:
    ' 计算器类 '
    def __init__(self, width=290, height=400):
        # 创建主界面
        self.win = Tk()
        self.win.title('我是一只菜菜菜鸟...')
        self.win.geometry(str(width) + 'x' + str(height))

        self.menu = Menu(self.win)
        self.ShowMenu()
        self.latest_sign_flag = 0  # 0表示上次按下的是数字键，1表示上次按下的是操作符键

    def ShowMenu(self):
        '显示菜单栏'
        self.win.config(menu=self.menu)

        sub_switch = Menu(self.menu)
        self.menu.add_cascade(label='≡', menu=sub_switch)

        sub_switch.add_command(label='计算器', command=self.subViewFun1)
        sub_switch.add_command(label='  标准', command=self.subViewFun2)
        sub_switch.add_command(label='  科学', command=self.subViewFun3)
        sub_switch.add_command(label='  日期计算', command=self.subViewFun4)

        sub_view = Menu(self.menu)
        self.menu.add_cascade(label='编辑(E)', menu=sub_view)
        sub_view.add_command(label='重做', command=self.subViewFun1)
        sub_view.add_command(label='撤销', command=self.subViewFun1)

        sub_help = Menu(self.menu)
        self.menu.add_cascade(label='帮助(H)', menu=sub_help)
        sub_help.add_command(label='使用手册', command=self.subViewFun1)
        sub_help.add_command(label='联系我们', command=self.subViewFun1)

        space_bar = Label(self.win)
        space_bar.pack(side=TOP, fill=X)

    def showResultInfo(self):
        '显示操作结果展示栏'
        self.operator_value_1 = StringVar()
        self.operator_1 = Entry(self.win, textvariable=self.operator_value_1, font=('Arial', 20), justify=RIGHT)
        self.operator_1.place(x=10, y=0, width=85, height=25)

        self.operator_value_2 = StringVar()
        self.operator_2 = Entry(self.win, textvariable=self.operator_value_2, font=('Arial', 20), justify=RIGHT)
        self.operator_2.place(x=102, y=0, width=85, height=25)

        self.operator_value_3 = StringVar()
        self.operator_3 = Entry(self.win, textvariable=self.operator_value_3, font=('Arial', 20), justify=RIGHT)
        self.operator_3.place(x=195, y=0, width=85, height=25)

        self.input_value_1 = StringVar()
        self.edit_input_1 = Entry(self.win, textvariable=self.input_value_1, font=('Arial', 18), justify=RIGHT)
        self.edit_input_1.place(x=10, y=30, width=270, height=30)

    def softKeyboard(self):
        '显示软键盘'
        padxV = 10
        padyV = 10
        widthV = 50
        heightV = 50
        button_1_1 = Button(text='MC', padx=padxV, pady=padyV, command=lambda: self.pressCalculate('MC'))
        button_1_2 = Button(text='MR', padx=padxV, pady=padyV, command=lambda: self.pressCalculate('MR'))
        button_1_3 = Button(text='MS', padx=padxV, pady=padyV, command=lambda: self.pressCalculate('MS'))
        button_1_4 = Button(text='M+', padx=padxV, pady=padyV, command=lambda: self.pressCalculate('M+'))
        button_1_5 = Button(text='M-', padx=padxV, pady=padyV, command=lambda: self.pressCalculate('M-'))

        button_2_1 = Button(text='←', padx=padxV, pady=padyV, command=lambda: self.pressCalculate('BACK'))
        button_2_2 = Button(text='CE', padx=padxV, pady=padyV, command=lambda: self.pressCalculate('CE'))
        button_2_3 = Button(text='C', padx=padxV, pady=padyV, command=lambda: self.pressCalculate('C'))
        button_2_4 = Button(text='±', padx=padxV, pady=padyV, command=lambda: self.pressCalculate('ADD_SUB_COMBINE'))
        button_2_5 = Button(text='√', padx=padxV, pady=padyV, command=lambda: self.pressCalculate('√'))

        button_3_1 = Button(text='7', padx=padxV, pady=padyV, command=lambda: self.pressNum('7'))
        button_3_2 = Button(text='8', padx=padxV, pady=padyV, command=lambda: self.pressNum('8'))
        button_3_3 = Button(text='9', padx=padxV, pady=padyV, command=lambda: self.pressNum('9'))
        button_3_4 = Button(text='/', padx=padxV, pady=padyV, command=lambda: self.pressCalculate('/'))
        button_3_5 = Button(text='//', padx=padxV, pady=padyV, command=lambda: self.pressCalculate('//'))

        button_4_1 = Button(text='4', padx=padxV, pady=padyV, command=lambda: self.pressNum('4'))
        button_4_2 = Button(text='5', padx=padxV, pady=padyV, command=lambda: self.pressNum('5'))
        button_4_3 = Button(text='6', padx=padxV, pady=padyV, command=lambda: self.pressNum('6'))
        button_4_4 = Button(text='*', padx=padxV, pady=padyV, command=lambda: self.pressCalculate('*'))
        button_4_5 = Button(text='1/x', padx=padxV, pady=padyV, command=lambda: self.pressCalculate('1/x'))

        button_5_1 = Button(text='1', padx=padxV, pady=padyV, command=lambda: self.pressNum('1'))
        button_5_2 = Button(text='2', padx=padxV, pady=padyV, command=lambda: self.pressNum('2'))
        button_5_3 = Button(text='3', padx=padxV, pady=padyV, command=lambda: self.pressNum('3'))
        button_5_4 = Button(text='-', padx=padxV, pady=padyV, command=lambda: self.pressCalculate('-'))
        button_5_5 = Button(text='=', padx=padxV, pady=padyV, command=lambda: self.pressCalculate('='))

        button_6_1 = Button(text='0', padx=padxV, pady=padyV, command=lambda: self.pressNum('0'))
        button_6_2 = Button(text='.', padx=padxV, pady=padyV, command=lambda: self.pressNum('.'))
        button_6_3 = Button(text='+', padx=padxV, pady=padyV, command=lambda: self.pressCalculate('+'))

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

    def pressNum(self, num):
        '按下 数字键'
        if self.latest_sign_flag == 1:
            self.operator_1.delete(0, END)
            self.operator_1.insert(0, self.operator_2.get())
            self.operator_2.delete(0, END)
            self.operator_2.insert(0, self.operator_3.get())

        if self.edit_input_1.get() != '' and float(self.edit_input_1.get()) == 0:
            self.edit_input_1.delete(0, END)
            self.edit_input_1.insert(END, str(num))
        else:
            self.edit_input_1.insert(END, str(num))

        self.operator_3.delete(0, END)
        self.operator_3.insert(0, self.edit_input_1.get())

        self.latest_sign_flag = 0

    def pressCalculate(self, sign):
        '按下操作键'
        sign = str(sign)

        if sign == 'C':
            self.edit_input_1.delete(0, END)
            self.edit_input_1.insert(0, 0)
            self.operator_1.delete(0, END)
            self.operator_2.delete(0, END)
            self.operator_3.delete(0, END)

        elif sign == 'CE':
            self.edit_input_1.delete(0, END)
            self.edit_input_1.insert(0, 0)

        elif sign == 'BACK':
            edit_input_1_length = len(self.edit_input_1.get())
            self.edit_input_1.delete(edit_input_1_length - 1)

        elif sign in ['+', '-', '*', '/']:
            self.changeShowText(sign)  # 重置 显示框

        elif sign in ['=', '1/x', '√']:

            result = 'NULL'

            if sign == '=':
                var_1 = float(self.operator_1.get())
                var_2 = self.operator_2.get()
                var_3 = float(self.operator_3.get())
                if var_2 == '+':
                    result = var_1 + var_3

                elif var_2 == '-':
                    result = var_1 - var_3

                elif var_2 == '*':
                    result = var_1 * var_3

                elif var_2 == '/':
                    result = var_1 / var_3

            elif sign == '√':
                self.changeShowText(sign)  # 重置 显示框
                var_2 = float(self.operator_2.get())
                var_3 = self.operator_3.get()
                result = math.sqrt(var_2)

            elif sign == '1/x':
                self.changeShowText(sign)  # 重置 显示框
                var_2 = float(self.operator_2.get())
                var_3 = self.operator_3.get()
                result = 1 / var_2

            self.edit_input_1.delete(0, END)
            self.edit_input_1.insert(0, result)

    def changeShowText(self, sign):
        '重置 显示框'
        self.operator_1.delete(0, END)
        self.operator_1.insert(0, self.operator_2.get())

        self.operator_2.delete(0, END)
        self.operator_2.insert(0, self.edit_input_1.get())

        self.operator_3.delete(0, END)
        self.operator_3.insert(0, str(sign))

        self.edit_input_1.delete(0, END)

        self.latest_sign_flag = 1

    def subViewFun1(self):
        '展示提示信息：未实现的功能'
        tkMessageBox.showinfo('提示', '您点击了计算器')

    def subViewFun2(self):
        '展示提示信息：未实现的功能'
        tkMessageBox.showinfo('提示', '您点击了标准')

    def subViewFun3(self):
        '展示提示信息：未实现的功能'
        tkMessageBox.showinfo('提示', '您点击了科学')

    def subViewFun4(self):
        '展示提示信息：未实现的功能'
        tkMessageBox.showinfo('提示', '您点击了日期计算')


# 展示计算机功能界面
calcul = Calculator(290, 400)
calcul.showResultInfo()
calcul.softKeyboard()
calcul.win.mainloop()
