'''
given input array of characters, replace each 'a' with 2 'd's and delete each 'b'
[a, c, d, b, b, c, a] -> [d, d, c, d, c, d, d]

'''

def replace_and_remove(A, n):
    a_cnt = 0
    #错误1. 没有把 b 之后的字母向前移动， 而是流出空缺， 这样子从后面开始写入就会有错位
    for i in range(n):
        if A[i] == 'a':
            a_cnt += 1
        elif A[i] == 'b':
            A[i] = ''
            a_cnt -= 1
    j = len(A) - 1
    i = (n - 1) + a_cnt
    print(A)
    while(i >= 0):
        print(i, j)
        if A[j] == 'a':
            A[i] = 'd'
            A[i - 1] = 'd'
            i -= 2
            j -= 1
        else:
            A[j] = A[i]
            i -= 1
            j -= 1
    return A

def second_attempt(A, n):
    a_cnt = 0
    write_idx = 0
    for i in range(n):
        if A[i] != 'b':
            A[write_idx] = A[i]
            write_idx += 1
        if A[i] == 'a':
            a_cnt += 1
    # backward write
    curr_idx = write_idx - 1
    write_idx += a_cnt - 1
    print(A)
    while(curr_idx >= 0):
        print(curr_idx, write_idx)
        if A[curr_idx] == 'a':
            A[write_idx] = 'd'
            A[write_idx - 1] = 'd'
            write_idx -= 2
        else:
            A[write_idx] = A[curr_idx]
            write_idx -= 1
        curr_idx -= 1
    return A
A = ['a', 'c', 'd', 'b', 'b', 'c', 'a']

res = second_attempt(A, len(A))
print(res)

    
