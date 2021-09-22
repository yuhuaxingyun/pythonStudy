#
# 题目：有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。
# 程序分析：请抓住分子与分母的变化规律。
#

def sumUp(count):
    molecule = 2.0
    denominator = 1.0
    sum = 0.0
    for i in range(0,count):
        print('%d/%d'%(molecule,denominator))
        sum += molecule / denominator
        tem = molecule
        molecule = molecule +  denominator
        denominator = tem


    print('总和：%f'%sum)


# 此处还没实现
def fractionSumUp(count):
    molecule = 2.0
    denominator = 1.0
    sum = 0.0
    for i in range(0,count):
        print('%d/%d'%(molecule,denominator))
        # sum += molecule / denominator
        sumMolecule = molecule
        sumDenominator = denominator
        tem = molecule
        molecule = molecule +  denominator
        denominator = tem


    print('总和：%f'%sum)

count = int(input('请输入数列前多少的项数：'))
sumUp(count)



