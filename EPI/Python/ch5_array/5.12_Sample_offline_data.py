from typing import *
import random
'''
    Give an array and k, return a subset size of k randomly selected.
    ALl subset should equally likely

'''

def EPI_sol(k: int, A: List[int]) -> None:
    for i in range(k): # we will choose k elements
        r = random.randint(i, len(A) - 1) #use induction as a formal proof
        A[i], A[r] = A[r], A[i]
    
    return A[:k]

A = [3, 7, 5, 11]
res = EPI_sol(3, A)
print(res)
