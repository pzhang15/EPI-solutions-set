from typing import *
#buy and sell stock twice
def EPI_sol(A: List[float]) -> float:
    min_price = float('inf')
    max_first_profit = float('-inf')
    first_buy_sell = [0] * len(A)
    for i in range(len(A)):
        max_first_profit = max(max_first_profit, A[i] - min_price)
        first_buy_sell[i] = max_first_profit
        min_price = min(min_price, A[i])
    
    
    max_price = float('-inf')
    max_second_profit = float('-inf')
    second_buy_sell = [0] * len(A)
    for i in reversed(range(len(A))):
        max_second_profit = max(max_second_profit, max_price - A[i])
        second_buy_sell[i] = max_second_profit
        max_price = max(max_price, A[i])
    
    max_total = float('-inf')
    for i in range(len(A)):
        max_total = max(max_total, first_buy_sell[i] + second_buy_sell[i])
    return max_total


         

A = [12, 11, 13, 9, 12, 8, 14, 13, 15]

res = EPI_sol(A)

print(res)
