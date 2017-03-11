'''pe44の解答'''

import basic

class Pentagonal_Number_Iterator:
    ''' 五角数を生成するクラス'''

    def __init__(self, maxn = 0):
        ''' 生成する五角数の最大項数を保存する '''
        self._maxn = maxn
        self._pentagonal_list = []


    def __iter__(self):
        ''' イテレータをコールされたて際に初期化する
            生成する項番を１に設定する'''
        self._n = 1
        return self


    def __next__(self):
        ''' イテレータ
            五角数は Pn = n(3n-1)/2 で生成される'''
        if self._maxn != 0 and self._n > self._maxn:
            raise StopIteration

        p = self._n * (3*self._n-1) // 2
        self._n += 1

        self._pentagonal_list.append(p)
        return p


    def get_pentagonal_list(self):
        return self._pentagonal_list


    def is_pentagonal(self, n):
        if n in self._pentagonal_list:
            return True
        else:
            return False


    def get_nth_pentagonal(self,n):
        return self._pentagonal_list[n-1]


class Pentagonal_Number:
    ''' 五角数を生成するクラス'''

    def __init__(self, maxn = 3000):
        ''' 生成する五角数の最大項数を保存する
            引数値が省略されて場合は、10000を最大値とする'''
        self._maxn = maxn
        self._pentagonal_list = []

        # 五角数は Pn = n(3n-1)/2 で生成される
        for self._n in range(1, self._maxn + 1):
            p = self._n * (3*self._n - 1) // 2
            self._pentagonal_list.append(p)

    def get_pentagonal_list(self):
        return self._pentagonal_list

    def is_pentagonal(self, n):
        if n in self._pentagonal_list:
            return True
        else:
            return False

    def get_nth_pentagonal(self,n):
        return self._pentagonal_list[n-1]

    def get_max_pentagonal(self):
        return self._pentagonal_list[self._maxn - 1]

    @property
    def maxn(self):
        return self._maxn


if __name__ == "__main__":

    def test_main():
        pentagon = Pentagonal_Number()
        for i,n in enumerate(pentagon.get_pentagonal_list()):
            print(i, n)

    @basic.time_log
    def pe44():
        ps = set()
        i = 2
        while True:
            i += 1
            print(i)
            s = (3 * i * i - i) // 2
            for Pj in ps:
                if s - Pj in ps and s - 2 * Pj in ps:
                    return s - 2 * Pj
            ps.add(s)

    @basic.time_log
    def main():

        def sol44():
            for s in range(3, pentagon.maxn + 1):
                print(s)
                sv = pentagon.get_nth_pentagonal(s)
                for k in range(1, s-1):
                    kv = pentagon.get_nth_pentagonal(k)
                    if pentagon.is_pentagonal(sv - kv) and pentagon.is_pentagonal(sv - 2*kv):
                        print(kv, sv-kv, sv-2*kv)
                        return

        pentagon = Pentagonal_Number()

        sol44()


    pe44()

