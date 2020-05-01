# 质数分解
# 将一个合数化为若干质数的幂积
# 比如18 = 2*9 = (2^1)*(3^2),将底数2和3放在列表L中，将指数1和2放在列表L_num中
# 这里设置了一个flag，因为会出现多次除以某个因数的情况，
# 当第一次除以某个因数时flag为1，此时L列表扩充
# 而不是第一次除以某个因数时flag为0，此时 L列表不用append，只要指数列表最后一项加一即可。

def prime_Decomposition(k):
    L = []
    L_num = []
    i = 2
    flag = 1
    while k >= i:
        if k % i == 0:
            if flag == 1:
                flag = 0
                k = k / i
                L.append(i)
                L_num.append(1)
            else:
                k = k / i
                L_num[-1] += 1
        else:
            flag = 1
            i += 1
    # print(L)
    # print(L_num)

    return L, L_num





