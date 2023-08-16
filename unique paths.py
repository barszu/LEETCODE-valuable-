"""
CASHING BRUTE FORCE
How many ways to get from (0,0) to (n-1,n-1)
"""

class Solution:
    #bottom up DP
    def uniquePaths(self, m: int, n: int) -> int:
        ROWS , COLS = m , n
        # f(i,j) - how many ways to get from (i,j)->end
        DP = [[0 for i in range(COLS)] for j in range(ROWS)]
        #firstly cols from right to left , then go up
        DP[ROWS-1][COLS-1] = 1
        for i in range(ROWS-1 , -1 ,-1):
            for j in range(COLS-1 , -1 , -1):
                if (i,j) == (ROWS-1,COLS-1): continue
                down = DP[i+1][j] if i+1 < ROWS else 0
                right = DP[i][j+1] if j+1 < COLS else 0

                DP[i][j] = down + right
        return DP[0][0]

sol = Solution()
m = 3
n = 7
res = sol.uniquePaths(m,n)
print(res)