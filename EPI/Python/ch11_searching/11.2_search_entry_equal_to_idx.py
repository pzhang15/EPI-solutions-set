'''

take an sorted aray of distinct integer, and return an index such that the element at i is equal to i
A = [-2, 0, 2, 3, 6, 7, 9]
return 2, or 3 would be correct

'''
def sol(A):
    l, r = 0, len(A)
    while l < r:
        mid = (l + r)//2
        diff = A[mid] - mid
        if diff == 0:
            return mid
        elif diff < 0:
            l = mid + 1
        else:
            r = mid
    return -1