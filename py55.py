"""Problem 55 「Lychrel数」 †
47とその反転を足し合わせると, 47 + 74 = 121となり, 回文数になる.

全ての数が素早く回文数になるわけではない. 349を考えよう,

349 + 943 = 1292,
1292 + 2921 = 4213
4213 + 3124 = 7337
349は, 3回の操作を経て回文数になる.

まだ証明はされていないが, 196のようないくつかの数字は回文数にならないと考えられている. 反転したものを足すという操作を経ても回文数にならないものをLychrel数と呼ぶ. 先のような数の理論的な性質により, またこの問題の目的のために, Lychrel数で無いと証明されていない数はLychrel数だと仮定する.

更に, 10000未満の数については，常に以下のどちらか一方が成り立つと仮定してよい.

50回未満の操作で回文数になる
まだ誰も回文数まで到達していない
実際, 10677が50回以上の操作を必要とする最初の数である: 4668731596684224866951378664 (53回の操作で28桁のこの回文数になる).

驚くべきことに, 回文数かつLychrel数であるものが存在する. 最初の数は4994である.

10000未満のLychrel数の個数を答えよ.

注: 2007/04/24にLychrel数の理論的な性質を強調するために文面が修正された."""

import basic


def iskaibun(n):
    """引数ｎが回文数であるか判定する関数"""
    if kaibun(n) == n:
        return True
    else:
        return False


def kaibun(n):
    """引数の回文数を返す関数"""
    li = basic.inttolist(n)
    li.reverse()
    tn = basic.listtoint(li)
    return tn


def islychrel(n):
    """引数nがLychrel数（５０回の足し算を繰り返しても回文にならない数）か判定する関数"""

    for _ in range(50):
        new_n = n + kaibun(n)
        if iskaibun(new_n):
            return False
        else:
            n = new_n

    return True

if __name__ == "__main__":

    def test():
        print(islychrel(47))


    @basic.time_log
    def main():
        count = 0
        for n in range(1,10000):
            if islychrel(n):
                print(n)
                count += 1

        print("count = {0:5d}".format(count))


    main()
