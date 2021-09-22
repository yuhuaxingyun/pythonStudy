#
# 题目：画椭圆。　
# 程序分析：使用 Tkinter。
#

# 没反应，再研究


from tkinter import *
if __name__ == '_main__':

    canvas = Canvas(width=400,height=600,bg='white')
    x = 360
    y = 160
    top = y - 30
    bottom = y - 30
    for i in range(15):
        canvas.create_oval(250-top,250-bottom,250+top,250+bottom)
        top -= 5
        bottom += 5

    canvas.pack()
    mainloop()
        

    