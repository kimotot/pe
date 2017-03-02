# coding:UTF-8

import time

def kai(n):
    ''' 正の整数の階乗を求める関数
         階乗の計算結果'''
    if n == 0 or n == 1:
        return 1
    else:
        return n * kai(n - 1)


def is_kaijyowa(n):
    # 正の整数値の各桁の階乗和と、整数値が等しいか判定する関数
    temp_sum = 0
    temp_n = n

    while temp_n > 0:
        temp_sum = temp_sum + klist[temp_n % 10]
        temp_n = temp_n // 10

    if temp_sum == n:
        return True
    else:
        return False


if __name__ == '__main__':
    klist = [kai(x) for x in range(10)]
    sum = 0

    start = time.time()

    for n in range(10, klist[9]*7):
        if is_kaijyowa(n):
            sum += n

    print("総和={0}".format(sum))

    elapsed_time = time.time() - start
    print("時間={0:.3}".format(elapsed_time))

    print("競合 リモートで変更")


    print("競合 リモートで変更したよ")
