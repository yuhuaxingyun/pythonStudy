#
# 题目：一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
# 程序分析：无
#



def rebound(height,tim):
    tours = []
    heights = []

    for i in range(1,tim + 1):
        if i == 1:
            tours.append(height)
        else:
            tours.append(2*height)
        height /= 2
        heights.append(height)

    print('总高度：tours = {0}'.format(sum(tours)))
    print('第%d次反弹高度：heights = %d'%(tim,heights[-1]))



def judgeGreaterZero(type,height,tim):

    if type == 0:
        if height < 1:
            print('请输入大于0的数！')
            height = int(input('请输入起始高度：'))
            judgeGreaterZero(type, height,0)
        else:
            tim = int(input('请输入第几次落地：'))
            judgeGreaterZero(1,height,tim)
    else:
        if tim < 1:
            print('请输入大于0的数！')
            tim = int(input('请输入第几次落地：'))
            judgeGreaterZero(type,height,tim)
        else:
            rebound(height, tim)

hei = int(input('请输入起始高度：'))
judgeGreaterZero(0,hei,0)



        
    