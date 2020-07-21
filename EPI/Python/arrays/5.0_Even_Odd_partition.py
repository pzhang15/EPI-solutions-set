from typing import List
'''
Your input is an array of integers, 
and you have to reorder its entries so that the even entries appear first. 
This is easy if you use O(n) space, where n is the length of the array.
However, you are required to solve it without allocating additional storage.
'''
# O(N) time, O(1) space 
def even_odd_partition(A: List[int]) -> None:
    even, odd = 0, len(A) - 1 # even start on 0, odd start on last element
    while even < odd:
        if A[even] % 2 == 0:
            even += 1
        else:
            A[even], A[odd] = A[odd], A[even] # python swap is suprior!
            odd -= 1 # odd now must pointing to an odd number after the swap

A = [5, 3, 1, 4, 1, 4]

print(A)
even_odd_partition(A)
print(A) 