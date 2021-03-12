import collections
'''
compute both the min and max with less than 2N comparison
A = [3, 2, 5, 1, 2, 4]
return 1 and 5, which is min and max
'''
def sol(A):
    min_1, max_1 = A[0], A[1]
    for i in range(2, len(A), 2):
        print(i)
        if A[i] < A[i + 1]:
            local_min, local_max = A[i], A[i + 1]
        else:
            local_min, local_max = A[i + 1], A[i]
        min_1 = min(local_min, min_1)
        max_1 = max(local_max, max_1)

    if len(A) % 2:
        min_1 = min(A[-1], min_1)
        max_1 = max(A[-1], min_1)
    return (min_1, max_1)

A = [3, 2, 5, 1, 2, 4]
min_1, max_1 = sol(A)
print(min_1, max_1)