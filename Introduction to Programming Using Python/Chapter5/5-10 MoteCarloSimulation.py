import random

NUMBER_OF_TRIALS = 1000000    # Constant
numberOfHits = 0

for i in range(NUMBER_OF_TRIALS):   # 在正方形内重复产生随机点（x,y）
    x = random.random() * 2 - 1
    y = random.random() * 2 - 1

    if x * x + y * y <= 1:
        numberOfHits += 1

pi = 4 * numberOfHits / NUMBER_OF_TRIALS

print("PI is", pi)


'''
    蒙特卡罗模拟：
        蒙特卡罗模拟使用随机数和概率来解决问题。它在计算机数学、物理、化学和经济方面
        都有着非常广泛的应用。使用蒙特卡罗模拟来估计π的例子
'''