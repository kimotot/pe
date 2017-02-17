# coding:utf-8
import time

# 数字リストの足し算
def list_plus(lista,listb):
	listans = []
	
	numa = len(lista)
	numb = len(listb)
	
	if numa < numb:
		nummin = numa
	else:
		nummin = numb

	for i in range(nummin):
		listans.append(lista[i] + listb[i])

	if numa > numb:
		for i in range(numb,numa):
			listans.append(lista[i])
	elif numa < numb:
		for i in range(numa,numb):
			listans.append(listb[i])

	i = 0
	while i < len(listans):
		t = listans[i] // 10
		listans[i] = listans[i] % 10
		
		if t > 0:
			if i == len(listans) - 1:
				listans.append(t)
			else:
				listans[i+1] += t

		i += 1

	return listans

def list_kake(lista,n):
	listans = list(lista)
	for i in range(len(listans)):
		listans[i] = listans[i] * n

	i = 0
	while i < len(listans):
		t = listans[i] // 10
		listans[i] = listans[i] % 10
		
		if t > 0:
			if i == len(listans) - 1:
				listans.append(t)
			else:
				listans[i+1] += t

		i += 1


	return listans

def add_func(a,b):
	return a+b

lista = [1]
for i in range(2,101):
	lista = list_kake(lista,i)

sum = 0
for i in lista:
	sum += i
		
print(sum)

