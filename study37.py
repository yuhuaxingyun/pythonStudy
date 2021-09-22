#
# 题目：对10个数进行排序。
# 程序分析：可以利用选择法，即从后9个比较过程中，选择一个最小的与第一个元素交换，下次类推，即用第二个元素与后8个进行比较，并进行交换。
#


def sort(n):
    print('请依次输入%d个数字'%n)
    l = []
    for i in range(n):
        s = int(input('请输入%d个整数：\n'%(i+1)))
        l.append(int(s))
    
    for i in range(n):
        print(l[i])

    for i in range(n-1):
        for j in range(i+1,n):
            if l[i]>l[j]:
                temp = l[i]
                l[i] = l[j]
                l[j] = temp
            
    print('排列之后：')
    for i in range(n):
        print(l[i])


if __name__ == '__main__':
    n = int(input('请输入需要排序的数字个数：\n'))
    sort(n)
        

                
            
                
        
    