"""Problem 60 「素数ペア集合」 †
素数3, 7, 109, 673は非凡な性質を持っている. 任意の2つの素数を任意の順で繋げると, また素数になっている. 例えば, 7と109を用いると, 7109と1097の両方が素数である. これら4つの素数の和は792である. これは, このような性質をもつ4つの素数の集合の和の中で最小である.

任意の2つの素数を繋げたときに別の素数が生成される, 5つの素数の集合の和の中で最小のものを求めよ."""

import Prime
import basic

table = {}


def andlist(l1, l2):
    result = []
    for x in l1:
        if x in l2:
            result.append(x)
    return result

def find_conect_prime(n, prime_list):
    """引数の素数nについて、引数prime_listで与えられる素数列の中から、
        前後に繋げても素数になるものを見つけ、リスト形式で返却する"""

    ans = []

    str_n = str(n)

    for p in prime_list:
        str_p = str(p)
        if Prime.is_prime(int(str_n + str_p)) and \
                Prime.is_prime(int(str_p + str_n)):

            ans.append(p)

    ans.sort(reverse=True)
    return ans


def check_conectable(n: int, m: int, plist: list):
    """
    引数の素数nと連結可能な素数リストpl istが与えられる
    このリストの中から、相互に連結可能なm個の素数の組みを見つけて
    自分自身を加えたリスト列として返す
    :param n: 連結ベースとなる素数n
    :param m: plistの中から,m個の相互連結可能な素数を見つける
    :param plist: nが連結可能な素数列
    :return: plistの中から見つけたm個の連結可能素数のリスト列。
    見つからなければ空リスト
    """
    result = []

    if m > len(plist) or m < 1:
        return []

    if m == 1:
        for x in plist:
            result.append([n,x])
        return result

    cplist = plist.copy()
    for i in plist:
        cplist.remove(i)
        anlist = andlist(table[i] , cplist)

        if len(anlist) >= m-1:
            subresult = check_conectable(i, m-1, anlist)
            if len(subresult) != 0:
                for x in subresult:
                    cs = x.copy()
                    cs.insert(0, n)
                    result.append(cs)

    return result


if __name__ == "__main__":

    def test():
        prime = Prime.Prime(100)

        print(find_conect_prime(7,prime.get_prime_list()))

    @basic.time_log
    def main():
        target = 5
        primeit = Prime.PrimeIter()

        for p in primeit:
            table[p] = find_conect_prime(p, primeit.get_prime_list())

            if len(table[p]) >= target-1:
                ans = check_conectable(p, target-1, table[p])

                if len(ans) > 0:
                    print(ans)
                    for li in ans:
                        print(sum(li))
                    return
                else:
                    print("No Answer", p)

    main()

