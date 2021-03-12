'''
Design an efficient algo for sorting a k-increasing-decreasing array
'''
def sol(A):
    sorted_subarray = []
    increasing, decreasing = [0, 1]
    subarray_type = increasing
    start_idx = 0
    for i in range(1, len(A) + 1):
        if(i == len(A) or (A[i - 1] < A[i] and subarray_type == decreasing) or (A[i - 1] >= A[i] and subarray_type == increasing)):
            sorted_subarray.append(A[start_idx:i] if subarray_type == increasing else A[i - 1:start_idx - 1:-1])
            start_idx = i
            subarray_type = decreasing if subarray_type == increasing else decreasing

    return merge_sorted_array(sorted_subarray) # from 10.1