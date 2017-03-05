'''pe37の回答'''

import Prime

def leftcut(n):
    '''引数を左から切り詰めた数字をリスト形式で返す関数'''

    keta = 0
    t = n

    while t > 0:
        keta += 1
        t = t // 10

    ans = set()
    t = n
    keta -= 1
    while keta > 0:
        n = n % 10**keta
        ans.add(n)
        keta -= 1

    r = list(ans)
    r.sort()
    return r


def rightcut(n):
    ans = set()

    t = n // 10
    while t > 0:
        ans.add(t)
        t //= 10

    r = list(ans)
    r.sort()

    return r


def leftrightOK(n):
    li = leftcut(n)
    for t in li:
        if not(t in prime.get_prime_list()):
            return False

    li = rightcut(n)
    for t in li:
        if not(t in prime.get_prime_list()):
            return False

    return True

if __name__ == "__main__":

    count = 0
    s = 0
    prime = Prime.PrimeIter()

    for n in prime:
        if n >= 11:
            if leftrightOK(n):
                count += 1
                s += n

                if count >= 11: break

    print(s)