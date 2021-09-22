#
# 题目：时间函数举例3。
# 程序分析：无。
#

#
import time

if __name__ == '__main__':
    start = time.perf_counter()
    for i in range(10000):
        print(i)
    end = time.perf_counter()
    print('different is %6.3f'%(end-start))

    start1 = time.process_time()
    for j in range(10000):
        print(j)
    end1 = time.process_time()
    print('different1 is %6.3f'%(end1-start1))