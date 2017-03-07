'''pe44の解答'''

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

    def __init__(self, maxn = 10000):
        ''' 生成する五角数の最大項数を保存する '''
        self._maxn = maxn
        self._pentagonal_list = []

        # 五角数は Pn = n(3n-1)/2 で生成される'''
        for self._n in range(1,self._maxn+1):
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


    @property
    def maxn(self):
        return self._maxn

if __name__ == "__main__":

    def test_main():
        pentagon = Pentagonal_Number()

        print(pentagon.get_pentagonal_list())



    def main():

        max_d = 99999999999

        pentagon = Pentagonal_Number()

        for k in range(2,pentagon.maxn+1):
            print(k)
            j = k - 1
            while j > 0:
                kvalue = pentagon.get_nth_pentagonal(k)
                jvalue = pentagon.get_nth_pentagonal(j)
                temp_d = kvalue - jvalue
                if pentagon.is_pentagonal(temp_d) \
                        and temp_d < max_d\
                        and pentagon.is_pentagonal(kvalue + jvalue):
                    max_d = temp_d
                    ans = (j,k)
                    print(ans,jvalue , kvalue, max_d)
                j -= 1

    main()