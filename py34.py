# coding:UTF-8


def kai(n):
	# 正の整数の階乗を求める関数
	# 階乗の計算結果
	if n == 1:
		return 1
	else:
		return n * kai(n - 1)


def set_klist():
	# 0〜9の階乗値をグローバル変数klistに保存する関数
	for n in range(1, 10):
		if n == 1:
			klist.append(1)
		else:
			klist.append(klist[n - 1] * n)


def is_kaijyowa(n):
	# 正の整数値の各桁の階乗和と、整数値が等しいか判定する関数
	sum = 0

	n10 = n // 10
	n1 = n - n10 * 10

	while (n1 > 0) or (n10 > 0):
		sum = sum + klist[n1]
		t = n10
		n10 = n10 // 10
		n1 = t - n10 * 10

	if sum == n:
		return True
	else:
		return False


if __name__ == '__main__':
	klist = [0]
	set_klist()

	s = 0

	for n in range(20000000,30000000):
		if is_kaijyowa(n):
			s = s + n
			print(n)

	print(s)
