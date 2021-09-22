
# -*- coding: UTF-8 -*-
#
# 测试一
#
# from multiprocessing import Pool
# import os,time,random

# def run_task(name):
#     print('Task %s (pid = %s) is running...'%(name,os.getpid()))
#     time.sleep(random.random()*3)

# if __name__ == '__main__':
#     print('Current process %s.'%os.getpid())
#     p = Pool(processes=3)
#     for i in range(5):
#         p.apply_async(run_task,args=(i,))
#     print('Waiting for all subprocesses done...')
#     p.close()
#     p.join()
#     print('All subprocesses done.')
#
#
# 测试二
#

import random
import time,threading

def thread_run(urls):
    print('Current %s is running...'%threading.current_thread().name)
    for url in urls:
        print('%s --->>> %s'%(threading.current_thread().name,url))
        time.sleep(random.random())
    print('%s ended.'%threading.current_thread().name)
print('%s is running...'%threading.current_thread().name)
t1 = threading.Thread(target=thread_run,name='Thread_1',args=(['url_1','url_2','url_3'],))
t2 = threading.Thread(target=thread_run,name='Thread_2',args=(['url_4','url_5','url_6'],))
t1.start()
t2.start()
t1.join()
t2.join()
print('%s ended.'%threading.current_thread().name)


        
    