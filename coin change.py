"""
UNBOUND KNAPSACK PROBLEM

How many unique ways to add coins to sum
coins = [1,2,5] -> take 1 or take [2,5] -> take 2 or take [5] -> take 5 
"""
# f(coin)(amount) - how many unique ways to create amount using that coin now

# if I use 2 now I can't use 1 , I can use 2 or >

def change(amount: int, coins: list[int]) -> int:
        dp = [[0 for c in range(len(coins))] for i in range(amount+1)] # [sum][coin_idx]
        for c in range(len(coins)): dp[0][c] = 1

        for c_idx in range(len(coins)-1 , -1 ,-1):
            for i in range(1,amount+1):
                # coins[1,2,5]
                take_c = dp[i-coins[c_idx]][c_idx] if i-coins[c_idx] >= 0 else 0
                #take 1 coin -> problem reduced to lesser sum - coin taken
                take_r = dp[i][c_idx+1] if c_idx+1 < len(coins) else 0
                # or not take 1 take the rest -> [2,5] - coin not taken next atend
                dp[i][c_idx] = take_c + take_r
        
        return dp[amount][0]

print(change(5,[1,2,5]))