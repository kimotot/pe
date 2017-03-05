'''pe38の解答'''

def pangegital_check(num):
    ''' 引数nの積がパンデジタルかチェックする関数'''

    dig_string = ""
    n = 0

    while True:
        n += 1
        dig_string += str(num * n)
        if len(dig_string) == 9:
            return pandegital(dig_string), num, dig_string
        elif len(dig_string) > 9:
            return False, num, dig_string


def pandegital(string):
    t_set = set(string)
    if t_set == {str(x) for x in range(1,10)}:
        return True
    else:
        return False


if __name__ == "__main__":

    ans_a = 0
    ans_n = 0
    for i in range(1,10000):
        b,n,s = pangegital_check(i)

        if b:
            a = int(s)
            if ans_a < a:
                ans_a = a
                ans_n = n
    print(ans_n,ans_a)