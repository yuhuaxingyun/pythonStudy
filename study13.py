#
# 题目：打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。
# 程序分析：利用for循环控制100-999个数，每个数分解出个位，十位，百位。
#

def narcissisticNumber(m,n):
    if m >= n:
        print('第一位水仙花数必须小于第二位水仙花数，请重新输入！')
        m = int(input('请输入第一位水仙花数(包含):\n'))
        n = int(input('请输入第二位水仙花数(不包含):\n'))
        narcissisticNumber(m,n) 
    else:   
        print('%d~%d范围内的水仙花数为：' %(m,n))
        for x in range(m,n):
            i = x // 100
            j = x // 10 % 10
            k = x % 10
            if x == i*i*i+j*j*j+k*k*k:
                print (x)

def judgeOneNumber(m):
    if 99<m<1000:
        n = int(input('请输入第二位水仙花数(不包含):\n'))
        judgeTwoNumber(m,n)
    else:
        print('水仙花数必须为三位数！')
        m = int(input('请输入第一位水仙花数(包含):\n'))
        judgeOneNumber(m)

def judgeTwoNumber(m,n):
    if 99<n<=1000:
        narcissisticNumber(m,n)    
    else:  
        print('水仙花数必须为三位数！')
        n = int(input('请输入第二位水仙花数(不包含):\n'))
        judgeTwoNumber(m,n)     


print('请输入水仙花数的范围100~1000: 包含100、不包含1000')
m = int(input('请输入第一位水仙花数(包含):\n'))
judgeOneNumber(m)





    