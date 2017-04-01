"""pe69の解答"""

import basic


def tagainiso(n):

    ans = 0
    for i in range(1, n):
        if basic.gcd(n, i) == 1:
            ans += 1

    return ans


if __name__ == "__main__":

    @basic.time_log
    def test():

        for n in range(1, 10000):
           tagainiso(n)


    test()