#coding:UTF-8

def kai(n):
	if n== 1:
		return 1
	else:
		return n*kai(n-1)

print(kai(9))
