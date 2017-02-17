# coding: UTF-8

import time

def col(n):
	ans = []
	
	if n == 1:
		return [1]

	elif n % 2 == 0:
		return [n] + col(n // 2)

	else:
		return [n] + col(n * 3 + 1)

def num_col(n):
	if n <= MAX:
		if list[n] != 0:
			return list[n]
		else:
			if n == 1:
				list[1] = 1
				return 1
			elif n % 2 == 0:
				list[n] = num_col(n // 2) + 1
				return list[n]
			else:
				list[n] = num_col(n * 3 + 1) + 1
				return list[n]
	elif n % 2 == 0:
		return num_col(n // 2) + 1
	else:
		return num_col(n * 3 + 1) + 1
		

start = time.time()

# コラッツ数を記録しておくデータベース（リスト）を用意する

MAX = 3000000			# リストの最大値
list = [0]*(MAX + 1)	# 配列の添字が０始まりなので、MAX+1個のリストを0で初期化しておく

# 1から1000000までのコラッツ数を求める
for i in range(1,1000001):
	list[i] = num_col(i)

idx = 0
ans = 0
for i in range(1,1000001):
	if list[i] > ans:
		ans = list[i]
		idx = i

print(idx,ans)

elp = time.time() - start
print("経過時間:{0}".format(elp)) 

#for n in range(1,14):
#	print(n,col(n))
