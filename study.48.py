#
# 题目：数字比较。
# 程序分析：无
#

def judgeSize(i,j):
    if i>j:
        print('%d 大于 %d'% (i,j))
    elif i == j:
        print('%d 等于 %d'% (i,j))
    elif i<j:
        print('%d 小于 %d'% (i,j))
    else:
        print('未知')


if __name__ == '__main__':
    
    i = int(input('请输入第一个值：'))
    j = int(input('请输入第二个值：'))
    judgeSize(i, j)

        
        
        
    