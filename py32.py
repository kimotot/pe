# coding:UTF-8

import copy
import time

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
    ''' 与えられたリスト要素の順列を求める関数
        引数はリストなど、イテーラブルなもの
        戻値は全ての順列を要素としてリストにしたもの
        再帰呼び出し関数'''

    if len(origin) == 0:
        yield []
    else:
        for index, header in enumerate(origin):
            new_orign = copy.deepcopy(origin)
            del new_orign[index]

            for cuder in permutationsIt(new_orign):
                cuder.insert(0, header)
                yield cuder


def pandegi14(alist):
    '''１から９の数字列が、1X４のパンデジタルであるか判定する関数'''
    x = alist[0]
    y = alist[1]*1000 + alist[2]*100 + alist[3]*10 + alist[4]
    z = alist[5]*1000 + alist[6]*100 + alist[7]*10 + alist[8]

    if x * y == z:
        return True,z
    else:
        return False,0


def pandegi23(alist):
    '''１から９の数字列が、２X３のパンデジタルであるか判定する関数'''
    x = alist[0]*10 + alist[1]
    y = alist[2]*100 + alist[3]*10 + alist[4]
    z = alist[5]*1000 + alist[6]*100 + alist[7]*10 + alist[8]

    if x * y == z:
        return True,z
    else:
        return False,0


if __name__ == "__main__":

    start = time.time()

    s = set()

    for n in permutationsIt([1,2,3,4,5,6,7,8,9]):
        b,z = pandegi14(n)
        if b:
            print(14,n)
            s.add(z)

        b,z = pandegi23(n)
        if b:
            print(23,n)
            s.add(z)

    print("総和={0}".format(sum(s)))

    elapsed_time = time.time() - start
    print("処理時間={0:.4f}".format(elapsed_time))


