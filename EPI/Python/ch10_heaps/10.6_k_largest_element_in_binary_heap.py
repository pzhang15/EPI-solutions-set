import heapq
'''
Given a binary heap as an array, return top k largest element in the heap
'''
def sol(A, k):
    res = []
    max_heap = [(-A[0], 0)] #A[0] is the largest one
    for _ in range(k):
        candidate = heapq.heappop(max_heap)
        res.append(-candidate[0])
        idx = candidate[1]
        left_child = 2*idx + 1
        if left_child < len(A):
            heapq.heappush(max_heap, (-A[left_child], left_child))
        right_child = 2*idx + 2
        if right_child < len(A):
            heapq.heappush(max_heap, (-A[right_child], right_child))
    return res

A = [561, 314, 401, 28, 156, 359, 271, 11, 1]
k = 4
res = sol(A, k)
print(res)

