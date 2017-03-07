''' 三角数, 五角数, 六角数は以下のように生成される.

    三角数	Tn=n(n+1)/2	1, 3, 6, 10, 15, ...
    五角数	Pn=n(3n-1)/2	1, 5, 12, 22, 35, ...
    六角数	Hn=n(2n-1)	1, 6, 15, 28, 45, ...
    T285 = P165 = H143 = 40755であることが分かる.

    次の三角数かつ五角数かつ六角数な数を求めよ.'''

class NunberIterator:
    ''' n角数を発生させる基本クラス'''

    def __init__(self,func, max_number = 0):
        ''' n角数を発生させる最大値を設定する
            指定がなければ0を設定する。その場合は無限に発生させる
            また、n角数を発生させる数式を設定する'''
        self._max = max_number
        self._func = func


    def __iter__(self):
        ''' イテレータとしての初期化処理
            次に発生させる数の項番号を記憶する
            1から数えるものとし、初期値は0とする'''
        self._n = 0
        return self


    def __next__(self):
        ''' n項目(self._n)の数を生成する'''
        if self._n > self._max > 0:
            raise StopIteration

        self._n += 1
        return self._func(self._n)





if __name__ == "__main__":

    def test():
        nc = NunberIterator(max_number = 10, func = lambda x:x * (3*x-1) //2 )
        for n in nc:

            print(n)


    def main():
        tn_it = iter(NunberIterator(func = lambda x: x * (x + 1) // 2))
        pn_it = iter(NunberIterator(func = lambda x: x * (3*x - 1) // 2))
        hn_it = iter(NunberIterator(func = lambda x: x * (2*x - 1)))
        tn = next(tn_it)
        pn = next(pn_it)
        hn = next(hn_it)

        while True:
            if tn == pn == hn:
                print(tn,pn,hn)
                tn = next(tn_it)
                pn = next(pn_it)
                hn = next(hn_it)

            elif tn <= pn and tn <= hn:
                tn = next(tn_it)
            elif pn <= tn and pn <= hn:
                pn = next(pn_it)
            else:
                hn = next(hn_it)


    main()