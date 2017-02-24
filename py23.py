# coding:UTF-8

import time
from functools import reduce

kajyou_list = []

def shinyaku(num):
    """ 真の約数を求める関数
        引数：約数を求める対象となる正の整数値
        戻値：約数のリスト
        1は約数に含める"""

    yakusu_list = []

    for i in range(1,num // 2 + 1):
        if num % i == 0:
            yakusu_list.append(i)

    return(yakusu_list)


def kajyou(num):
    """ 過剰数かどうかを判定する関数
        返値： 過剰数である　→　True
               過剰数でない　→　False """

    yakusu_list = shinyaku(num)

    if reduce(lambda x,y:x+y,yakusu_list) > num:
        return True
    else:
        return False


def set_kajyou_list(max):
    """ max値以下の過剰数のリストを求める関数
        返値：過剰数のリスト"""

    for n in range(12,max+1):
        if kajyou(n):
            kajyou_list.append(n)


def kajyouwa(num):
    """ 過剰数の和で表現できるか判定する関数
        引数： 過剰数の和で表現できるのか判定対象とする正の整数値
        返値： 過剰数の和ならTrue、そうでないならFalse"""

    for a in kajyou_list:
        if a >= num:
            return False
        else:
            if num - a in kajyou_list:
                return True
    return False



if __name__ == "__main__":
    start = time.time()

    kajyou_list = []
    set_kajyou_list(28123)
    sum = 0

    for a in range(28123 + 1):
        if kajyouwa(a):
            print("○ {0}".format(a))
        else:
            print("× {0}".format(a))
            sum += a



    print(sum)
    elp = time.time() - start
    print(kajyou_list)
    print("{0} sec".format(elp))

