"""
CASHING BRUTE FORCE
longest increasing path in 2D matrix
"""
# f(i,j) = longest path len starting from (i,j)

def longestIncreasingPath(matrix: list[list[int]]) -> int:
        ROWS , COLS = len(matrix) , len(matrix[0])
        track_max = 1 #max len of increasing path
        cashe = [[None for j in range(COLS)] for i in range(ROWS)]

        def dfs(i,j): #i,j in bound
            nonlocal ROWS , COLS , track_max 
            if cashe[i][j] != None: return cashe[i][j] #already done
            val = matrix[i][j]
            left , right , up , down = 0 ,0 , 0, 0

            if j-1 >= 0 and matrix[i][j-1] > val: #left
                left = dfs(i,j-1)

            if j+1 < COLS and matrix[i][j+1] > val: #rigth
                right = dfs(i,j+1)

            if i-1 >= 0 and matrix[i-1][j] > val: #up
                up = dfs(i-1,j)

            if i+1 < ROWS and matrix[i+1][j] > val: #down
                down = dfs(i+1,j)
            
            cashe[i][j] = 1 + max(left,up,right,down)
            track_max = max(track_max , cashe[i][j])
            return cashe[i][j]
        
        for i in range(ROWS):
            for j in range(COLS):
                dfs(i,j)
        
        return track_max