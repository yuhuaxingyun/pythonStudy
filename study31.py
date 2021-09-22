#
# 题目：请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母。
# 程序分析：用情况语句比较好，如果第一个字母一样，则判断用情况语句或if语句判断第二个字母。。
# 星期一：Monday、星期二：Tuesday、星期三：Wednesday、星期四：Thursday、星期五：Friday、星期六：Saturday、星期日：Sunday
#

def judgeOneDay():
    s = input('请输入第一个字母：')
    if s == 'M':
        print('星期一')
    elif s == 'T':
        judgeTwoDay(s)
    elif s == 'W':
        print('星期三')
    elif s == 'F':
        print('星期五')
    elif s == 'S':
        judgeTwoDay(s)
    else:
        print('输入错误,请重新输入')
        judgeOneDay()

def judgeTwoDay(s):
    l = input('请输入第二个字母：')
    if s == 'T':
        if l == 'u':
            print('星期二')
        elif l == 'h':
            print('星期四')
        else:
            print('输入错误,请重新输入') 
            judgeTwoDay(s)
    elif s == 'S':   
        if l == 'a':
            print('星期六')
        elif l == 'u':
            print('星期日')
        else:
            print('输入错误,请重新输入')
            judgeTwoDay(s)


judgeOneDay()   
        


    
    
