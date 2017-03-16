"""1から始めて, 以下のように反時計回りに数字を並べていくと, 辺の長さが7の渦巻きが形成される.

37	36	35	34	33	32	31
38	17	16	15	14	13	30
39	18	5	4	3	12	29
40	19	6	1	2	11	28
41	20	7	8	9	10	27
42	21	22	23	24	25	26
43	44	45	46	47	48	49
面白いことに, 奇平方数が右下の対角線上に出現する. もっと面白いことには, 対角線上の13個の数字のうち, 8個が素数である. ここで割合は8/13 ≈ 62%である.

渦巻きに新しい層を付け加えよう. すると辺の長さが9の渦巻きが出来る. 以下, この操作を繰り返していく. 対角線上の素数の割合が10%未満に落ちる最初の辺の長さを求めよ."""

import Prime
import basic

def countprime(length):
    """一辺の長さがlengthの時、四隅に現れる数字のうち、素数の数を求める"""
    n = length * length
    count = 0

    for i in range(4):
        if Prime.is_prime(n - i*(length-1)):
            count += 1

    return count


if __name__ == "__main__":

    @basic.time_log
    def main():
        length = 7
        c = 8
        m = 13

        while c/m >= 0.1:
            length += 2
            c += countprime(length)
            m += 4

        print(length)


    main()
