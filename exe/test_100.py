#!/usr/bin/python
# coding:gbk
import time

# 题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
numbers_range = [1, 2, 3, 4]
print numbers_range
res_combine_number = []
for i in numbers_range:
    for j in numbers_range:
        for k in numbers_range:
            if(i != j) and (j != k) and (i != k):
                res_combine_number.append(i * 100 + j * 10 + k)

print res_combine_number


# 题目：企业发放的奖金根据利润提成。
# 利润(I)低于或等于10万元时，奖金可提10%；
# 利润高于10万元，低于20万元时，低于10万元的部分按10%提成;高于10万元的部分，可提成7.5%；
# 20万到40万之间时，高于20万元的部分，可提成5%；
# 40万到60万之间时高于40万元的部分，可提成3%；
# 60万到100万之间时，高于60万元的部分，可提成1.5%;
# 高于100万元时，超过100万元的部分按1%提成
# 从键盘输入当月利润I，求应发放奖金总数？
# 使用数轴来分界，定位
def get_total_bonus(my_profit):
    total_bonus = 0
    rate = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]
    prof = [1000000, 600000, 400000, 200000, 100000, 0]

    for idx in range(0, 6):
        if my_profit > prof[idx]:
            total_bonus += (my_profit - prof[idx]) * rate[idx]
            my_profit = prof[idx]
    return total_bonus


# inp_profit = int(raw_input('请输入利润：'))
inp_profit = 1000
my_bonus = get_total_bonus(inp_profit)
print my_bonus

# 题目：一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
# 分析：假设这个数为 x，
# 则 x + 100 = n的平方,x + 100 + 168 = m的平方
# 则 (m + n)(m - n) = 168
# 因为 m,n都是整数，所以 m-n 是整数，则 m-n>=1 则 m+n <=168,则 m<168
# 就可以计算出 m,n
x = []
for m in range(1,168):
    for n in range(1,168):
        if (m + n) * (m - n) == 168:
            print 'm:', m, 'n:', n, 'm+n:', m + n, 'm-n:', m - n, 'x:', n * n - 100
            x.append(n * n - 100)
print x


# 题目：输入某年某月某日，判断这一天是这一年的第几天？
# 分析：设置每个月的天数，再根据数轴分界，计算
# 闰年（能被4整除且不能被100整除或能被400整除）
per_month_the_days1 = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# 平年
per_month_the_days2 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# year = int(raw_input("输入年份："))
# month = int(raw_input('输入月份：'))
# day = int(raw_input('输入天：'))

year = 10
month = 10
day = 10

if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
    per_month_the_days = per_month_the_days1
else:
    per_month_the_days = per_month_the_days2

print per_month_the_days

total_day = 0  # 第几天

for i in range(month - 1, 0, -1):
    total_day += per_month_the_days[i-1]
    print per_month_the_days[i-1]

total_day += day
print total_day


# 题目：输入三个整数x,y,z，请把这三个数由小到大输出。
# ll = []
# for i in range(1,4):
#     li = int(raw_input("请输入第 " + str(i) + " 个数："))
#     ll.append(li)
#
# ll.sort()
# print ll

# 斐波那契数列
# 1,1,2,3,5,8,13,21,34,55
# length = int(raw_input("请输入数列长度："))
length = 10
fbnqsl = []
for i in range(0,length):
    if i == 0 or i == 1:
        fbnqsl.append(1)
    else:
        ss = fbnqsl[i-1] + fbnqsl[i-2]
        fbnqsl.append(ss)

print fbnqsl


# 输出 9*9 乘法口诀表
for i in range(1, 10):
    print
    for j in range(1, i+1):
        print "%d*%d=%d" % (i, j, i*j),
print

# 暂停一秒输出。
myD = {1: 'a', 2: 'b'}
for key, value in dict.items(myD):
    time.sleep(1)
    print "%s %s" % (key, value)

# 题目：古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？
# 其实是 斐波那契数列



