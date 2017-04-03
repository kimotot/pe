"""pe69の解答"""

import basic
from fractions import Fraction


if __name__ == "__main__":

    @basic.time_log
    def main():

        maxfai = 0
        maxn = 0

        for n in range(2, 1000000):
            pset = basic.prime_factorization_set(n)

            fai = n
            for p in pset:
                fai = fai * (1 - Fraction(1, p))

            print(n, fai)
            tfai = n / fai

            if tfai > maxfai:
                maxfai = tfai
                maxn = n

        print(maxn, maxfai)


    main()
