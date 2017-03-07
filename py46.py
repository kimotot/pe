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


class Odd_composite_number_Iterator:
    ''' 奇数の合成数を発生させるイテレータクラス
        ９以上で素数でない奇数とする'''

    def __init__(self,max_number = 0):
        ''' 生成する合成数の最大値を設定する
            最大値以下の数字までとする'''
        self._max = max_number


    def __iter__(self):
        '''イテレータを初期化する'''
        self._count = 0         #生成した合成数の個数をカウントする変数を初期化する
        self._head = 7
        return self


    def __next__(self):
        ''' 素数でない奇数を奇数合成数とし、
            ９から始めて奇数合成数を発生させる関数
            最大max値まで生成するが、max=0の場合、無限に発生させる'''
        while True:
            self._head += 2
            if self._head > self._max != 0:
                raise StopIteration

            if Prime.is_prime(self._head):
                pass
            else:
                self._count += 1
                return self._head


if __name__ == "__main__":

    @basic.time_log
    def test():
        it = Odd_composite_number_Iterator()
        for x in it:
            print(x)

    @basic.time_log
    def main():
        it = Odd_composite_number_Iterator(10)

        for x in it:
            if is_odd_composite_number(x):
                pass
            else:
                print(x)
                break

    test()
