"""
DP I WITH CHANGING ONE DECISION (buy/sell)

max income from buying and selling (coldown always posible , buy -> sell ), after sell 1 day cooldown
"""
# f(i)(buy/sell) - max income from that day buying/selling

def maxProfit(prices: list[int]) -> int:
    # brute-force DFS with cashing
    n = len(prices)
    if n==1: return 0
    if n==2:
        if prices[0] < prices[1]:
            return prices[1]-prices[0]
        else: return 0
    
    dp_sell = [None] * n
    dp_buy = [None] * n


    def dfs(i,buying):
        nonlocal n
        if i>= n: return 0
        if buying and dp_buy[i] != None: return dp_buy[i]  #already cashed
        if not buying and dp_sell[i] != None: return dp_sell[i]

        if buying:
            buy = -prices[i] + dfs(i+1,False)
            cooldown = dfs(i+1,True)
            dp_buy[i] = max(cooldown , buy)
            return dp_buy[i]
        else:
            sell = prices[i] + dfs(i+2,True)
            cooldown = dfs(i+1,False)
            dp_sell[i] = max(sell,cooldown)
            return dp_sell[i]
    
    return dfs(0,True)

print(maxProfit([1,2,3,0,2]))