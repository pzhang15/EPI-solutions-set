from typing import *

#brute force solution就是从2-n每个数字，尝试是否有factor
#对于我每个数字i ，我们尝试 1～ 根号（i）
#所以brute force是 n * 根号n = O（n^3/2）

#我们也可以反向来（buttom up），对于每个数字，把他的所有multiple都筛掉，
#！【一个数字可以被factor也意味着，他一定是某个数字的倍数】

def generates_primes(n: int) -> List[int]:
    primes = [] #empty list to store our primes
    #boolean array to represent ith element is prime or not
    is_prime = [False, False] + [True] * (n - 1) # total N slot, 0, 1 are not primes
    for i in range(2, n + 1):
        #为什么一定是is_prime[i] = True 的时候进行筛选呢？
        #因为假如i个是个composite number， 那么他的multiple也一定被之前的prime筛掉过
        #理解prime power decomposition的定理也可以帮助更好的理解这里
        if is_prime[i]: 
            primes.append(i)
            # Sieve i's multiples
            for i in range(i * 2, n + 1, i):
                is_prime[i] = False
    return primes

    