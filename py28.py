#coding:UTF-8

z = [[0]*1001 for i in range(1001)]

def getz(x,y):
	return z[x+500][y+500]

def setz(x,y,v):
	z[x+500][y+500] = v

for x in range(-500,501):
	for y in range(-500,501):
		setz(x,y,x+y)

for count in range(1,501):
	sx = count				#その周回で最初に数字を埋めるマスのＸ
	sy = y + count - 1		#その周回で最初に数字を埋めるマスのＹ
	sn = getz(sx-1,y)		#その周回で最初に埋めるマスの数字
	