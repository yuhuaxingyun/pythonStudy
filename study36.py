#
# 题目：求100之内的素数。
# 程序分析：无。
#

lower = int(input('输入区间最小值：'))
upper = int(input('输入区间最大值：'))

for num in range(lower,upper+1):
    if num > 1:
        # for......else......语法
        for i in range(2,num):
            if (num % i) == 0:
                break
        else:
            print(num)
                
            
        
    