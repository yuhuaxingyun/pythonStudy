#
# 题目：时间函数举例2。
# 程序分析：无。
#

import time

if __name__ == '__main__':
    start = time.time()
    for i in range(3000):
        print(i)
    end = time.time()
print(end - start)