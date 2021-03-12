from typing import *
import itertools
import random
'''
    Design a program that takes as input a size k and reads packets, 
    continuouly maintain a uniform random subset of size k of the read packets
    题目要求在k个packet之后， 之后每个packet都有uniform的概率被选中
''' 
def EPI_sol(stream: Iterator[int], k: int) -> List[int]:
    #itearate first k element from the iteratable's, stop until the iterator hasNext return false
    running_sample = list(itertools.islice(stream, k))
    n = k
    # for loop for Iterator object in python is actually implemented as while with try and catch block
    '''
    while True:
        try:
            element = next(iter_obj)
        except StopIteration:
            break
    '''
    for num in stream:
        n += 1
        #generate a number between 0~n, if it's less than k, 
        #then replace that element with the new element num
        #选择replace的概率 = 新number被选中的应有概率 = k/(n + 1)
        #当有新的element读取的时候，
        #很巧妙的将原本问题：需要重新选择第(n + 1)以 k/(n + 1)的概率变成了选择以k/(n + 1) 概率去去除原本k里面的一个
        #正确性的证明为 induction
       
        # induction hypothesis：
        # all -sized subsets are equally likely after n >= k packets has been read
        idx_to_replace = random.randrange(n)
        if idx_to_replace < k:
            running_sample[idx_to_replace] = num

    return running_sample

A = [3, 6, 1, 5, 4, 7]

k = 3
stream = iter(A)
sample = EPI_sol(stream , k)

print(sample)
