#
# 题目：输入一个奇数，然后判断最少几个 9 除于该数的结果为整数。
# 程序分析：999999 / 13 = 76923。
#
if __name__ == '__main__':
    n = 1
    c = 1
    m = 9
    sum = 9
    p = int(input('请输入一个奇数：\n'))

    while n != 0:
        if sum%p == 0:
            n = 0
        else:
            m *= 10
            sum += m
            c += 1
    print('%d 个 9 可以被 %d 整除 : %d' % (c,p,sum))
    r = sum / p
    print ('%d / %d = %d' % (sum,p,r))
        