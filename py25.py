# coding: utf-8

import time
from functools import reduce

#二つのリスト要素を加算する
def addlist(list1,list2):
	nlist1 = len(list1)
	nlist2 = len(list2)
	ans = []
	
	if nlist1 > nlist2:
		for i in range(nlist2):
			ans.append(list1[i] + list2[i])
		for i in range(nlist2,nlist1):
			ans.append(list1[i])
	else:
		for i in range(nlist1):
			ans.append(list1[i] + list2[i])
		for i in range(nlist1,nlist2):
			ans.append(list2[i])

	i = 0
	while i < len(ans):
		t = ans[i]
		ans[i] = t % 10
		tt = t // 10
		if tt >0:
			if i ==  len(ans) - 1:
				ans.append(tt)
			else:
				ans[i+1] += tt
		i += 1
			
	return ans

#フィボリストに次の要素（フィボナッチ数）を一つ追加する
f1 = [1]
f2 = [1]
n = 2

while len(f2) < 1000:
	f = addlist(f1,f2)
	f1 = f2
	f2 = f
	n += 1

print(f2,n)



		