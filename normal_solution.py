from prime_decomposition import prime_Decomposition
from data_process import Data
from my_crt import Crt


# 在同余式组有解，但不满足中国剩余定理，用一般方法求解
# 求解原理详见实验报告。 原理资料来源：http://www.doc88.com/p-0028984655763.html
# 本类实现了 对应的三套（余数列表和模列表，底数列表，指数列表）一步一步将一般情况的同余式方程组转化为符合中国剩余定理的形式，
# 最后调用中国剩余定理即可。
class Nst(object):
    def __init__(self, congruence):
        # self.remainder:余数列表
        # self.mod:      模列表
        # self.solution_unknown:未知数变量列表
        # self.num_equation    :方程个数
        self.num_equation = congruence.num_equation
        self.remainder = congruence.remainder
        self.mod = congruence.mod
        self.solution = 0

        # self.remainder2 :余数列表
        # self.base2      :底数列表
        # self.exponent   :指数列表
        # self.num_equation2 :方程转化个数
        self.remainder2 = []
        self.base2 = []
        self.exponent = []
        self.num_equation2 = 0

        # self.remainder3 ：余数列表
        # self.base3      ：底数列表
        # self.exponent3  ：指数列表
        # self.num_equation3 ：方程个数
        self.remainder3 = []
        self.base3 = []
        self.exponent3 = []
        self.num_equation3 = 0

    # 一般求解方法
    def nst_compute(self):
        # 首先对同余式方程组的模进行质数分解（调用prime_Decomposition函数）
        # 质数分解获得模的标准分解式，然后构成了第二套等价的方程组
        for i in range(self.num_equation):
            a, b = prime_Decomposition(self.mod[i])
            self.base2.extend(a)
            self.exponent.extend(b)
            for j in range(len(a)):
                self.remainder2.append(self.remainder[i])
                self.num_equation2 += 1
        # 双重循环遍历因数分解后的同余方程式组
        # 这一步将使同余式方程组符合中国剩余定理
        for i in range(self.num_equation2):
            for j in range(i+1, self.num_equation2):
                if self.base2[i] == self.base2[j]:
                    # flag为了标记第i项和第j项指数到底是谁比较大
                    flag = int(self.exponent[i] > self.exponent[j])
                    # c为指数较小项
                    # b为较大指数项
                    c = [self.exponent[j], self.exponent[i]][self.exponent[j] >= self.exponent[i]]
                    b = [self.exponent[i], self.exponent[j]][self.exponent[j] > self.exponent[i]]
                    # 判别条件：(base^c)|余数差
                    if abs(self.remainder2[i] - self.remainder2[j]) % pow(self.base2[i], c) == 0:
                        # 按条件扩充余数列表
                        if flag:
                            self.remainder3.append(self.remainder2[i])
                        else:
                            self.remainder3.append(self.remainder2[j])
                        # 按条件扩充底数，指数，并且方程个数增加一
                        self.base3.append(self.base2[i])
                        self.exponent3.append(b)
                        self.num_equation3 += 1
                    else:
                        print("矛盾，该同余式组无解")
                        exit()
        # 将同余方程式组中落单的方程添加到最终方程组中
        # 使用了enumerate函数，使用列表的count方法，
        # 若某项只出现一次，用该索引值获取该项值，并添加到相应列表中
        for index, value in enumerate(self.base2):
            if self.base2.count(value) == 1:
                self.remainder3.append(self.remainder2[index])
                self.base3.append(self.base2[index])
                self.exponent3.append(self.exponent[index])
                self.num_equation3 += 1
        # 创建新文件，构造最终方程式组并将该方程式组放入txt文件中，
        # 这样就可以用该路径创建新的数据对象
        # 到此为止，历尽千辛万苦构造的新同余式方程组就可能满足中国剩余定理了，如果满足，只要调用crt类即可
        with open("src_data/transformed_data.txt", 'w') as f:
            for i in range(self.num_equation3):
                f.write("x=%d(mod%d)\n" % (self.remainder3[i], pow(self.base3[i], self.exponent3[i])))
        # 构造Data对象
        transformed_data = Data("src_data/transformed_data.txt")
        # 调用crt_judge方法，若返回1，则说明经过一轮转化已经满足中国剩余定理
        if transformed_data.crt_judge():
            tcrt = Crt(transformed_data)
            return tcrt.crt_compute()
        # 如果crt_judge方法返回0，则说明经过一轮转化并不转化成满足中国剩余定理形式，但已经更接近中国剩余定理条件
        # 此时则需要进行递归运算，将此时的transformed_data再次传入nst，进行新的一轮三部转化
        else:
            print("以一般方法 递归 求解")
            return Nst(transformed_data).nst_compute()








