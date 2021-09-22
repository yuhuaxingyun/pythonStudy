#
# 题目：八进制转换为十进制
# 程序分析：无。
#


# if __name__ == '__main__':
#     n = 0
#     p = input('input a octal number:\n')
#     for i in range(len(p)):
#         n = n * 8 + ord(p[i]) - ord('0')
#     print (n)

import math

if __name__ == '__main__':
    
    n = 0
    p = input('input a octal number:\n')
    l = len(str(p)) 

    flag = True
    for i in range(l):
        m = int(p[i])
        if m<0:
            flag = False
            break
        elif m>=8:
            flag = False
            break
        else:
            flag = True
           
            
    if flag == False:
        print('请输入8进制,每位数都为（0～7）！')
        
    else:
        for i in range(l):
            n = n * 8 + ord(p[i]) - ord('0')
        print (n)