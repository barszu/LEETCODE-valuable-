"""
LONGEST COMMON SUBSEQUENCE PROBLEM
How many ways to create t from s (s->t)? (keep order of letters)
"""

def numDistinct(s: str, t: str) -> int:
        # cache[i][j] -> having s[i:n] , t[j:n]
        cache = [[None for j in range(len(t)+1)] for i in range(len(s)+1)]
        for i in range(len(s)+1): cache[i][len(t)] = 1
        for j in range(len(t)): cache[len(s)][j] = 0


        def dfs(i,j): #i-> s , j->t
            # if i > len(s) or j > len(t): return 0 #out of bound
            if cache[i][j] != None: return cache[i][j]
            eq_letters = 0
            if s[i] == t[j]: eq_letters = dfs(i+1,j+1)
            
            cache[i][j] = eq_letters + dfs(i+1,j)
            return cache[i][j]
        
        return dfs(0,0)

print(numDistinct("rabbbit", "rabbit"))