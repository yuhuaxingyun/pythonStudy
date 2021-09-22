#
# 题目：一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。
# 程序分析：无。
#


def palindromeNum(s):
    x = str(s)
    if len(str(s)) %2 == 0:
        print('回文数必须为奇数位！')
        s = int(input('请输入一个数字：'))
        palindromeNum(s)
    else: 
        flag = True
        for i in range(len(x)//2):
            if x[i] != x[-i-1]:
                flag = False
                break

        if flag:
            print('%d 是一个回文数'%s)
        else:
            print('%d 不是一个回文数'%s)
     

s = int(input('请输入一个数字：'))
palindromeNum(s)