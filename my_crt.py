from invserse_solution import getInv


# 中国剩余定理类，该类对处理好的Data实例对象用中国剩余定理进行求解
class Crt(object):
    # self.num_equation:方程个数
    # self.remainder   :余数列表
    # self.mod         :模列表
    # self.solution_unknown:未知数列表
    # self.M           :所有你模的乘积
    # self.Mi          :(列表)M/mi
    # self.Ti          :逆元列表
    # self.solution    :最后答案
    def __init__(self, congruence):
        self.num_equation = congruence.num_equation
        self.remainder = congruence.remainder
        self.mod = congruence.mod
        self.solution_unknown = congruence.solution_unknown
        self.M = 1
        self.Mi = []
        self.Ti = []
        self.solution = 0

    # 用中国剩余定理来计算最后答案
    def crt_compute(self):
        # 对数据进行检测，未知数必须为一次，防止出现高次同余式组
        def data_check():
            for solution_un in self.solution_unknown:
                if len(solution_un) != 1:
                    print("这不是一次同余式组")
                    return 0

        # 求逆元
        def inverse_element():
            for ii in range(self.num_equation):
                self.Ti.append(getInv(self.Mi[ii], self.mod[ii]))
        # 计算模的乘积
        for m in self.mod:
            self.M *= m
        # 计算Mi
        for i in range(self.num_equation):
            self.Mi.append(int(self.M / self.mod[i]))

        inverse_element()
        data_check()
        # 计算解<====>sum(逆元*余数*Mi)
        for i in range(self.num_equation):
            self.solution += self.remainder[i]*self.Mi[i]*self.Ti[i]
        self.solution %= self.M
        self.solution %= self.M
        return self.solution, self.M
