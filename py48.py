'''Problem 48 「自身のべき乗(self powers)」 †
次の式は, 11 + 22 + 33 + ... + 1010 = 10405071317 である.

では, 11 + 22 + 33 + ... + 10001000 の最後の10桁を求めよ.'''

import math

def main():
    sumint = 0
    for n in range(1,1001):
        sumint += n**n

    ans = []
    for _ in range(10):
        r = sumint % 10
        sumint //= 10
        ans.insert(0,r)

    return ans


if __name__ == "__main__":
    print(main())