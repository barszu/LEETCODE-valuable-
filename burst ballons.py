"""
REVERSE THING BRUTE FORCE WITH CACHE

max coins to optain, killing all ballons -> kill i-th -> all_coins += left(i) + i + right(i)
left right changing always after kill

solution -> take i-th as last

"""
# f(l,r) = max coins toget from ballons[l,r]

class Solution:
    # pop i-th el last having tab[l:r]
    # dp[l][r] - max num of coins from tab[l:r]
    def maxCoins(self, nums: list[int]) -> int:
        n = len(nums)
        dp = [[None for i in range(n)] for j in range(n)]

        def dfs(l,r):
            # nonlocal n
            if l > r: return 0 #nothing left to pop
            if dp[l][r]: return dp[l][r]
            # if l==r: #one ballon
            dp[l][r] = 0
            for i in range(l,r+1): #poping i-th as last
                left = nums[l-1] if l-1 >=0 else 1
                right = nums[r+1] if r+1 < n else 1

                coins =  left * nums[i] * right
                coins += dfs(l,i-1) + dfs(i+1 ,r)
                dp[l][r] = max(dp[l][r] , coins)
            return dp[l][r]
        
        return dfs(0,n-1)