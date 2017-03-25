"""pe65の解答"""

class RenbunE:
    """eを連分数で表現を管理するクラス"""

    def __init__(self, n = 100):
        """
        最大n項目まで、連分数を求める。その最大項を初期設定する
        :param n: 最大求める連分数の項番号
        """
        if n < 1:
            raise IndexError
        else:
            self._max = n

        self._list = [2]
        k = 0
        while len(self._list) < self._max-1:
            k += 1
            self._list.append(1)
            self._list.append(2 * k)
            self._list.append(1)

    @property
    def renbune_list(self):
        return self._list


def refunc(n, e, owari = 99):
    if n == owari:
        return e.renbune_list[n], 1
    else:
        (c, m) = refunc(n + 1, e, owari)
        a = e.renbune_list[n]
        return a*c+m, c


if __name__ == "__main__":

    def test():
        e = RenbunE()
        c, m = refunc(0, e, owari= 99)

        s = 0
        for n in str(c):
            s += int(n)

        print(s)

    test()
