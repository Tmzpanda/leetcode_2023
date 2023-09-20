"""
rates = [2, 4, 1, 5, 10, 6]
strategy = [-1, 1, 0, 1, -1, 0] 
k = 4

"""
# greedy
def solution(rates, strategy, k):
    n = len(rates)
    max_profit = sum(rate * s for rate, s in zip(rates, strategy)) 

    for i in range(n-k+1):
        new_strategy = strategy[:i] + [0]*(k//2)+[1]*(k//2) + strategy[i+k:]   # boundary
        profit = sum(rate * s for rate, s in zip(rates, new_strategy))
        max_profit = max(max_profit, profit)

    return max_profit

