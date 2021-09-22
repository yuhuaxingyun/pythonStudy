#
# 题目：从键盘输入一个字符串，将小写字母全部转换成大写字母，然后输出到一个磁盘文件"test"中保存。
# 程序分析：无。
#

import sys

str = input('请输入一个字符串:\n')
with open('test.txt','w') as f:
    f.write(str.upper())