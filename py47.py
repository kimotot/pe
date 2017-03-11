'''Problem 47 「異なる素因数」 †
それぞれ2つの異なる素因数を持つ連続する2つの数が最初に現れるのは:

14 = 2 × 7
15 = 3 × 5

それぞれ3つの異なる素因数を持つ連続する3つの数が最初に現れるのは:

644 = 22 × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19

最初に現れるそれぞれ4つの異なる素因数を持つ連続する4つの数を求めよ. その最初の数はいくつか?'''

import basic


def pe47():
    ''' pe47の解答を求めるプログラム '''

    n = 2
    yaku = [0, 0, 0, 0]

    while True:
        count = len(set(basic.prime_factorization(n)))
        yaku.append(count)
        del yaku[0]

        if yaku[0] == yaku[1] == yaku[2] == yaku[3] == 4:
            return n-3
        else:
            n += 1


if __name__ == "__main__":
    print(pe47())
