'''
  0    1   2   3    4    5    6    7    8
[-14, -10, 2, 108, 108, 243, 285, 285, 401]
k = 106, return: 3

k = 286 return 6

LC 278 First Bad Version
'''
def sol(A, k):
    l, r = 0, len(A)
    while l < r:
        mid = (l + r) //2
        if A[mid] <= k:
            left  = mid + 1
        else:
            right = mid
    return right
        