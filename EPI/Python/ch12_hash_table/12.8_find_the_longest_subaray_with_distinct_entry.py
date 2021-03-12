import collections
'''
A= [f, x, f, e, t, w, e, n, w, e,]
the longest subarray all elements are distinct is [s, f, e, t, w]

'''
def sol(A):
    most_recent_occruence = dict()
    dup_free_start_idx = 0
    res = 0
    for i, e in enumerate(A):
        if e in most_recent_occruence:
            dup_idx = most_recent_occruence[e]
            #重复元素的位置如果在我们的starting index之前，我们就可以忽略
            #如果在之后， 我们才需要重新调整我们的starting index
            if dup_idx >= dup_free_start_idx:
                res = max(res, i - dup_free_start_idx)
                dup_free_start_idx = dup_idx + 1

        most_recent_occruence[e] = i