#
# 题目：两个乒乓球队进行比赛，各出三人。甲队为a,b,c三人，乙队为x,y,z三人。已抽签决定比赛名单。有人向队员打听比赛的名单。a说他不和x比，c说他不和x,z比，请编程序找出三队赛手的名单。
#

for i in range(ord('x'),ord('z')+1): # 对战x～z、i为 a 对战
    for j in range(ord('x'),ord('z')+1): # 对战x～z、j为 b 对战
        if i != j: 
           for k in range(ord('x'),ord('z')+1): # 对战x～z、k为 c 对战
               if (i != k) and (j != k): 
                   if (i!= ord('x')) and (k != ord('x') and (k != ord('z'))): # 条件：a不和 x 对战、c不和 x,z 对战
                       print('对战结果： a -- %s\tb -- %s\tc -- %s' % (chr(i),chr(j),chr(k)))


                       
                   
            
        
    