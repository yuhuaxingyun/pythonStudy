#
# 题目：暂停一秒输出，并格式化当前时间。
# 程序分析：无。
#

import time


for item in range(5):
   
    print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    time.sleep(1)