# coding:utf-8

import time

# 数字を英語表記した文字列を保持するリスト
e = [''] * 1001
e[1] = 'one'
e[2] = 'two'
e[3] = 'three'
e[4] = 'four'
e[5] = 'five'
e[6] = 'six'
e[7] = 'seven'
e[8] = 'eight'
e[9] = 'nine'
e[10] = 'ten'
e[11] = 'eleven'
e[12] = 'twelve'
e[12] = 'twelve'
e[13] = 'thirteen'
e[14] = 'fourteen'
e[15] = 'fifteen'
e[16] = 'sixteen'
e[17] = 'seventeen'
e[18] = 'eighteen'
e[19] = 'nineteen'
e[20] = 'twenty'
e[30] = 'thirty'
e[40] = 'forty'
e[50] = 'fifty'
e[60] = 'sixty'
e[70] = 'seventy'
e[80] = 'eighty'
e[90] = 'ninety'
e[100] = 'one hundred'
e[200] = 'two hundred'
e[300] = 'three hundred'
e[400] = 'four hundred'
e[500] = 'five hundred'
e[600] = 'six hundred'
e[700] = 'seven hundred'
e[800] = 'eight hundred'
e[900] = 'nine hundred'
e[1000] = 'one thousand'

# 空白以外の文字数をカウントする
def len_nonblank(str):
	
	ans = 0
	
	for c in str:
		if c != ' ':
			ans += 1
	
	return ans

for n in range(10,100):
	if e[n] == '':
		n1 = n % 10
		n10 = n // 10
		e[n] = e[n10 * 10] + ' ' + e[n1]

for n in range(100,1000):
	if e[n] == '':
		n100 = n // 100
		n10_ = n - n100 * 100
		
		e[n] = e[n100] + ' hundred and ' + e[n10_]

sum = 0

for n in range(1,1001):
	sum += len_nonblank(e[n])

print(sum)










