#
# 题目：模仿静态变量的用法。
# 程序分析：无。
#

def varfunc():
    var = 0  # 局部变量
    print('var = %d'%var)
    var += 1
    

if __name__ == '__main__':
    for i in range(3):
        varfunc()



class Static:
    StaticVar = 5
    def varfunc(self):
        self.StaticVar += 1
        print(self.StaticVar)

print(Static().StaticVar)
a = Static()
for i in range(3):
    a.varfunc()
            
    