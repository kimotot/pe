""" Problem 52 「置換倍数」 †
125874を2倍すると251748となる. これは元の数125874と順番は違うが同じ数を含む.

2x, 3x, 4x, 5x, 6x が x と同じ数を含むような最小の正整数 x を求めよ."""

import basic

def isequalnum(a,b):
    """ ふたつの数字が同じ要素（数字）から構成されているか判定する関数"""
    lista = basic.inttolist(a)
    listb = basic.inttolist(b)

    if sorted(lista) == sorted(listb):
        return True
    else:
        return False


def is6numberequal(n):
    """引数nの２〜６倍の数字が、同じ構成要素であるか判定する関数"""

    for bai in range(2, 7):
        if not isequalnum(n, n * bai):
            return False

    return True


if __name__ == "__main__":

    def test():
        print(is6numberequal(1428570))

    @basic.time_log
    def main():
        keta = 5

        while keta < 6:
            for n in range(10**keta, 10**(keta+1) // 6):
                print(n)
                if is6numberequal(n):
                    print("ans= ", n)
                    return

            keta += 1

        print("No Answer!")

    main()
