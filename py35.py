# coding:UTF-8

# 100万未満の循環素数の個数を求める

import math
import time


def get_sosu(maximum):
	# 引数max以下の循環素数を求める
	# 戻り値は求めた素数を含むリスト
	# なお、1は素数に含めない

	sosu_list = [2, 3]  # 自明の素数をセットしておく

	for n in range(5, maximum, 2):

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
	"""引数を桁数分回転した数字列のリストを返す関数
	   引数は、基本となる正の整数値
	   戻り値は、リスト"""

	# 引数を各桁ごとの数字のリストに変換する
	split_list = []

	n1 = num % 10
	n10 = num // 10

	while (n1 > 0) or (n10 > 0):
		split_list.insert(0,n1)
		n1 = n10 % 10
		n10 = n10 // 10

	# split_listからローテートした数字を求める
	c = 0
	n_split_list = [list(split_list)]
	while c < len(split_list) - 1:
		t = split_list[0]
		split_list.pop(0)
		split_list.append(t)
		n_split_list.append(list(split_list))
		c += 1

	# 整数値に戻す
	int_list = []
	for one_split_list in n_split_list:
		s = 0
		for n in one_split_list:
			s = s*10 + n

		int_list.append(s)


	return int_list


def all_kisu(num):
	"""全ての数字が奇数であるか判定する関数
	   """

	# 引数を各桁ごとの数字のリストに変換する
	split_list = []

	n1 = num % 10
	n10 = num // 10

	while (n1 > 0) or (n10 > 0):
		split_list.insert(0,n1)
		n1 = n10 % 10
		n10 = n10 // 10

	iskisu = True
	for n in split_list:
		if n % 2 == 0:
			iskisu = False
			break

	return iskisu

if __name__ == "__main__":
	MAX = 1000000

	start_time = time.time()

	slist = get_sosu(MAX)

	elapsed_time = time.time() - start_time
	print("経過時間={0:.3}".format(elapsed_time))

	coun = 0
	for n in slist:
		if all_kisu(n):
			rs = all_rotate(n)

			isprime = True
			for nrs in rs:
				if nrs in slist:
					pass
				else:
					isprime = False
					break

			if isprime:
				coun += 1
			print(n)

	print(coun)

	elapsed_time = time.time() - start_time
	print("経過時間={0:.3}".format(elapsed_time))

