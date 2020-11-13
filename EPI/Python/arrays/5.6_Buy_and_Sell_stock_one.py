from typing import *

'''Write a program that computes the maximum profit that can be made by buying and selling a share at most twice.
The second buy must be made on another date after the first sale.

Hint: What do you need to know about the first i elements when processing the (i + l)th element?
'''

def my_sol(A:List) -> int:
    maxprofit, n = 0, len(A)
    for i in range(n):
        for j in range(i + 1, n):
            #buy at i, sell at j
            maxprofit = max(maxprofit, A[j] - A[i])
    return maxprofit

    
#O(N) time and O(1) space, EPI_sol其实是由上面的brute force solution衍生出来的
def EPI_sol(A: List[float]) -> float:
    min_price, max_profit = float('inf'), 0.0
    for price in A:
        max_profit = max(max_profit, price - min_price)
        min_price = min(min_price, price)
    return max_profit

A = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]

res = EPI_sol(A)

print(res)
