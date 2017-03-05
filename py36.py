'''pe36の回答'''
# coding:UTF-8

def kaibun(n,base = 'd'):
    '''１０進数の引数nが回文であるか判定する関数'''

    origin_string = format(n,base)
    reverse_string = ""

    for c in origin_string:
        reverse_string = c + reverse_string

    if origin_string == reverse_string:
        return True
    else:
        return False


if __name__ == "__main__":

    s = 0
    for n in range(1,1000000):
        if kaibun(n,'d') & kaibun(n,'b'):
            s += n

    print(s)
