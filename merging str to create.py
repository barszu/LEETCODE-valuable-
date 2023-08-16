"""
LCS PROBLEM
whether can I make s3 mixing s1 with s2 (save letters order)
"""
# f(i,j) - LCS

class Solution:
    # czy da sie zrobic s3 mieszajac s1 z s2 (nie zmieniajac kolejnosci miejsc)
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3): return False
        dp = [[None for j in range(len(s2)+1)] for i in range(len(s1)+1)] #[s1][s2]
        dp[len(s1)][len(s2)] = True

        for i in range(len(s1),-1,-1):
            for j in range(len(s2),-1,-1):
                if dp[i][j] != None: continue
                take_s1 , take_s2 = False , False

                if i+1 <= len(s1) and s3[i+j] == s1[i]:
                    take_s1 = dp[i+1][j]

                if j+1 <= len(s2) and s3[i+j] == s2[j]:
                    take_s2 = dp[i][j+1]

                dp[i][j] = take_s1 or take_s2
        
        return dp[0][0]