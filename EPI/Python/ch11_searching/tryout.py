'''
11.1
LC 287
'''

'''

take an sorted aray of distinct integer, and return an index such that the element 
at i is equal to i
A = [-2, 0, 2, 3, 6, 7, 9]
return 2, or 3 would be correct

'''

'''
compute both the min and max with less than 2N comparison
A = [3, 2, 5, 1, 2, 4]
return 1 and 5, which is min and max
'''

def sol(A):
    mini, maxi = A[0], A[1]
    for i in range(2, len(A), 2):
        if A[i] > A[i + 1]:
            mini = min (mini, A[i + 1])
            maxi = max(maxi, A[i])
        else:
            mini = min (mini, A[i])
            maxi = max(maxi, A[i + 1])
    if len(A) % 2:
        mini = min(A[-1], mini)
        maxi = max(A[-1], maxi)
    return (mini, maxi)
A = [3, 2, 5, 1, 2, 4]
min_1, max_1 = sol(A)
print(min_1, max_1)