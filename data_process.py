import re
from format_check import FormatError


# 数据处理类
# 将path文件中的同余方程式组进行处理和提取，并提供了方法来判定是否有解
class Data(object):
    @staticmethod
    # 该函数求解最大公约数
    def gcd(a, b):
        if a < b:
            a, b = b, a
        if a % b == 0:
            return b
        return Data.gcd(b, a % b)

    # 初始化函数
    # self.path:     存放同余式方程组的文件
    # self.re_exp:   正则表达式预编译
    # self.remainder:余数列表
    # self.mod:      模列表
    # self.solution_unknown:未知数变量列表
    # self.num_equation:    去重后方程个数
    def __init__(self, path):
        self.path = path
        self.re_exp = re.compile(r'([a-zA-Z]\d?)=(\d+)\(mod(\d+)\)')
        with open(path, 'r') as f:
            self.f_list = f.readlines()
        self.remainder = []
        self.mod = []
        self.solution_unknown = []
        self.error_flag = 1
        self.solution = 0

        # 去掉重复出现的方程
        for equation in self.f_list:
            count = self.f_list.count(equation)
            if count != 1:
                for i in range(count-1):
                    self.f_list.remove(equation)

        self.num_equation = len(self.f_list)
        # 利用正则表达式 ，对txt文件里面的方程组进行提取数据，并存放到相应的列表属性中

        try:
            for equation in self.f_list:
                self.remainder.append(self.re_exp.search(equation).group(2))
                self.mod.append(self.re_exp.search(equation).group(3))
                self.solution_unknown.append(self.re_exp.search(equation).group(1))
                # 正则提取的部分是字符类型，把列表中每一项转化为整型，便于之后直接用来运算
                self.remainder = [int(r) for r in self.remainder]
                self.mod = [int(mm) for mm in self.mod]
        except AttributeError:
            self.solution = "!!请修改输入文本格式!!"
            self.error_flag = 0
            print(self.solution)


        # 例：若输入”x2=2（mod3)“，即出现了二次同余式，则抛出错误
        for solution_un in self.solution_unknown:
            try:
                if len(solution_un) != 1:
                    raise FormatError("该同余式组含有高次项")
            except FormatError as e:
                self.solution = "!!请修改输入文本格式!!\n!!该同余式组含有高次项!!"
                self.error_flag = 0
                print(self.solution)

    # 该函数用来判断同余方程式组是否有解
    # 定理：有解充要条件<=>对于同余方程式组中的任意两项，该两项的模的最大公约数要能够整除该两项的余数差
    # 实现：通过双重循环遍历方程组一一判断即可



    def solution_judge(self):
        flag = 1
        for i in range(self.num_equation):
            for j in range(self.num_equation):
                if (self.remainder[i] - self.remainder[j]) % Data.gcd(self.mod[i], self.mod[j]) != 0:
                    flag = 0
        return flag

    # 该函数用来判断在同余方程式组有解的前提下，该同余方程式组是否可以用中国剩余定理来求解
    # 定理：若模两两互素，则可以用中国剩余定理
    # 实现：判断两两互素，即两个数最大公约数为1，调用gcd函数判断即可
    def crt_judge(self):
        flag = 1
        for i in self.mod:
            for j in self.mod:

                if i != j and Data.gcd(i, j) != 1:
                    flag = 0
        return flag




































