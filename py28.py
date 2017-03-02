# プロジェクトオイラー Problem28
# coding:UTF-8

MAX_LOOP = 500

def get_rightup(max = MAX_LOOP):
    ''' 中心からみて右斜め上方向に出現する数字列を求める関数
        最大max個まで求める
        先頭（0番目）は1である'''

    list_rightup = [1]
    n = 1

    while n <= max:
        list_rightup.append(list_rightup[n-1] + n*8)
        n += 1

    return list_rightup


def get_other(list_rightup,max = MAX_LOOP):
    '''中心から見て左上・左下・右下方向に出現する数字列を求める関数
        右上方向に出現する数字列を引数とし、それをもとに他列を求める
        あとで総計を求める作業を簡単にするため先頭（０番目）は０とする'''

    list_leftup = [0]
    list_leftdown = [0]
    list_rightdown = [0]

    n = 1

    while n <= max:
        list_leftup.append(list_rightup[n] - (2*n) * 1)
        list_leftdown.append(list_rightup[n] - (2*n) * 2)
        list_rightdown.append(list_rightup[n] - (2*n) * 3)
        n += 1
    return list_leftup,list_leftdown,list_rightdown

if __name__ == "__main__":
    li_rightup = get_rightup()
    li_leftup,li_leftdown,li_rightdown = get_other(li_rightup)

    s = 0
    for nlist in [li_rightup,li_leftup,li_leftdown,li_rightdown]:
        s += sum(nlist)
    print(s)