'''pe41の解答'''

import Prime
import basic


if __name__ == "__main__":

    @basic.time_log
    def main():
        prime = Prime.PrimeIter()

        ans = 0
        for p in prime:
            if p < 10000000:
                #     if is_pandigital(p):
                #         print(len(str(p)),p)
                #         if ans < p:
                #             ans = p
                print(p)
            else:
                break

        print(ans)


    @basic.time_log
    def main2():
        origin_list = [9,8,7,6,5,4,3,2,1]

        while len(origin_list) > 0:
            for li in basic.permutationsIt(origin_list):
                dig = basic.permutationToInt(li)
                print(li,dig)
                if Prime.is_prime(dig):
                    print(dig)
                    return dig
    
            origin_list.pop(0)

    main2()
