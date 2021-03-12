from typing import *
import random
'''
Write a program that taken a array A of n numbers,
and rearranges A's elememts tp get a mew array B having the property that B[0] <= B[1] >= B[2] <= B[3] ...
For example: [1, 3, 2, 4, 0, 5]

foloow up: IN-PLACE
'''
#start swapping first half and second half
def naive_sol_1(A: List[int]) -> None:
    A.sort()
    n, start, end = len(A), 1, len(A) // 2 
    while(start < n and end < n):
        print(start, ' ', end)
        A[start], A[end] = A[end], A[start]
        start += 2
        end +=1

# swapping two adjacent element
def naive_sol_2(A: List[int]) -> None:
    A.sort()
    for i in range(0, len(A) - 1, 2):
        A[i], A[i + 1] = A[i + 1], A[i]
    
#quick select to find median, then re-arrange the element around the median
def quick_select_kth(A: List[int], k: int) -> int:
    def partition(left, right, pivot_idx):
        pivot_val = A[pivot_idx]
        write_idx = left - 1
        for j in range(left, right):
            if(A[j] <= pivot_val):
                write_idx += 1
                A[write_idx], A[j] = A[j], A[write_idx]
                
        # Swap the pivot to where it belongs:
        # All things on the left is less than pivot , all things on the right is bigger than the pivot        
        A[write_idx + 1], A[pivot_idx] = A[pivot_idx], A[write_idx + 1]
        return write_idx + 1
    #begin our scan
    left, right = 0, len(A) - 1
    while(left <= right):
        pivot_idx = random.randint(left, right)
        new_pivot_idx = partition(left, right, pivot_idx)
        print(new_pivot_idx, ' ', k)
        if new_pivot_idx == k:
            return A[new_pivot_idx]
        elif new_pivot_idx <= k:
            left = new_pivot_idx + 1
        else:
            right = new_pivot_idx - 1

def quick_median_sol(A: List[int]) -> None:
    n = len(A)
    median = quick_select_kth(A, n//2)
    print(median)
#重新翻译一下题目：
#当i为even的时候， i + 1的数字要小于等于第i个
#当i为odd的时候， i + 1的数字要大于等于第i个
#我们只需要针对i的奇偶性， 检查A[i]和A[i + 1] 的属性， 如果有非法属性， 我们就只需要swap就行
#为什么只swap就行，因为要么小于等于，要么大于（反之亦然）。只有两个选择，我们进行swap就可以达成反方向的合法条件
#而且有个细节就是swap具有传导性，可能某个element会被swap不止一次
#O(n)
def EPI_sol(A:List[int]) -> None:
    for i in range(len(A)):
        #ascending sort i and i + 1 if i is even, other wise 
        # bool(i %2) i 是even的时候 会等于0， 那么bool(0) = False, 也就是ascending sort
        A[i: i + 2] = sorted(A[i:i + 2], reverse=bool(i%2))

#write it out more explicitely
def my_sol_2(A:List[int]) -> None:
    for i in range(len(A) - 1):
        if i % 2 == 0:
            if A[i] > A[i + 1]:
                A[i], A[i + 1] = A[i + 1], A[i]
        else:
            if A[i] < A[i + 1]:
                A[i], A[i + 1] = A[i + 1], A[i]



A = [1, 3, 2, 4, 0, 5, -1, 2, 1]
my_sol_2(A)
print(A)
