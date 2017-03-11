'''Problem 49 「素数数列」 †
項差3330の等差数列1487, 4817, 8147は次の2つの変わった性質を持つ.

(i)3つの項はそれぞれ素数である.
(ii)各項は他の項の置換で表される.
1, 2, 3桁の素数にはこのような性質を持った数列は存在しないが, 4桁の増加列にはもう1つ存在する.

それではこの数列の3つの項を連結した12桁の数を求めよ.'''

import Prime

def get4primelist():
    '''４桁の素数のリストを得る関数'''
    prime = Prime.Prime(10000)
    primelist = list(filter(lambda x:1000<=x<=9999, prime.get_prime_list()))

    return primelist

def searchtriple(primelist):
    ''' 引数の素数リストの中から、等差の３数字をみつける'''
    for i in range(len(primelist) - 2):
        for j in range(i+1, len(primelist) - 1):
            iv = primelist[i]
            jv = primelist[j]
            diff = jv -iv
            if jv + diff in primelist and is_rotate(iv,jv,jv+diff):
                print(iv,jv,jv+diff)

def is_rotate(*args):
    ''' 引数の３つの数が、転置数字であるか判定する'''
    ans = []

    for i in args:
        ans.append(sorted([c for c in str(i)]))

    for n in range(1,len(ans)):
        if ans[0] != ans[n]:
            return False

    return True


if __name__ == "__main__":
    searchtriple(get4primelist())

