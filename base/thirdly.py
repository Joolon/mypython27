# coding:utf-8

import time
import calendar
import math
from math import cos

dict = {"a":1,"b":2}
print dict

cos(1)



dict = {('Name'): 'Zara', 'Age': 7}

print "dict['Name']: ", dict['Name']

#time.sleep(2)

localtime = time.localtime(time.time())
print "The localtime is:" , localtime

cal = calendar.month(2021,4)
print cal


def printme(name,age):
    "print char"
    print "name:",name
    print "age:",age
    return


printme(age='30',name='jolon')


def printinfo(*params ):
   "print any input params"
   print "Output: "
   for var in params:
      print var
   return


printinfo(1,2,3)

Money = 2000


def AddMoney():
    global Money
    Money = Money + 1




print Money
AddMoney()
print Money

content = dir(math)
print content


str = raw_input("Please input simple characters:")
str2 = input("Please input any python 啊啊啊:")
print str
print str2