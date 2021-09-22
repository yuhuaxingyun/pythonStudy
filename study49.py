#
# 题目：使用lambda来创建匿名函数。
# 程序分析：无
# 获取最大值和最小值
#

MAXIMUM = lambda x,y : (x>y)*x + (x<y)*y
MINIMUM = lambda x,y : (x>y)*y + (x<y)*x

if __name__ == '__main__':
    a = 10
    b = 20
    print('最大值：%d'%MAXIMUM(a,b))
    print('最小值：%d'%MINIMUM(a,b))
    