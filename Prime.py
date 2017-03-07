# 素数を列挙するイテレータクラスのモジュールファイル

import math
import basic

class PrimeIter:
    '''素数を列挙するイテレータクラス'''

    def __init__(self, max = 0):
        ''' 生成する素数の最大値を設定する
            値の最小値は２
            引数が２以下の数字であったら、maxに０を設定する。この場合、無限に素数を生成する
            1は素数ではない'''
        if max < 2:
            self._max = 0
        else:
            self._max = max

    def __iter__(self):
        '''イテレータとして初期化する'''
        self._n = 1          # 1の次の数字（２）から素数の探索を始める
        self._prime_list = []    # クラス内部で求めた素数を保持するリスト
        return self

    def __next__(self):
        '''nの次の素数を探索して返す'''
        while True:
            self._n += 1
            if self._max !=0 and self._n > self._max:
                raise StopIteration

            # 今までに見つけた全ての素数で割り切れなければ素数である
            # もしくは割ろうと試みる数字が、sqrt(n)以上になれば素数である
            is_prime = True
            q = math.sqrt(self._n)

            for p in self._prime_list:
                if p > q:
                    is_prime = True
                    break

                if self._n % p == 0:
                    is_prime = False
                    break

            if is_prime:
                self._prime_list.append(self._n)
                return self._n

    def get_prime_list(self):
        '''インスタンス内部で保持している素数リストを返す関数'''
        return self._prime_list

    def get_nth_prime(self,nth):
        ''' ２から初めてn番目の素数を返す関数
            先頭の素数は０番目とする'''
        if nth <= len(self._prime_list):
            return self._prime_list[nth]
        else:
            raise IndexError


class Prime:
            '''素数をリスト形式で保持するクラス'''

            def __init__(self, max = 2):
                ''' 生成する素数の最大値を設定する
                    値の最小値は２
                    引数が２以下の数字であったら、maxに強制的に２を設定する。
                    1は素数ではない'''

                self._prime_list = []

                if max < 2:
                    self._max = 2
                else:
                    self._max = max

                self._n = 2
                while self._n <= self._max:
                    # 今までに見つけた全ての素数で割り切れなければ素数である
                    # もしくは割ろうと試みる数字が、sqrt(n)以上になれば素数である
                    is_prime = True
                    q = math.sqrt(self._n)

                    for p in self._prime_list:
                        if p > q:
                            is_prime = True
                            break

                        if self._n % p == 0:
                            is_prime = False
                            break

                    if is_prime:
                        self._prime_list.append(self._n)

                    self._n += 1

            def get_prime_list(self):
                '''インスタンス内部で保持している素数リストを返す関数'''
                return self._prime_list

            def get_nth_prime(self, nth):
                ''' ２から初めてn番目の素数を返す関数
                    先頭の素数は０番目とする'''
                if nth <= len(self._prime_list):
                    return self._prime_list[nth]
                else:
                    raise IndexError


def is_prime(num):
    '''引数が素数であるか判定する関数'''

    if num % 2 == 0:
        return False
    else:
        sq = int(math.sqrt(num))
        for i in range(3, sq+1, 2):
            if num % i == 0:
                return False

    return True

# 100以下の素数を列挙する
if __name__ == "__main__":

    MA = 1000000

    @basic.time_log
    def test():
        prime = PrimeIter()
        for p in prime:

            if p > MA:break


    @basic.time_log
    def test2():
        prime = Prime(MA)

    test()
    test2()