from typing import *
import math
'''
Sudoku Checker, Given N x N grid, Every row, Every Column, 
Every sqrt(N) x sqrt(N) subarray contains no duplicate and only contains 1~N, (0 indicate empty slot)

'''
#we need to check nine row constraints, nine column contrainsts , and nin sub-grid
# it's convenient to use bit array to test for constraint violations
def is_valid_soduku(grid: List[List[int]]) -> bool:
    def has_duplicate(block):
        #不考虑还未填入的地方
        block = list(filter(lambda a: a != 0, block))
        print(block)
        return len(block) != len(set(block))
    
    n = len(grid)
    # check every row and column
    for i in range(n):
        if has_duplicate([grid[i][j] for j in range(n)]) or has_duplicate([grid[j][i] for j in range(n)]):
            return False
    #Check each region
    region_size = int(math.sqrt(n))
    '''
        ---------------------
        |   1  |   2  |   3  |
        |______|______|______|
        |   4  |   5  |   6  |
        |______|______|______|
        |  7   |   8  |   9  |    
        |      |      |      |
        |--------------------|
    '''
    #一共有 sqrt（N）x sqrt(N)个zone， 每个zone的长宽都为sqrt(N)
    #我们遍历的时候需要跳跃到每个zone的开始， 所以是sqrt（N） x i，（也可以看作是多个sqrt（N）累加）
    for i in range(region_size):
        for j in range(region_size):
            if(has_duplicate([
                grid[a][b]  #grabbing each of the element in grid, put it into a list comprehension
                for a in range(region_size * i, region_size * (i + 1))
                for b in range(region_size * j, region_size * (j + 1))

                ])):
                return False
    return True



    

A = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 3],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9]
    ]
print(is_valid_soduku(A))

