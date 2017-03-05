'''pe40の解答'''

def syo(keta):
    '''少数ketaまでの循環少数を求める関数'''

    ans = ""
    n = 1

    while len(ans) < keta:
        ans += str(n)
        n += 1

    return ans


if __name__ == "__main__":
    a = syo(1000001)

    result = 1

    for k in range(7):
        result = result * int(a[10**k - 1])

    print(result)
