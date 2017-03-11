''' Problem 51 「素数の桁置換」 †
*3の第1桁を置き換えることで, 13, 23, 43, 53, 73, 83という6つの素数が得られる.
56**3の第3桁と第4桁を同じ数で置き換えることを考えよう. この5桁の数は7つの素数をもつ最初の例である
: 56003, 56113, 56333, 56443, 56663, 56773, 56993.
 よって, この族の最初の数である56003は, このような性質を持つ最小の素数である.

桁を同じ数で置き換えることで8つの素数が得られる最小の素数を求めよ. (注:連続した桁でなくても良い)'''

import basic
import Prime

MAX = 1000000                   # 調査する素数の最大値　ひとまず百万とする

def numtoset(n):
    """ 引数nの整数値から、出現する数字の集合に変換する関数
        ただし、１の位の数字は返値の就業に含めない"""

    ansset = set()
    t = n

    while t > 0:
        a = t % 10
        t //= 10
        ansset.add(a)

    ansset.remove(n % 10)       # １の位の数字を取り除く

    return ansset


def exchangenum(n, a):
    """ 引数nの中に存在する数字aをa以外の数字に変換した整数値を
        集合で返す関数"""

    li = basic.inttolist(n)
    ans = set()

    for b in range(10):
        if a != b:
            newli = []
            t = n
            while t > 0:
                ta = t % 10
                t //= 10
                if ta == a:
                    newli.insert(0, b)
                else:
                    newli.insert(0, ta)

            if newli[0] != 0:                   # 先頭数字が０の場合は、戻り値から除外する
                ans.add(basic.listtoint(newli))

    return ans


def countprime(numset):
    """ 引数numset(集合）で与えられた数字の中に、素数がいくつあるか走査する関数
        戻り値は、素数の数"""

    ans = 0

    for p in numset:
        if Prime.is_prime(p):
            ans += 1

    return ans

    # for p in numset:
    #     if p in primelist:
    #         ans += 1
    # return ans


if __name__ == "__main__":

    @basic.time_log
    def test():
        prime = Prime.Prime(100)
        print(countprime({3, 5, 7}))


    @basic.time_log
    def main():
        prime = Prime.Prime(MAX)
        primelist = prime.get_prime_list()

        for p in primelist:
            pset = numtoset(p)

            for a in pset:
                if countprime(exchangenum(p, a)) == 7:
                    print("ans=", p)
                    return


    main()