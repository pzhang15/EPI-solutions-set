from typing import *

'''
Write a program which takes as input an array of digits encoding a decimal number D 
and updates the array to represent the number D + 1. 
is (1,2,9) then you should update the array to (1,3,0). 
Your algorithm should work even if it is implemented in a language that has finite-precision arithmetic.
'''

def add_one_my_sol(A: List) -> int:
    carry, p = 0, len(A) - 1
    while(p >= 0):
        if p == len(A) - 1: 
            increment = A[p] + 1
        else:
            increment =  A[p] + carry
        carry =  increment // 10
        A[p] = increment % 10
        p = p - 1

    if carry == 1:
        return [1] + A
    else:
        return A
#O(N)
def add_one_EPI_sol(A: List) -> int:
    
    A[-1] += 1 #这是精髓，我们总想着上来进入forloop来进行increment，里面再设置很多的if很复杂

    #实际上我们是步骤，1.increment 2.check进位
    #这样子比混在一起在一个forloop里面要好得多
    for i in reversed(range(1, len(A))):
        if A[i] != 10:
            break
        A[i] = 0
        A[i - 1] += 1
    #if none of them is not equal to 10 = if all of them is equal to 10
    else: #for else 的精髓, 如果没有任何一次if，则会execute else
          #这样子我们就知道A[1] ~A[N - 1]必定都是9， 所以我们再进行一次check   
        if A[0] == 10:
            A[0] = 1 #A slick way to add 1 without O(N) complexity
            A.append(0)
    return A

A = [1, 2, 9 ]
res1 = add_one_my_sol(A)
print(res1)

A = [1, 2, 9 ]
res2 = add_one_EPI_sol(A)
print(res2)
