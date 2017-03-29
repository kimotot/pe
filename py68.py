"""pe68の解答
xo + x1 + y0 = n
x1 + x2 + y1 = n
x2 + x3 + y2 = n
x3 + x4 + y3 = n
x4 + x0 + y4 = n

全ての式を足し合わせると
2*(x0+x1+x2+x3+x4) + (y0+y1+y2+y3+y4) = 5n
2X + Y = 5n ---①

また、X+Y は1から10の合計になるので、
X + Y = 55 ---②

①-②は
X = 5n - 55
X = 5(n-11)

すなわち、Xは５の倍数で、その範囲は 15 <= X <= 35
(Xに10は含まれないから）

以上より
X   Y   n
15  40  14
20  35  15
25  30  16
30  25  17
35  20  18
"""

import basic

def ispentagonal(x, y):
    """
    五角形が成立しているか判定する関数
    :param x:
    :param y:
    :return:
    """
    n0 = x[0] + x[1] + y[0]
    n1 = x[1] + x[2] + y[1]
    n2 = x[2] + x[3] + y[2]
    n3 = x[3] + x[4] + y[3]
    n4 = x[4] + x[0] + y[4]

    if n0 == n1 == n2 == n3 == n4:
        return True
    else:
        return False


def getkouho():
    """
    五角形問題の候補数字を作成する
    :return:
    """

    resultx = []
    for x in basic.kumiawase(5, [1, 2, 3, 4, 5, 6, 7, 8, 9]):
        if sum(x) % 5 == 0:
            resultx.append(x)

    result = []
    base = set(range(1,11))

    for x in resultx:
        y = base - set(x)
        y = list(y)
        y.sort()
        result.append((x, y))

    return result


def getdetailkouho(x, y):
    ys = []

    ret = basic.permutations(y[1:])
    for t in ret:
        ys.append([y[0]] + t)

    xs = basic.permutations(x)

    for tx in xs:
        for ty in ys:
            if ispentagonal(tx, ty):
                s = str(ty[0]) + str(tx[0]) + str(tx[1])
                s = s + str(ty[1]) + str(tx[1]) + str(tx[2])
                s = s + str(ty[2]) + str(tx[2]) + str(tx[3])
                s = s + str(ty[3]) + str(tx[3]) + str(tx[4])
                s = s + str(ty[4]) + str(tx[4]) + str(tx[0])
                print(tx, ty, s)



if __name__ == "__main__":

    def test():
        getdetailkouho([1,2,3,4,5], [6,7,8,9,10])

    @basic.time_log
    def main():
        ret = getkouho()
        for (x, y) in ret:
            getdetailkouho(x, y)

    main()