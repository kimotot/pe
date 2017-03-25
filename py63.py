"""Problem 63 「べき乗の桁の個数」 †
5桁の数 16807 = 75は自然数を5乗した数である. 同様に9桁の数 134217728 = 89も自然数を9乗した数である.

自然数を n 乗して得られる n 桁の正整数は何個あるか?"""


count = 0

for base in range(1, 10):
    n = 1
    flag = True
    while flag:
        target = base ** n
        if len(str(target)) == n:
            print(base, n, target)
            count += 1
            n += 1
        else:
            flag = False

print(count)
