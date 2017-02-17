# coding:UTF-8

li = []

for a in range(2,101):
	for b in range(2,101):
		li.append(a ** b)

list_uniqe = list(set(li))
list_uniqe.sort()

print(len(list_uniqe))
