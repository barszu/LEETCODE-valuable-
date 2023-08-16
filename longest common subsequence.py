"""
LCS beetwen 2 str -> same letters in order
"""
# f(i,j) = LCS beetwen s[i] and t[i]

class Solution:
    # subsequences must be the same in both str's
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        A , B = text1 , text2
        a , b = len(A) , len(B)
        # b - wiersze , a- kolumny
        dp = [[None for i in range(a+1)] for j in range(b+1) ]
        for i in range(a+1):
            dp[b][i] = 0
        for i in range(b+1):
            dp[i][a] = 0


        for i in range(b-1,-1,-1):
            for j in range(a-1,-1,-1):
                if A[j] == B[i]: 
                    dp[i][j] = 1 + dp[i+1][j+1] #if in bound
                else:
                    dp[i][j] = max( dp[i+1][j] , dp[i][j+1] )
        
        return dp[0][0]