import Prime
import time

def gcm(a,b):
    ''' ユークリッド互除法を用いて、最大公約数を求める関数'''
    r = a % b
    if r == 0:
        return b
    else:
        return gcm(b,r)


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



if __name__ == "__main__":
    it = Prime.PrimeIter(1000000)

    start = time.time()

    for n in it:
        print(n)

    elapsed_time = time.time() - start
    print("{0:.3}".format(elapsed_time))