'''pe39解答'''

def triangel(p):
    ''' 直角三角形の編の長さの合計がpの時に、
        辺の組み合わせ数を返す関数
        p>=3であること'''

    count = 0
    for a in range(1,p-1):
        for b in range(a,p-2):
            c = p-a-b
            if a**2 + b**2 == c**2:
                count += 1
                print(a,b,c,)
    return count


if __name__ == "__main__":

    maxi = 0
    maxp = 0

    for p in range(3,1001):
        m = triangel(p)
        if m > maxi:
            maxi = m
            maxp = p

    print(maxp)