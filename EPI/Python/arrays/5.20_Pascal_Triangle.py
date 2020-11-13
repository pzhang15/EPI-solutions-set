from typing import *
'''
Pascal Triangle Wiki: https://en.wikipedia.org/wiki/Pascal%27s_triangle
每一行会比上一行多一个element， 每个element等于上面一行的相邻两个的和

Write a program which takes as input a nonnegative integer n
returns the first n rows of Pascal's triangle

'''
#如果想要把这个变成三角形很难， 不如把所有的数字对到
def epi_sol(n: int) -> List[List[int]]:
    #把正方形左下角全部设置成1（每一行比上一行多一个，之后会覆盖掉不需要的1）
    result = [[1] * (i + 1) for i in range(n)]
    for i in range(n):
        for j in range(1, i):
            result[i][j] = result[i - 1][j - 1] + result[i - 1][j]
    return result

result = epi_sol(5)
for row in result:
    print(row)