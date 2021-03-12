import heapq
'''
Design an efficient algo for sorting a k-increasing-decreasing array
A = [57, 131, 493, 294, 221, 339, 418, 452, 443, 190]
'''


'''
Given a long sequence of numbers, each number is at most k away from its correctly sorted positions
i.g         [3, -1, 2, 6, 4, 5, 8] and k = 2, no number is 2 index away from its sorted positon
correct:    [-1, 2, 3, 4, 5, 6, 8]
print number in sorted order
'''
'''
Given a binary heap as an array, return top k largest element in the heap
'''
def sol(A, k):
    max_heap = [(-A[0], 0)]
    i = 0
    while k:
        value, idx = heapq.heappop(max_heap)
        print(-value)
        left_child = idx * 2 + 1
        right_child = idx * 2 + 2
        if left_child < len(A):
            heapq.heappush(max_heap, (-A[left_child], left_child))
        if right_child < len(A):
            heapq.heappush(max_heap, (-A[right_child], right_child))
        k -=1


A = [561, 314, 401, 28, 156, 359, 271, 11, 1]
k = 4
res = sol(A, k)
print(res)
