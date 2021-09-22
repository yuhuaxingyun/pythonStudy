#
# 题目：利用递归方法求5!。
# 程序分析：递归公式：fn=fn_1*4!
#

def fact(j):
    sum = 0
    if j == 0:
        sum = 1
    else:
        sum = j * fact(j-1)
    return sum

def judgeNumber(num):
    if num < 0:
        print('请输入正整数!')
        num = int(input('请输入需要求的正整数阶乘：'))
        return judgeNumber(num)
    else:
        return fact(num) 

    
num = int(input('请输入需要求的正整数阶乘：'))
print(judgeNumber(num))        
    