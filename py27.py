#coding:UTF-8



import time
import math
import functools
from copy import copy

'''
    |a| < 1000, |b| ≤ 1000 として以下の二次式を考える
    (ここで |a| は絶対値): 例えば |11| = 11 |-4| = 4である.
    n*n + an + b
    n = 0 から始めて連続する整数で素数を生成したときに最長の長さとなる上の二次式の, 係数 a, b の積を答えよ.

    bは正の整数値でかつ素数であること！ →　1000以下の素数

    n=1の時を考えると、1+a+b は素数である
    a+b+1 > 0
    a > -b - 1　→　1000 > a > -b - 1

'''

def get_sosu(maximum):
    """
    引数max以下の素数を求める
    戻り値は求めた素数を含むリスト
    なお、1は素数ではないので、リストに含めない
    """
    sosu_list = [2, 3]  # 自明の素数をセットしておく

    for n in range(5, maximum, 2):

        sq = int(math.sqrt(n))

        isprime = True
        for prime in sosu_list:
            if prime > sq:
                isprime = True
                break
            elif n % prime == 0:
                isprime = False
                break

        if isprime:
            sosu_list.append(n)

    return sosu_list


def count_sosu(a,b,slist):
    """
    引数を係数とした二次式で何個の素数を連続して生成するかカウントする関数
    :param a: 係数a
    :param b: 係数b
    :param slist: 素数のリスト
    :return: 連続して生成した素数の個数
    """

    count = 0
    n = 0
    while (n*n + a*n + b) in slist:
        count += 1
        n += 1

    return count


if __name__ == "__main__":
    start = time.time()

    sosu_list = get_sosu(1000000)
    ab_list = get_sosu(1000)

    maxa = 0
    maxb = 0
    maxcount = 0

    for b in ab_list:
        for a in range(-b,1000):
            if p in ab_list:
                a = p - b -1
                if a >
                print(a,b,count_sosu(a,b,sosu_list))

        for p in ab_list:

            a = p - b - 1
            if (a > -b) and (a < 1000):
                c = count_sosu(a,b,sosu_list)
                if c > maxcount:
                    maxa = a
                    maxb = b
                    maxcount = c


    elp_time = time.time() - start
    print("{0:6.3f} sec".format(elp_time))


