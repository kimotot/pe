"""Problem 61 「巡回図形数」 †
三角数, 四角数, 五角数, 六角数, 七角数, 八角数は多角数であり, それぞれ以下の式で生成される.

三角数	P3,n=n(n+1)/2	1, 3, 6, 10, 15, ...
四角数	P4,n=n2	1, 4, 9, 16, 25, ...
五角数	P5,n=n(3n-1)/2	1, 5, 12, 22, 35, ...
六角数	P6,n=n(2n-1)	1, 6, 15, 28, 45, ...
七角数	P7,n=n(5n-3)/2	1, 7, 18, 34, 55, ...
八角数	P8,n=n(3n-2)	1, 8, 21, 40, 65, ...
3つの4桁の数の順番付きの集合 (8128, 2882, 8281) は以下の面白い性質を持つ.

この集合は巡回的である. 最後の数も含めて, 各数の後半2桁は次の数の前半2桁と一致する
それぞれ多角数である: 三角数 (P3,127=8128), 四角数 (P4,91=8281), 五角数 (P5,44=2882) がそれぞれ別の数字で集合に含まれている
4桁の数の組で上の2つの性質をもつはこの組だけである.
三角数, 四角数, 五角数, 六角数, 七角数, 八角数が全て表れる6つの巡回する4桁の数からなる唯一の順序集合の和を求めよ."""

import basic
import copy

funcs_dic = {3: lambda n: n*(n+1)//2,
             4: lambda n: n*n,
             5: lambda n: n*(3*n-1)//2,
             6: lambda n: n*(2*n-1),
             7: lambda n: n*(5*n-3)//2,
             8: lambda n: n*(3*n-2)}

ndic = {}

def setnlist():
    for idx, f in funcs_dic.items():
        n = 1
        p = f(n)
        result = []
        while p < 10000:
            if p >= 1000:
                pu = p // 100
                pd = p % 100
                if pd > 9:
                    result.append((pu, pd))
            n += 1
            p = f(n)

        ndic[idx] = result


def getsets(max = 8):
    result = []

    if max < 3 or max > 8:
        raise IndexError
    else:
        ans = basic.permutations(list(range(max-1, 2, -1)))
        for x in ans:
            x.insert(0, max)
            result.append(x)

    return result


def find_nlevel(target, nlevel, aset):
    if nlevel < 0 or nlevel >= len(aset): raise IndexError

    target_nlist = [(xup, xdown) for (xup, xdown) in ndic[aset[nlevel]] if xup == target]

    if nlevel == len(aset)-1 :
        result = [[x] for x in target_nlist]
        return result
    else:
        result = []
        for (xup, xdown) in target_nlist:
            ans = find_nlevel(xdown, nlevel+1, aset)

            for x in ans:
                x.insert(0, (xup, xdown))
                result.append(x)

        return result


if __name__ == "__main__":

    @basic.time_log
    def test():
        setnlist()
        for idx, nlist in ndic.items():
            print(idx, nlist)

        sets = getsets(max = 8)

        for (xup, xdown) in ndic[8]:
            for aset in sets:
                result = find_nlevel(xdown, 1, aset)

                for x in result:
                    if xup == x[len(x)-1][1]:
                        print([(xup, xdown)] + x)
                        ans = copy.copy(x)
                        ans.insert(0, (xup, xdown))

                        s = 0
                        for y in ans:
                            s += y[0] * 100
                            s += y[1]
                        print(s)


    test()
