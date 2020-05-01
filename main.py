from data_process import Data
from my_crt import Crt
from normal_solution import Nst

# 同余式方程组目录
dir = 'src_data'

solution = 0


def main():
    global solution
    # 创建Data类实例对象
    data = Data('src_data/data.txt')
    # 调用data对象的solution_judge方法，来判断该同余方程组是否有解

    if (data.error_flag):
        if data.solution_judge():
            print("该同余式组有解")
            # 如果有解，则分两种方式求解
            # 先调用crt_judge方法，判断是否可以用中国剩余定理求解
            if data.crt_judge():
                print("该同余式组可以用中国剩余定理")
                sol = "解为: x=%d(mod %d)" % Crt(data).crt_compute()
                print(sol)
                # 将答案写入文件
                with open("src_data/data.txt", "a") as f:
                    f.write("\n"+sol)
                return sol
            # 如果crt_judge方法返回0，则调用nst方法，用一般求解方式进行求解
            else:
                print("该同余式组不可以用中国剩余定理，以一般方法求解")
                sol = "解为: x=%d(mod %d)" % Nst(data).nst_compute()
                print(sol)

                # 将答案写入文件
                with open("src_data/data.txt", "a") as f:
                    f.write("\n"+sol)
                return sol
        else:
            solution = "该同余式组无解"
            print("该同余式组无解")
            return solution
    else:
        return data.solution

if __name__ == '__main__':
    main()

