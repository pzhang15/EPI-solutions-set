from typing import *

'''
Write a program that computes the maximum profit that can be made by buying and selling a share at most twice. 
The second buy must be made on another date after the first sale.
Hint: What do you need to know about the first i elements when processing the (i + l)th element?
'''

#O(n^4) brute force
def my_sol(A: List[float]) -> float:
    first_buy, first_sell = 0, 0
    second_buy, second_sell = 0, 0
    max_profit, n = 0, len(A)
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                for l in range(k + 1, n):
                    max_profit = max(max_profit, (A[j] - A[i]) + (A[l] - A[k]))
    return max_profit
#确认一个原则：如果我们在最低点买入，在最高点卖出，一定可以获得最大的profit
def EPI_sol(A: List[float]) -> float:
    #我们先找到从 [0 ～ j] 之间的最优解
    min_price = float('inf') #假设我们永远在最低点买入
    first_buy_sell_profit = [0] * len(A)
    max_profit = 0.0
    for i, price in enumerate(A):
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price) #额外单独维护max_profit，因为可能我们第二个forloop不会开始遍历
        first_buy_sell_profit[i] = max_profit
    print(first_buy_sell_profit)  

    #为什么要从右往左走？我们第一遍for loop从左往右走，是在遍历卖出的price，并且维护一个之前的min_price
    # 从右往左走是因为我们：
    # 1.对于第一次买入的最大prifit，也就是 first_buy_sell_profit[i]，我们只知道是在第i个price卖出，并不知道在哪个price卖出
    # 2.因为我们第二次一定要在i之后买入，我们从右往左是在遍历买入price，维护i之后的最大卖出price   
    # 这样子对于每个i，[0~i]的最大profit我们知道，[i~n]的最大profit我们也知道
    max_price = float('-inf') #假设我们在max_price的卖出

    for i, price in reversed(list(enumerate(A[1:], 1))):
        print(i)
        print(price, ' ', first_buy_sell_profit[i])
        max_price = max(max_price, price)
        max_profit = max(max_profit, first_buy_sell_profit[i] + (max_price - price))
    return max_profit
#1个原则要明白
#profit = (first_sell - first buy) + (second_sell - second_buy)
#       = ((first_sell - first buy) - second_buy) + second_sell
#       = (first_profit - second_buy) + second_sell
#       = second_cost + second_sell 
def one_pass_sol(A: List[float]) -> float:
    t1_cost, t2_cost = float('inf'), float('inf')
    t1_profit, t2_profit = 0, 0
    for price in prices:
        # the maximum profit if only one transaction is allowed
        t1_cost = min(t1_cost, price)
        t1_profit = max(t1_profit, price - t1_cost)
        # reinvest the gained profit in the second transaction
        t2_cost = min(t2_cost, price - t1_profit)
        t2_profit = max(t2_profit, price - t2_cost)

    return t2_profit    

A = [12, 11, 13, 9, 12, 8, 14, 13, 15]

res = EPI_sol(A)

print('res: ',res)