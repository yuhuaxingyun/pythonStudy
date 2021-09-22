#
# 题目：回答结果（结构体变量传递）。
# 程序分析：无。
#

if __name__ == '__main__':
    class student:
        x = 0
        y = 0

    def fun(stu):
        stu.x = 20
        stu.y = 'c'
    
    a = student()
    a.x = 3
    a.y = 'a'

    fun(a)
    print(a.x,a.y)
        
    