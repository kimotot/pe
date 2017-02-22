# coding:UTF-8

# 100万未満の循環素数の個数を求める

import math
import time

def get_sosu(maximum):
	# 引数max以下の循環素数を求める
	# 戻り値は求めた素数を含むリスト
	# なお、1は素数に含めない

	sosu_list = [2,3]				# 自明の素数をセットしておく

	for n in range(5,maximum,2):

		sq = int(math.sqrt(n))

		isprime = True
		for prime in sosu_list:
			if prime > sq:
				isprime = True
				break
			elif n % prime == 0:
				isprime = False
				break

		if isprime:
			sosu_list.append(n)

	return sosu_list


def rotate(num):
	# 引数の数値を一桁回転してずらす
	# 最上位桁を１の位にもってくる

	# numの桁数を求める
	keta = 0
	n = num

	while n > 0:
		n = n // 10
		keta += 1

	ntop = num // (10 ** (keta - 1))
	return (num - ntop * (10 ** (keta - 1))) * 10 + ntop


def all_rotate(num):
	# 引数の数をローテーとしたすべての数持ったリストを返す関数

	ans = [num]
	r = rotate(num)

	while r != num:
		ans.append(r)
		r = rotate(r)
	else:
		return ans

if __name__ == "__main__":
	MAX = 10000

	start_time = time.time()

	slist = get_sosu(MAX)

	print(slist)

	for n in slist:
		rs = all_rotate(n)
		isprime = True
		for nrs in rs:
			if nrs in slist:
				pass
			else:
				isprime = False
				break

		if isprime:
			print(n)

	elapsed_time = time.time() - start_time
	print("経過時間={0:.3}".format(elapsed_time))