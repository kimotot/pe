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
            new_orirign = copy.deepcopy(origin)
            del new_orirign[index]

            for cuder in permutations(new_orirign):
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



# 整数値のリスト
li = [1,2,3,4,5,6,7,8,9]

def pickone(selected):
    if len(li) == 0:
        yield selected
    else:
        for ix,x in enumerate(li):
            del li[ix]
            selected.append(x)
            pickone(selected)

            selected.pop()
            li.insert(ix,x)


if __name__ == "__main__":

    start = time.time()

    for n in permutationsIt([1,2,3,4,5,6,7,8,9]):
        pass

    elapsed_time = time.time() - start
    print("処理時間={0:.4f}".format(elapsed_time))


