'''
A = ["ALl", "Work", "and", "no","play","makes","for","no","work","no","fun", "and", "no", "result"]
The nearest entry is second and third no, with differnet of 1

'''
def sol(A):
    dic = {}
    min_diff = float('inf')
    for i in range(len(A)):
        s = A[i]
        if s in dic:
            min_dff = min(min_dff, i - dic[s])
        dic[s] = i
    return min_diff
    