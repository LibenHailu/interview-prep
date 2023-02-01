class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        dp =  [[mat[i][j] for j in range(len(mat[0]))] for i in range(len(mat))]
        for i in range(len(mat)):
            for j in range(1,len(mat[0])):
                dp[i][j] += dp[i][j-1]
        for i in range(1,len(mat)):
            for j in range(len(mat[0])):
                dp[i][j] += dp[i-1][j] 
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                r1, r2 = max(0, j-k), min(j+k, len(mat[0])-1)
                c1, c2 = max(0, i-k), min(i+k, len(mat)-1)
                dy = dp[c1-1][r2] if c1 > 0 else 0
                dx = dp[c2][r1-1] if r1 > 0 else 0
                dz = dp[c1-1][r1-1] if (r1 > 0 and c1 > 0) else 0
                mat[i][j] = dp[c2][r2] - dy - dx + dz
        return mat