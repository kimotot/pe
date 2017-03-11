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


if __name__ == "__main__":

    def test():
        print(isequalnum(123,322))

    @basic.time_log
    def main():
        n = 125874

        while True:
            print(n)
            count = 0
            for x in range(2, 7):
                if isequalnum(n, n*x):
                    count += 1
                else:
                    break

                if count == 6:
                    return True,n

            n += 1

    print(main())
