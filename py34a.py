from math import factorial as fact
from timeit import default_timer as timer

start = timer()
def findFactorialSum():
    factorials = [fact(x) for x in range(0, 10)] # pre-calculate products
    total_sum = 0
    for k in range(10, fact(9) * 7): # 9999999 is way more than its fact-sum
        if sum([factorials[int(x)] for x in str(k)]) == k:
            total_sum += k
            print(k)

    return total_sum

ans = findFactorialSum()
elapsed_time = (timer() - start) * 1000 # s --> ms

print("Found {0} in {1} ms.".format(ans, elapsed_time))