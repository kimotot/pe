# coding: utf-8

import time
from functools import reduce

ans = []

#リストから辞書配列に従い数列を求める関数
def diclist(eranda,nokori):
		if len(nokori) == 1:		#候補リストに１個の要素しかない場合
			eranda2 = list(eranda)
			eranda2.append(nokori[0])
			ans.append(eranda2)
		else:
			for i in nokori:			#候補リストに複数の要素が残っている場合
				eranda2 = list(eranda)
				eranda2.append(i)
				nokori2 = list(nokori)
				nokori2.remove(i)
				diclist(eranda2,nokori2)


diclist([],[0,1,2,3,4,5,6,7,8,9])
print(ans[1000000-1])

				