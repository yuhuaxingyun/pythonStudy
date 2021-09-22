#
# 题目：打印出如下图案（菱形）:
#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *
# 程序分析：先把图形分成两部分来看待，前四行一个规律，后三行一个规律，利用双重for循环，第一层控制行，第二层控制列。
#

Warning('还有bug')

from sys import stdout

def diamondNum(count):
    if count < 3:
        print('菱形的层数必须大于2！')
        num = int(input('请输入菱形的层数(大于2)：'))
        diamondNum(num) 
    elif (count%2 == 0) :
        print('菱形的层数必须为奇数！')
        num = int(input('请输入菱形的层数(奇数)：'))
        diamondNum(num) 
    else:    
        num1 = int((count-1)/2 + 1)
        num2 = int((count-1)/2)
        for i in range(num1):
            for j in range(2 - i + 1):
                stdout.write(' ')
            for k in range(2 * i + 1):
                stdout.write('*')
            print('')
    
        for i in range(num2):
            for j in range(i + 1):
                stdout.write(' ')
            for k in range(num1 - 2 * i + 1):
                stdout.write('*')
            print('')

count = int(input('请输入菱形的层数(奇数且大于0)：'))
diamondNum(count)    
            
        
    