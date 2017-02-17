# coding:UTF-8

from functools import reduce

ans = []

for a6 in range(10):
	for a5 in range(10):
		for a4 in range(10):
			for a3 in range(10):
				for a2 in range(10):
					for a1 in range(10):
						a =  a6 * 100000 + a5 * 10000 + a4 * 1000 + a3 * 100 + a2 *10 + a1
						k =  a6**5 + a5**5 + a4**5 + a3**5 + a2**5 + a1**5
						if a == k:
							ans.append(a)

print(ans)
print(reduce(lambda x,y:x+y, ans))
