#!/usr/bin/python
# coding:gbk
import time

# ��Ŀ�����ĸ����֣�1��2��3��4������ɶ��ٸ�������ͬ�����ظ����ֵ���λ�������Ƕ��٣�
numbers_range = [1, 2, 3, 4]
print numbers_range
res_combine_number = []
for i in numbers_range:
    for j in numbers_range:
        for k in numbers_range:
            if(i != j) and (j != k) and (i != k):
                res_combine_number.append(i * 100 + j * 10 + k)

print res_combine_number


# ��Ŀ����ҵ���ŵĽ������������ɡ�
# ����(I)���ڻ����10��Ԫʱ���������10%��
# �������10��Ԫ������20��Ԫʱ������10��Ԫ�Ĳ��ְ�10%���;����10��Ԫ�Ĳ��֣������7.5%��
# 20��40��֮��ʱ������20��Ԫ�Ĳ��֣������5%��
# 40��60��֮��ʱ����40��Ԫ�Ĳ��֣������3%��
# 60��100��֮��ʱ������60��Ԫ�Ĳ��֣������1.5%;
# ����100��Ԫʱ������100��Ԫ�Ĳ��ְ�1%���
# �Ӽ������뵱������I����Ӧ���Ž���������
# ʹ���������ֽ磬��λ
def get_total_bonus(my_profit):
    total_bonus = 0
    rate = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]
    prof = [1000000, 600000, 400000, 200000, 100000, 0]

    for idx in range(0, 6):
        if my_profit > prof[idx]:
            total_bonus += (my_profit - prof[idx]) * rate[idx]
            my_profit = prof[idx]
    return total_bonus


# inp_profit = int(raw_input('����������'))
inp_profit = 1000
my_bonus = get_total_bonus(inp_profit)
print my_bonus

# ��Ŀ��һ��������������100����һ����ȫƽ�������ټ���168����һ����ȫƽ���������ʸ����Ƕ��٣�
# ���������������Ϊ x��
# �� x + 100 = n��ƽ��,x + 100 + 168 = m��ƽ��
# �� (m + n)(m - n) = 168
# ��Ϊ m,n�������������� m-n ���������� m-n>=1 �� m+n <=168,�� m<168
# �Ϳ��Լ���� m,n
x = []
for m in range(1,168):
    for n in range(1,168):
        if (m + n) * (m - n) == 168:
            print 'm:', m, 'n:', n, 'm+n:', m + n, 'm-n:', m - n, 'x:', n * n - 100
            x.append(n * n - 100)
print x


# ��Ŀ������ĳ��ĳ��ĳ�գ��ж���һ������һ��ĵڼ��죿
# ����������ÿ���µ��������ٸ�������ֽ磬����
# ���꣨�ܱ�4�����Ҳ��ܱ�100�������ܱ�400������
per_month_the_days1 = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# ƽ��
per_month_the_days2 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# year = int(raw_input("������ݣ�"))
# month = int(raw_input('�����·ݣ�'))
# day = int(raw_input('�����죺'))

year = 10
month = 10
day = 10

if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
    per_month_the_days = per_month_the_days1
else:
    per_month_the_days = per_month_the_days2

print per_month_the_days

total_day = 0  # �ڼ���

for i in range(month - 1, 0, -1):
    total_day += per_month_the_days[i-1]
    print per_month_the_days[i-1]

total_day += day
print total_day


# ��Ŀ��������������x,y,z���������������С���������
# ll = []
# for i in range(1,4):
#     li = int(raw_input("������� " + str(i) + " ������"))
#     ll.append(li)
#
# ll.sort()
# print ll

# 쳲���������
# 1,1,2,3,5,8,13,21,34,55
# length = int(raw_input("���������г��ȣ�"))
length = 10
fbnqsl = []
for i in range(0,length):
    if i == 0 or i == 1:
        fbnqsl.append(1)
    else:
        ss = fbnqsl[i-1] + fbnqsl[i-2]
        fbnqsl.append(ss)

print fbnqsl


# ��� 9*9 �˷��ھ���
for i in range(1, 10):
    print
    for j in range(1, i+1):
        print "%d*%d=%d" % (i, j, i*j),
print

# ��ͣһ�������
myD = {1: 'a', 2: 'b'}
for key, value in dict.items(myD):
    time.sleep(1)
    print "%s %s" % (key, value)

# ��Ŀ���ŵ����⣺��һ�����ӣ��ӳ������3������ÿ���¶���һ�����ӣ�С���ӳ����������º�ÿ��������һ�����ӣ��������Ӷ���������ÿ���µ���������Ϊ���٣�
# ��ʵ�� 쳲���������



