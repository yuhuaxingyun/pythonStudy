#
# 题目：时间函数举例1。
# 程序分析：无。
#

import time

if __name__ == '__main__':
    print(time.ctime(time.time()))
    print(time.asctime(time.localtime(time.time())))
    print(time.asctime(time.gmtime(time.time())))