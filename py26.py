# coding: utf-8

import time
from functools import reduce

#1から始めて割った時の余りの数字列を求める関数
def amari(n):
	ans = [1]
	
	while True:
		m = len(ans) - 1
		a = ans[m]*10 % n
		
		if a in ans:		#余り数字がリストに存在する。すなわち循環分数である
			ans.append(a)
			return ans,True
		elif a == 0:
			ans.append(a)			#余り数字が０。すなわち割り切れており、循環分数ではない
			return ans,False
		else:
			ans.append(a)
			
	return ans,ansj


maxketa = 0
maxi = 0
for i in range(2,1000):
	(a,j) = amari(i)
	
	if j:
		last = len(a) -1
		idx = a.index(a[last])
		keta = last - idx
		if keta >= maxketa:
			maxketa = keta
			maxi = i

print( maxketa,maxi)
