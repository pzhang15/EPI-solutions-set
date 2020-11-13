from typing import *


'''
In a particular board game, a player has to try to advance through a sequence of positions. 
Each position has a nonnegative integer associated with it, representing the maximum you can advance from that position in one move. 
You begin at the first position,and win by getting to the last position. For example,letA = {3,3,1,0,2,0,1} represent the board game, i.e., 
the ith entry in A is the maximum we can advance from i. 
Then the game can be won by the following sequence of advances through A: take 1 step from A[0] to A[1], then 3 steps from A[l] to A[4], then 2 steps from A[4] to A[6], which is the last position. Note that A[0] = 3 > 1, A[l] = 3 > 3, and A[4] = 2 > 2, so all moves are valid. 
If A instead was (3, 2, 0, 0, 2, 0,1), it would not possible to advance past position 3, so the game cannot be won.
Write a program which takes an array of n integers, 



where A[i] denotes the maximum you can advance from index i, 
and returns whether it is possible to advance to the last index starting from the beginning of the array.
'''


def epi_sol(A: List[int]) -> bool:
    furthest_so_far = 0
    i = 0
    last = len(A) - 1
    #第一个while loop condition是判断每个节点是否联通联通
    #有一点贪心的味道，我们想要走的越远越好，但是我们也会根据每个节点进行一次计算，所以不会落下任何最优解
    #可以尝试 [2 100 3 200 ...] 我们尝试先走100，这样子虽然会路过100，但是当i能走到200时（联通），我们也会计算200，所以永远是最长距离胜出
    #反证，如果最长距离无法到达最后，那么一定没有方法到达最后
    #这道题让你能走 小于等于 A[i]的节点，如果必须走A[i]，那么就需要dfs或者dp了
    
    #第二个condition注意是 < 因为如果能 == last就可以停止了，比last大也可以停止
    while(i <= furthest_so_far and furthest_so_far < last):
        print(i, " ", furthest_so_far)
        furthest_so_far = max(furthest_so_far, i + A[i])
        i += 1
    return furthest_so_far >= last

A = [2, 4, 1, 1, 0, 0, 0, 0, 2, 3]

res = epi_sol(A)

print(res)