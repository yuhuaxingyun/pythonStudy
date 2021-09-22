#
# 题目：某个公司采用公用电话传递数据，数据是四位的整数，在传递过程中是加密的，加密规则如下：每位数字都加上5,然后用和除以10的余数代替该数字，再将第一位和第四位交换，第二位和第三位交换。
# 程序分析：无。
#

import math
from sys import stdout

if __name__ == '__main__':
    aArray = []
    a = int(input('请输入四位的整数：\n'))
    aArray.append(a%10)
    aArray.append(a%100//10)
    aArray.append(a%1000//100)
    aArray.append(a//1000)

    print(aArray)
    for i in range(4):
        aArray[i] += 5
        aArray[i] %= 10
    for i in range(2):
        aArray[i],aArray[3-i] = aArray[3-i],aArray[i]
    for i in range(3,-1,-1):
        stdout.write(str(aArray[i]))
        
         