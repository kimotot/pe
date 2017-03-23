"""pe64の解答　N ≤ 10000 について奇数の周期をもつ平方根が何個あるか答えよ."""

import math
import basic

def renbunsu_sqrt(n):
    """nの平方根を連分数で表現する関数"""

    x = []
    y = [1]
    a = []

    a.append(int(math.sqrt(n)))
    x.append(-a[0])
    idx = 0
    flg = True

    while flg:
        x0 = x[idx]
        y0 = y[idx]

        y1 = (n - x0*x0) // y0
        a1 = int((math.sqrt(n) - x0) / y1)
        x1 = -x0 - a1*y1

        z = list(zip(x, y))
        del z[0]
        if (x1, y1) in z:
            flg = False
        else:
            x.append(x1)
            y.append(y1)
            a.append(a1)
            idx += 1

    return x, y, a


if __name__ =="__main__":

    def test():
        x, y, a = renbunsu_sqrt(23)
        print(x)
        print(y)
        print(a)


    def main():
        count = 0
        for n in range(2, 10001):
            if math.sqrt(n) != int(math.sqrt(n)):
                x, y, a = renbunsu_sqrt(n)
                print(n, a)
                if len(a) % 2 == 0:
                    count += 1

        print(count)

    main()

