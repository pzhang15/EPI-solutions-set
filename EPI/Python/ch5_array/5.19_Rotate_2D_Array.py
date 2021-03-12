from typing import *
'''
Given a N x N 2D array, and rotate the aray by 90 degree clock wise

'''

def EPI_sol(matrix: List[List[int]]) -> None:
    n = len(matrix)
    for layer in range(n//2):
        first = layer # layer is also how deep are we into the matrix
        last = n - 1 - layer 
        for i in range(first, last):
            #we move it one by one 
            #offset indicate which one did is i points to relative to the layer
            offset = i - first 
            #save top
            top = matrix[first][i]
            # top = left
            matrix[first][i] = matrix[la st - offset][first]
            # left = bottom
            matrix[last - offset][first] = matrix[last][last - offset]
            # bottom = right
            matrix[last][last - offset] = matrix[i][last]
            # right = top
            matrix[i][last] = top
    

A = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
    ]

EPI_sol(A)
print(A)