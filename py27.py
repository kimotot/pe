#coding:UTF-8

import time
import functools

'''
	コメント
	
	
'''

# 引数以下の素数を求めリストとして返す関数
def getsosu(max):
	list_sosu = [1]


	def is_sosu(n):
		for s in list_sosu[1:]:
			if n % s == 0:
				return False
		else:
			return True


	
	if max <= 0:
		return "負数はダメ"
	elif max == 1 or max == 2:
		return [1]
	else:
		for n in range(3,max+1,2):
			if is_sosu(n):
				list_sosu.append(n)
		else:
			return list_sosu

start = time.time()

print(getsosu(10000))

elp_time = time.time() - start
print("{0:6.3f} sec".format(elp_time))


