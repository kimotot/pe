"""Problem 57 「平方根の近似分数」 †
2の平方根は無限に続く連分数で表すことができる.

√ 2 = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...
最初の4回の繰り返しを展開すると以下が得られる.

1 + 1/2 = 3/2 = 1.5
1 + 1/(2 + 1/2) = 7/5 = 1.4
1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...

次の3つの項は99/70, 239/169, 577/408である. 第8項は1393/985である. これは分子の桁数が分母の桁数を超える最初の例である.

最初の1000項を考えたとき, 分子の桁数が分母の桁数を超える項はいくつあるか?"""

import basic

class sqrtiterator:
    """２の平方根の近似値を発生させるイテレータ"""

    def __init__(self, max):
        """発生させる最大の項番号を保存する"""
        self._max = max

    def __iter__(self):
        """イテレータとしての初期処理を行う"""
        self._n = 0         #今まで発生させた項の番号　初期値は0にする
        self._vlist = []    #今までに発生させた近似値を保存するリスト
        return self

    def __next__(self):
        """イテレータとして、n番目の近似値を発生させる"""
        self._n += 1

        if self._n > self._max:
            raise StopIteration
        elif self._n == 1:
            self._vlist.append((3, 2))
            return 3, 2
        else:
            (c_1, m_1) = self._vlist[self._n - 2]
            m = c_1 + m_1
            c = m + m_1
            self._vlist.append((c, m))
            return c,m


if __name__ == "__main__":

    @basic.time_log
    def test():

        count = 0
        sit = sqrtiterator(1000)
        for (c,m) in sit:
            print(c,m)
            if len(str(c)) > len(str(m)):
                count += 1

        print(count)


    test()



