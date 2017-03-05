'''pe43の解答'''

import basic

def listToInt(li):
    '''リスト形式の数字列を整数値に変換する関数'''
    s = 0
    for n in li:
        s = s*10 + n
    return s

def check(li):
    ''' 引数のリストが、問題の条件に合致するか判定する関数
        d2d3d4=406 は 2 で割り切れる
        d3d4d5=063 は 3 で割り切れる
        d4d5d6=635 は 5 で割り切れる
        d5d6d7=357 は 7 で割り切れる
        d6d7d8=572 は 11 で割り切れる
        d7d8d9=728 は 13 で割り切れる
        d8d9d10=289 は 17 で割り切れる'''

    # 先頭が０はだめ
    if li[0] == 0:
        return False

    # 数字のリストを文字列として結合する
    # d2d3d4は２で割り切れる
    n = listToInt(li[1:4])
    if n % 2 != 0:
        return False

    # d3d4d5 = 063は3割り切れる
    n = listToInt(li[2:5])
    if n % 3 != 0:
        return False

    # d4d5d6は５で割り切れる
    n = listToInt(li[3:6])
    if n % 5 != 0:
        return False

    # d5d6d7で７で割り切れる
    n = listToInt(li[4:7])
    if n % 7 != 0:
        return False

    # d6d7d8は11で割り切れる
    n = listToInt(li[5:8])
    if n % 11 != 0:
        return False

    # d7d8d9は13で割り切れる
    n = listToInt(li[6:9])
    if n % 13 != 0:
        return False

    # d8d9d10は17で割り切れる
    n = listToInt(li[7:10])
    if n % 17 != 0:
        return False

    return True



if __name__ == "__main__":

    @basic.time_log
    def main():

        s = 0

        for alist in basic.permutationsIt([0,1,2,3,4,5,6,7,8,9]):
            if check(alist):
                print(alist)
                s += listToInt(alist)

        print(s)

    main()