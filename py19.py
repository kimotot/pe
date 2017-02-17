# coding:UTF-8

import time

# 対象年がうるう年か判定する関する
def isuru(y):
	if y % 4 == 0:
		if (y % 400 != 0) & (y % 100 == 0):
			return False
		else:
			return True
	else:
		return False

# 各月の曜日を保持するリスト
# 1900年から始まる
# 0:月1:火 2:水 3:木 4:金 5:土 6:日 
cal = [[9] * 12 for i in range(102)]

cal[0][0] = 0

for y in range(101):
	for m in range(12):
		
		month = m + 1
		dd = 0
		
		if m == 11:
			y_1 = y + 1
			m_1 = 0
		else:
			y_1 = y
			m_1 = m + 1

		if (month == 1) | \
			(month == 3) | \
			(month == 5) | \
			(month == 7) | \
			(month == 8) | \
			(month == 10) | \
			(month == 12):
			dd = 3
		elif (month == 4) | \
			(month == 6) | \
			(month == 9) | \
			(month == 11):
			dd = 2
		else:
			if isuru(1900 + y):
				dd = 1
			else:
				dd = 0
		
		d = cal[y][m]
		cal[y_1][m_1] = (d + dd) % 7

c = 0

for y in range(1,101):
	for m in range(12):
		if cal[y][m] == 6:
			c += 1

print(c)

