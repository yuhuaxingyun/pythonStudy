#
# 题目：有 n 个整数，使其前面各数顺序向后移 m 个位置，最后 m 个数变成最前面的 m 个数
# 程序分析：无。
#

if __name__ == '__main__':

    def rightMove(array,n,m):
        array_end = array[n-1]
        for i in range(n-1,-1,-1):
            array[i] = array[i-1]
        array[0] = array_end
        m -= 1
        if m > 0:
            rightMove(array, n, m)


    def leftMove(array,n,m):
        array_start = array[0]
        for i in range(0,n-1):
            array[i] = array[i+1]
        array[n-1] = array_start
        m -= 1
        if m > 0:
            leftMove(array, n, m)
        

    def moveDirection():
        d = int(input('请输入向前移或向后移(向前移输入1、向后移输入2)：'))
        if d == 1:
           return d
        elif d == 2:
            return d
        else:
            print('输入有误，请重新输入！')
            return moveDirection()

        
    n = int(input('请输入几个整数为：'))
    d =  moveDirection()
    m = int(input('请输入移动几个位置：'))


    numbers = []
    for i in range(n):
        numbers.append(int(input('请输入第%d个数字：'%(i+1))))
    print('原始列表：',numbers)
    if d == 1:
        leftMove(numbers,n,m)
    elif d == 2:
        rightMove(numbers, n, m)
    else:
        print('输入有误，请重新输入！')
        moveDirection()

    print('移动之后：',numbers)
        
            
            
        
    