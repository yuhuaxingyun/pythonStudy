#
# 题目：判断101-200之间有多少个素数，并输出所有素数。
# 程序分析：判断素数的方法：用一个数分别去除2到sqrt(这个数)，如果能被整除，则表明此数不是素数，反之是素数。 
#

def primeNumber(m,n):
    
    if m > n:
        print('第一位素数必须小于第二位质数，请重新输入！')
        m = int(input('请输入第一位素数(包含):\n'))
        n = int(input('请输入第二位素数(不包含):\n'))
        primeNumber(m,n)    
    else:   
        print('%d~%d范围内的素数为：' %(m,n))
        h = 0
        leap = 1
        from math import sqrt
        from sys import stdout
        for m in range(m,n):
            k = int(sqrt(m+1))
            for i in range(2,k+1):
                if m%i == 0:
                    leap = 0
                    break;
            if leap == 1:
                print('%-4d'%m)
                h += 1
                if h%10 == 0:
                    print('')
            leap = 1
        print('The total is %d' %h)

print('请输入素数的范围')
m = int(input('请输入第一位素数(包含):\n'))
n = int(input('请输入第二位素数(不包含):\n'))
primeNumber(m,n)



             
        
            
        
    
