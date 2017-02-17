# coding:UTF-8

import time
from functools import reduce

kajyoulist = []

#真の約数をもとめる関数
def shinyaku(num):
	
	list = []
	
	for i in range(1,num // 2 + 1):
		if num % i == 0:
			list.append(i)

	return(list)

#過剰数であるかを判定する関数
def kajyou(num):
	l = shinyaku(num)
	
	if reduce(lambda x,y:x+y,l) > num:
		return True
	else:
		return False

#過剰数のリストを返す関数
def kj(max):
	for n in range(12,max+1):
		if kajyou(n):
			kajyoulist.append(n)

#過剰数の和で表現できるか判定する関数
def kajyouwa(num):
	for a in kajyoulist:
		if a >= num:
			return False
		else:
			if num - a in kajyoulist:
				return True
	return False


start = time.time()
kj(1000)
elp = time.time() - start
print(kajyoulist)
print("{0} sec".format(elp))

ans =[]
for n in range(24,28123):
	if kajyouwa(n):
		ans.append(n)

print(ans)

