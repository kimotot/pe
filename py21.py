# coding:UTF-8

import time
from functools import reduce

#約数の和を求める関数
def yakuwa(n):
	ans = [1]
	for i in range(2,n//2+1):
		if n % i == 0:
			ans.append(i)
	return(reduce(lambda x,y:x+y,ans))

list = [0]
for i in range(1,10000):
	list.append(yakuwa(i))

r = []
for a in range(1,10000):
	b = list[a]
	if (b != 0) & (b < 10000):
		if (list[b] == a) & (a != b):
			r.append(a)
			r.append(b)
			list[a] = 0
			list[b] = 0

print(r)
print(reduce(lambda x,y:x+y,r))

