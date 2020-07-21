from typing import *
'''
Suppose A = ⟨0, 1, 2, 0, 2, 1, 1⟩, and the pivot index is 3. 
Then A[3] = 0, so ⟨0, 0, 1, 2, 2, 1, 1⟩ is a valid partitioning. 
For the same array, if the pivot index is 2, then A[2] = 2, 
so the arrays ⟨0, 1, 0, 1, 1, 2, 2⟩ as well as ⟨0, 0, 1, 1, 1, 2, 2⟩ are valid partitionings.

Write a program that takes an array A and an index i into A, 
and rearranges the elements such that all elements less than A[i] (the “pivot”) appear first, 
followed by elements equal to the pivot, followed by elements greater than the pivot.
'''
# O(N) time, O(N) space
def trivial_solution(A: List[int], x: int) -> None:
    pivot = A[x]
    less = [a for a in A if a < pivot]
    equal = [a for a in A if a == pivot]
    greater = [a for a in A if a > pivot]
    return less + equal + greater

#O(N^2) time , O(1) space
def constant_space_sol(A: List[int], x: int) -> None:
    pivot = A[x]
    for i in range(len(A)): # keep track of the last smaller element index， 
        #j会因为每次i而重复检查是否有小于pivot， 我们可以进行简化
        for j in range(i + 1, len(A)):
            if A[j] < pivot:
                A[j], A[i] = A[i], A[j]
                break
    # by the end of this, 0 ~ i element will all be smaller than pivot
    
    # alternate iteration method, similar to Java or C++
    # #               start, stop, step 
    for i in range(len(A) - 1, -1, -1):    
        for j in range(i - 1, -1, -1): 
            if(A[j] > pivot):
                A[j], A[i] = A[i], A[j]
                break
    
    # this iteration method is from EPI
    # for i in reversed(range(len(A))):
    #     for j in reversed(range(i)):
    #         if(A[j] > pivot):
    #             A[j], A[i] = A[i], A[j]
    #             break

    # ---- for comparison between two iteration methods-----
    # for i in reversed(range(len(A))):
    #     print(i, end= ' ')
    #     for j in reversed(range(i)):
    #         print(j, end= ' ')
    #     print()
    # print("----------------")
    # for i in range(len(A) - 1, -1, -1):
    #     print(i, end= ' ')
    #     for j in range(i - 1, -1, -1):
    #         print(j, end= ' ')
    #     print()

#O(N) time , O(1) space
def two_pass_sol(A: List[int], x: int) -> None:
    pivot = A[x]
    # get rid of redundant loop 
    less = 0
    for i in range(1, len(A)):
        if A[i] < pivot:
            A[i], A[less] = A[less], A[j]
            less += 1
    
    greater = len(A) - 1
    for i  in range(greater - 1, -1, -1):
        if A[i] > pivot:
            A[i], A[greater] = A[greater], A[i]
            greater -=1

# Keep the 4 invariant during partitioning
# bottom [:less]
# middle [less:equal]
# unclassified [equal:larger]
# top [larger:]

#O(N) time , O(1) space
def one_pass_sol(A: List[int], x: int) -> None:
    pivot = A[x]
    smaller, equal, larger = 0, 0, len(A) - 1
    #keep iterate until there is no unclassified element
    #smaller和equal指针都起始0，equal和smaller进行分离以后，equal和smaller中间隔着的必定是和pivot equal值的
    while equal < larger:
        if A[equal] < pivot:
            A[smaller], A[equal] = A[equal], A[smaller]
            smaller, equal =  smaller + 1, equal + 1
        elif A[equal] == pivot:
            equal += 1
        else: # A[equal] > pivot
            A[larger], A[equal] = A[equal], A[larger]
            larger -= 1
            

A = [0, 1, 2, 0, 2, 1, 1]
x = 1
#constant_space_sol(A, x)
#two_pass_sol(A, x)
one_pass_sol(A, x)
print(A)