"""Problem 62 「立方数置換」 †
立方数 41063625 (3453) は, 桁の順番を入れ替えると2つの立方数になる: 56623104 (3843) と 66430125 (4053) である. 41063625は, 立方数になるような桁の置換をちょうど3つもつ最小の立方数である.

立方数になるような桁の置換をちょうど5つもつ最小の立方数を求めよ."""

table = {}

def number_count(n):
    d = {}

    for c in str(n):
        if c in d.keys():
            d[c] += 1
        else:
            d[c] = 1

    print(d)
    ans_str = ""
    for i in range(10):
        if str(i) in d.keys():
            ans_str += str(d[str(i)])
        else:
            ans_str += "0"

    return ans_str


if __name__ == "__main__":

    def test():
        print(number_count(1122334499885566))


    def main():
        n = 1
        while True:
            n3 = n * n * n
            n_str = number_count(n3)
            print(n, n3)

            if n_str in table.keys():
                li = table[n_str]
                li.append((n, n3))
                table[n_str] = li

                if len(li) == 5:
                    print(li)
                    return 0
            else:
                table[n_str] = [(n, n3)]

            n += 1

    main()