"""Problem 56 「もっとべき乗の数字和」 †
Googol (10100)は非常に大きな数である: 1の後に0が100個続く. 100100は想像を絶する. 1の後に0が200回続く. その大きさにも関わらず, 両者とも数字和 ( 桁の和 ) は1である.

a, b < 100 について自然数 ab を考える. 数字和の最大値を答えよ."""

import basic
import functools


def calc():
    max = 0
    for a in range(1, 100):
        for b in range(1, 100):
            listab = basic.inttolist(a ** b)
            sumab = functools.reduce(lambda x, y: x+y, listab, 0)
            if max < sumab:
                max = sumab

    return max


if __name__ == "__main__":
    print(calc())