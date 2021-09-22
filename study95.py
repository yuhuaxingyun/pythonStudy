#
# 题目：字符串日期转换为易读的日期格式。
# 程序分析：无。
#
# 需要安装 dateutil 

#!/usr/bin/python
# -*- coding: UTF-8 -*-

from dateutil import parser

dt = parser.parse("Aug 28 2015 12:00:00AM")
print (dt)