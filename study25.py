#
# 题目：求1+2!+3!+...+20!的和。
# 程序分析：此程序只是把累加变成了累乘。
#

#!/usr/bin/python
# -*- coding: UTF-8 -*-

def factorialSum(num):
    s = 0
    t = 1
    for n in range(1,num+1):
        t *= n
        s += t

    print('1~%d的阶乘和为：%d'%(num,s))
    
num = int(input('请输入阶乘的数(包含)：'))
factorialSum(num)
