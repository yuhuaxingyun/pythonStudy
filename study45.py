#
# 题目：统计 1 到 100 之和。
# 程序分析：无
#
def sumUp(i,j):
    sum = 0
    for i in range(i,j+1):
        sum += i
    print(sum)
    
def judgeNum(i,j):
    if i>j:
        print('最大值必须大于最小值！')
        j = int(input('请输入求和区间的最大值：'))
        judgeNum(i, j)
    else:
        sumUp(i, j)

i = int(input('请输入求和区间的最小值：'))
j = int(input('请输入求和区间的最大值：'))
judgeNum(i,j)