from typing import *
'''
Write a program which takes as input a sorted array
Updates it so that all duplicates have been removed 
and the remaining elements have been shifted left to fill the emptied indices. 
Return the number of valid elements. 
Many languages have library functions for performing this operation—you cannot use these functions.
Hint: There is an 0(n) time and 0(1) space solution.
'''
#错误写法，不要拿j和j - 1进行比较， 因为 1 2 3 或者 1 1 2 这种在两个段落之间不会形成A[j] == A[j - 1]
#正确写法是拿j 和 i比较，i为上一次写入的数值
def wrong_sol(A: List) -> None:
    i = 0 # write index
    for j in range(len(A)):
        A[i] = A[j]
        i = i + 1
        while(A[j] == 0 or A[j] == A[j - 1]):
            j = j + 1
            if(j >= len(A)): break
        print(j)

        
    A = A[:i]

def EPI_sol(A: List) -> List:
    #为什么我们要1起始进行写入，因为我们写入的位置会覆盖，所以一定要在上一个unique element的下一个进行写入，
    #而下面 A[write_index - 1] 实际上是寻找上一个写入的unique element
    for j in range(1, len(A)):
        #！！！思考一下A[write_index - 1] 和 起始于1的关系
        if A[write_index - 1] != A[j]:
            A[write_index] = A[j]
            write_index += 1
    return A[:write_index]

def my_alterantive_sol(A: List) -> None:
    i, j = 0, 1 # i is the write index
    while(j < len(A)):
        while j < len(A) - 1 and A[i] == A[j] :
            j = j + 1
        
        i = i + 1
        A[i] = A[j]
        print(i, " ", j)
        j = j + 1

    return A[:i + 1]


A = [1, 1, 2, 2, 2, 3]

res = EPI_sol(A)

print(res)