from typing import *
'''
    Given an N x N 2D array, return the spiral ordering of the array

'''

def EPI_sol(grid: List[List[int]]) -> List[int]:
    shift = ((0, 1), (1, 0), (0, -1), (-1, 0))
    direction = x = y = 0
    sprial_ordering = []

    for _ in range(len(grid) ** 2):
        sprial_ordering.append(grid[x][y])
        grid[x][y] = 0 # mark as visited
        next_x, next_y = x + shift[direction][0], y + shift[direction][1]
        if(next_x not in range(len(grid))
            or next_y not in range(len(grid))
            or grid[next_x][next_y] == 0):
            
            direction = (direction + 1) % 4
            next_x, next_y = x + shift[direction][0], y + shift[direction][1]
            
        x, y = next_x, next_y
    return sprial_ordering
A = [
        [5, 3, 4, 6],
        [6, 7, 2, 1],
        [1, 9, 8, 3],
        [8, 5, 9, 7],
    ]
res = EPI_sol(A)
print(res)