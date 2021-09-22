#
# 题目：列表使用实例。
# 程序分析：无。
#

# list
# 新建列表
testlist = [10086,'中国移动',[1,2,3,4,5]]

# 访问列表长度
print(len(testlist))

# 到列表结尾
print(testlist[1:])

# 向列表添加元素
testlist.append('i\'m new here')
print(testlist)
print(len(testlist))
print(testlist[-1])

# 弹出列表的第几个元素
print(testlist.pop(2))

print(len(testlist))
print(testlist)

# list comprehension
# 后面有介绍，暂时掠过
matrix = [[1,2,3],
        [4,5,6],
        [7,8,9]]

print(matrix)
print(matrix[1])

col2 = [row[1] for row in matrix] #get a column from a matrix
print(col2)

col2even = [row[1] for row in matrix if row[1] %2 == 0] #filter odd item 
print(col2even)