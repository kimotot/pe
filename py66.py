"""pe66の解答"""

import math

def f(d):
    x = 1
    while True:
        print(x)
        t = (x*x -1) / d
        if t > 0 and t == int(t):
            y = math.sqrt(t)
            if y == int(y):
                return x, int(y)
        x += 1


if __name__ == "__main__":

    def test():
        print(f(61))


    def main():
        max_x = 0

        for d in range(62, 1001):
            td = math.sqrt(d)
            if td != int(td):
                print(d)
                x, y = f(d)
                if max_x < x:
                    max_x = x

        print(x)

    test()