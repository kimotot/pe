'''Problem 50 「連続する素数の和」 †
素数41は6つの連続する素数の和として表せる:

41 = 2 + 3 + 5 + 7 + 11 + 13.
100未満の素数を連続する素数の和で表したときにこれが最長になる.

同様に, 連続する素数の和で1000未満の素数を表したときに最長になるのは953で21項を持つ.

100万未満の素数を連続する素数の和で表したときに最長になるのはどの素数か?'''

import Prime
import basic

MAX = 1000000

def is_prime_permulation(primelist, head, n):
    '''引数の素数列(primelist)のhead番目(先頭は0番とする)から
        連続するｎ個の素数の和が、素数であるか判定する関数'''

    s = sum(primelist[head:head + n])

    if s in primelist:
        return True, s
    else:
        return False, s




if __name__ == "__main__":

    @basic.time_log
    def main():
        prime = Prime.Prime(MAX)
        primelist = prime.get_prime_list()

        maxlen = 21
        maxhead = 0
        ans = 0

        for head in range(len(primelist)):
            n = maxlen + 1
            f, s = is_prime_permulation(primelist, head, n)

            if s > MAX:
                print("head=",head)
                break

            while s < MAX:
                if f:
                    maxhead = head
                    maxlen = n
                    ans = s
                    print(maxhead, n, ans)

                n += 1
                f, s = is_prime_permulation(primelist, head, n)

    @basic.time_log
    def test():
        prime = Prime.Prime(MAX)
        primelist = prime.get_prime_list()

        print(primelist[4703:4724])


    main()
