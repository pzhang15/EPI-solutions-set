from typing import *
import itertools
import random
import bisect
'''
given N number, and N probabilities(p1 ~ pN, sums to 1)
given a randome number generator that produces value in [0, 1)
generate on eof the n numbers according to the speicifed probabilities

for example, if the numbers are 3, 5, 7, 11, and the probabilities are 9/18, 6/18, 2/18, 1/18, 
then in 1,000,000 calls to your programs,  1 million
3 should appear roughly 500000 times,  1 mil * 9/18 = 500, 000
5 should appear rouglhly 333333 times, 
7 shold appear rougly 111111 times, 
11 should appear roughly 55555 times

'''

def EPI_sol(values: List[int], prob: List[float]) -> int:
    #用hashmap不可以， 因为其中是要用到interval的距离无法快速的进行lookup， 还是需要进行遍历
    #所以我们不如用排序好的进行二分查找
    # dic = {}
    # sum = 0
    # for i in range(len(prob)):
    #     #put interval -> number in our dictionary 
    #     dic[(sum, sum + prob[i])] = values[i]
    prefix_sum_interval = list(itertools.accumulate(prob))
    print(prefix_sum_interval)
    rand = random.random()
    print(rand)
    idx = bisect.bisect(prefix_sum_interval, rand) #返还贴近右边的数字，第一个大于他的数字， 正好和我们的n - 1个的墙对应n个区间（数字）对对应
    print("idx: ", idx)
    return values[idx]

val = [3, 5, 7, 11]
prob =[9/18, 6/18, 2/18, 1/18]
res = EPI_sol(val , prob)
print(res)