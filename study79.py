#
# 题目：字符串排序。
# 程序分析：无。
#

if __name__ == '__main__':
    n = int(input('请输入需要排序的个数：\n'))
    li = []
    for i in range(n):
        str = input('请输入字符串:\n')
        li.append(str)
    print(li)

    for i in range(0,len(li)):
        for j in range(i+1,len(li)):
            if li[i] > li[j]:
                temp = li[i]
                li[i] = li[j]
                li[j] = temp
    
    print(li)

        

    