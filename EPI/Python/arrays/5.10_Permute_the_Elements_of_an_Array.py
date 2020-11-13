from typing import *

'''
Given an array A and a permutation array P, produce the permuted array
    A: [a, b, c, d]
    P: [2, 0, 1, 3]
          \/  /  |
          / \/   |
         /  /\   |             
  res: [b, c, a, d]
Now do it in-place

'''
def EPI_sol(A: List[int], P:List[int]) -> None:
    for i in range(len(A)):
        #为什么要有while？为什么不每次进行swap完就结束了呢？
        #我们可以手动跑一下地下的test case
        #首先思考， 为什么这个time complexity是O(N)？for循环 + while难道不应该是N^2?
        #经过手动demo， 针对于当前i， 我们可以把当前的i想象成一个锚点， 经过锚点的所有点都会swap到正确的位置上面去
        #所以其实只需要n次swap就可以把每个点换到正确的地方
        #但是：【虽然每次swap之后会把一个数字换到正确的位置， 但位置的正确性不是从左到右的，
        #       我们需要while来确定当前锚点i也是正确的，
        #       也就是说for循环从左到右的属性需要while来确保每个i的正确性】
        #顾我们需要while 循环和for循环进行配合来确保结束时，每个位置的正确性。

        while P[i] != i:
            A[P[i]], A[i] = A[i], A[P[i]]
            P[P[i]], P[i] = P[i], P[P[i]]

A = ['a', 'b', 'c', 'd']
P = [2, 3, 1, 0]
EPI_sol(A, P)
print(A)

