# サイコロをエミュレーションするクラス定義
# coding : UTF-8

import random

class Dice:
    '''多面体のサイコロをエミュレートするクラス定義'''

    def __init__(self,men = 6):
        ''' 引数をサイコロの面数として初期化する
            正多面体を想定し、4,6,8,12,20に限定する
            省略値は６とする'''
        if men == 4:
            self._men = 4
        elif men == 6:
            self._men = 6
        elif men == 8:
            self._men = 8
        elif men == 12:
            self._men = 12
        elif men == 20:
            self._men = 20
        else:
            print("引数が誤っています")
            raise IndexError

    @property
    def roll_dice(self):
        '''サイコロを振る'''
        self._val = random.randint(1,self._men)
        return self._val

    @property
    def men(self):
        '''サイコロの面数を得る'''
        return self._men

    @property
    def val(self):
        '''振ったサイコロの出目を返す'''
        return self._val


class Dice2:
    ''' サイコロを２個持っていて
        振ると、２つの目を返す'''

    def __init__(self,d1_men = 6,d2_men = 6):
        '''サイコロを２個生成する'''
        self._d1 = Dice(d1_men)
        self._d2 = Dice(d2_men)

    def roll_dice(self):
        '''２個のサイコロを振る'''
        return self._d1.roll_dice,self._d2.roll_dice

    def get_men(self):
        '''サイコロの面数を返す'''
        if self._d1.men == self._d2.men:
            return self._d1.men
        else:
            return self._d1.men,self._d2.men

    @property
    def deme(self):
        return self._d1.val, self._d2.val

    @property
    def demekei(self):
        return self._d1.val + self._d2.val

if __name__ == "__main__":
    da = Dice2()
    print(da.get_men())
    print(da.roll_dice())
    print(da.deme)
    print(da.demekei)

    # dic_val ={}
    # for _ in range(10000):
    #     m = d.roll_dice
    #
    #     if m in dic_val:
    #         dic_val[m] += 1
    #     else:
    #         dic_val[m] = 1
    # print(sorted(dic_val.items()))