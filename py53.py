"""Problem 53 「組み合わせ選択」 †
12345から3つ選ぶ選び方は10通りである.

123, 124, 125, 134, 135, 145, 234, 235, 245, 345.
組み合わせでは, 以下の記法を用いてこのことを表す: 5C3 = 10.

一般に, r ≤ n について nCr = n!/(r!(n-r)!) である. ここで, n! = n×(n−1)×...×3×2×1, 0! = 1 と階乗を定義する.

n = 23 になるまで, これらの値が100万を超えることはない: 23C10 = 1144066.

1 ≤ n ≤ 100 について, 100万を超える nCr は何通りあるか?"""

import basic

kai = [1]            # 階乗の値を事前に計算し保持しておくリスト　グローバル変数

def setkai(max):
    """max値までの階乗値を計算し、kaiリストにほぞんする関数"""
    for n in range(1, max+1):
        kai.append(kai[n-1] * n)


def ismillionover(n, r):
    """nCrの組み合わせが、１００万以上であるか判定する関数"""
    if kai[n] / kai[r] / kai[n-r] > 1000000:
        return True
    else:
        return False


if __name__ == "__main__":

    def test():

        setkai(100)
        print(kai[23] // kai[10] // kai[13])


    @basic.time_log
    def main():
        setkai(100)
        count = 0

        for n in range(1, 101):
            print(n)
            for r in range(1, n):
                if ismillionover(n, r):
                    count += 1

        print(count)


    main()