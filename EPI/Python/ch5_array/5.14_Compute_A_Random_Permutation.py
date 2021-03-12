from typing import *

'''
    Design an algorithm that create unifromly random permutations of 0~N, you are given a randome number generator 
'''
# random sampling from 5.12
def random_samplig(k: int, A: List[int]) -> None:
    for i in range(k): # we will choose k elements
        r = random.randint(i, len(A) - 1) #use induction as a formal proof
        A[i], A[r] = A[r], A[i]
    
    return A[:k]
#把原本的k变为n， 用induction即可证明正确性
def EPI_sol(n: int) -> List[int]:
    permutation = list(range(n))
    random_samplig(n, permutation)
    return permutation
