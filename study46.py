#
# 题目：求输入数字的平方，如果平方运算后小于 50 则退出。
# 程序分析：无
#

import math

N = 50
flag = True
print('如果输入的数字平方运算后小于 %d，程序将停止运行!'%N)
while flag:
    num = int(input('请输入一个数字：'))
    val = int(math.pow(num, 2))
    print('运算结果：%d'%val)
    if val >= N:
        flag = True
    else:
        flag = False
    


