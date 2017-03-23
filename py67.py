"""pe67の解答"""

triangle = []


def settriangle():

    with open("files/triangle.txt", "r") as f:
        lines = f.readlines()
        for aline in lines:
            li = aline.strip().split(" ")
            li = [int(x) for x in li]
            triangle.append(li)


def tatamikomi():

    for n in range(len(triangle) -1 , 0, -1):
        for m in range(len(triangle[n])-1):
            if triangle[n][m] > triangle[n][m+1]:
                triangle[n-1][m] += triangle[n][m]
            else:
                triangle[n - 1][m] += triangle[n][m+1]


if __name__ == "__main__":

    def test():
        settriangle()
        tatamikomi()
        print(triangle[0][0])

    test()
