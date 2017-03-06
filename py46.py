'''pe46の解答'''

import basic
import Prime

def is_odd_composite_number(n):
    '''引数nが奇数の合成数であるか判定する関数'''

    i = 1
    r = n - (i**2) * 2

    while r > 0:
        if Prime.is_prime(r):
            return True

        i += 1
        r = n - (i**2) * 2
    else:
        return False


class Odd_composite_number:
    ''' 奇数の合成数を発生させるイテレータクラス
        ９以上で素数でない奇数とする'''

    def __init__(self,max_number = 0):
        ''' 生成する合成数の最大値を設定する
            最大値以下の数字までとする'''
        self._max = max_number


    def __iter__(self):
        '''イテレータを初期化する'''
        self._count = 0         #生成した合成数の個数をカウントする変数を初期化する
        self._prime = Prime.PrimeIter()
        self._head = 9
        return self


    def __next__(self):

        for self._p in self._prime:
            if self._max !=0  and self._head > self._max:
                raise StopIteration

            if self._head == self._p:
                self._head += 2
            else:
                while self._p > self._head:
                    ans = self._head
                    self._head += 2
                    self._count += 1
                    return ans



if __name__ == "__main__":

    @basic.time_log
    def test():
        it = Odd_composite_number(100)
        for x in it:
            print(x)

    @basic.time_log
    def main():
        it = Odd_composite_number()

        for x in it:
            if is_odd_composite_number(x):
                pass
            else:
                print(x)
                break

    main()
