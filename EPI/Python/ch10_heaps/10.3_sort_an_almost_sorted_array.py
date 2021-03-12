import heapq
'''
Given a long sequence of numers, each number is at most k away from its correctly sorted positions
i.g         [3, -1, 2, 6, 4, 5, 8] and k = 2, no number is 2 index away from its sorted positon
correct:    [-1, 2, 3, 4, 5, 6, 8]

'''
def sol(A, k):
    min_heap = []
    for i in range(k): #不用k + 1, 因为之后的pushpop会先push再pop
        heapq.heappush(min_heap, A[i])
    res = []
    
    for i in range(k, len(A)):
        smallest = heapq.heappushpop(min_heap, A[i])
        res.append(smallest)
    while min_heap:
        res.append(heapq.heappop(min_heap))
    return res