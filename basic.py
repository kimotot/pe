import Prime
import time
import copy
import random
import math

def gcd(a,b):
    ''' ユークリッド互除法を用いて、最大公約数を求める関数'''
    r = a % b
    if r == 0:
        return b
    else:
        return gcd(b, r)


def prime_factorization(n):
    '''単純に２からルートｎまでで割り算する手法で、
        素因数分解を行う
        返値は素因数分解結果のリスト
        引数が素数の場合は、その素数のみを含む、要素数が１のリストを返す'''
    if n <= 1:
        raise IndexError
    elif 2 <= n <= 3:
        return [n]
    else:
        for i in range(2, int(math.sqrt(n)) + 2):
            if n % i == 0:
                ans = prime_factorization(n // i)
                ans.insert(0, i)
                return ans
        return [n]


def pollard_rho(n):
    '''ロー法を用いて、素因数を求めるプログラム'''
    def f(x, a, n):
        return (x * x * x + a) % n

    x = random.randint(0, n-1)
    y = x
    a = random.randint(1, n-3)

    d = 0
    while d <= 1:
        x = f(x,a,n)
        y = f(y,a,n)
        y = f(y,a,n)
        d = gcd(x-y,n)

    return d


def yaku(n):
    ''' 引数nの約数を求める関数
        約数をリストの形式で返却する'''
    pit = Prime.PrimeIter()     #素数を無限に生成するイテレーションクラス
    ans = []
    t = n

    while True:
        for x in pit:
            if x >= t:
                ans.append(x)
                return ans

            if t % x == 0:
                ans.append(x)
                t = t / x
                break


def is_pandigital(n):
    '''引数nがパンデジタルであるか判定する関数'''
    k = len(str(n))

    l = set(str(n))
    r = set(str(x) for x in range(1,k+1))

    if l == r:
        return True
    else:
        return False


def permutations(origin):
    ''' 与えられたリスト要素の順列を求める関数
        引数はリストなど、イテーラブルなもの
        戻値は全ての順列を要素としてリストにしたもの
        再帰呼び出し関数'''

    if len(origin) == 0:
        return [[]]
    else:
        ans = []
        for index,header in enumerate(origin):
            new_orign = copy.deepcopy(origin)
            del new_orign[index]

            for cuder in permutations(new_orign):
                cuder.insert(0,header)
                ans.append(copy.deepcopy(cuder))

        return ans


def permutationsIt(origin):
    ''' 与えられた引数（リスト要素）の順列を求めるイテレーション
        引数はリストなど、イテーラブルなもの
        戻値は全ての順列を要素としてリストにしたもの
        再帰呼び出しを利用している'''

    if len(origin) == 0:
        yield []
    else:
        for index, header in enumerate(origin):
            new_orign = copy.deepcopy(origin)
            del new_orign[index]

            for cuder in permutationsIt(new_orign):
                cuder.insert(0, header)
                yield cuder


def permutationToInt(li):
    ''' 引数は一つの順列
        それを整数値に変換する関数'''
    sum = 0
    for n in li:
        sum = sum * 10 + n

    return sum

def time_log(func):
    ''' デコレータ
        関数の処理時間を計測し表示する関数'''

    def wrapper(*args, **kwargs):
        start = time.time()
        print("---Start---")
        result = func(*args, **kwargs)
        elapsed_time = time.time() - start
        print("---End---")
        print("処理時間={0:.6f}".format(elapsed_time))

    return wrapper



if __name__ == "__main__":

    @time_log
    def test():
        for n in range(10,1000000):
            print(n, prime_factorization(n))


    test()
