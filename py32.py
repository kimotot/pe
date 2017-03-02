# coding:UTF-8

# 整数値のリスト
li = [1,2,3,4,5,6,7,8,9]

def pickone(selected):
    if len(li) == 0:
        print(selected)
    else:
        for ix,x in enumerate(li):
            del li[ix]
            selected.append(x)
            pickone(selected)

            selected.pop()
            li.insert(ix,x)

def pan23(selected):
    selected

pickone([])

