# coding:UTF-8


def kai(n):
	"""
	正の整数の階乗を求める関数
	:rtype: 階乗の計算結果
	"""
	if n == 1:
		return 1
	else:
		return n * kai(n - 1)

print(kai(11))
