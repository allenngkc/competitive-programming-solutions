class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        ms, m, n = 0, len(matrix), len(matrix[0])
        
        dp = []
        for i in range(m):
            row = []
            for j in range(n):
                ms = max(ms, int(matrix[i][j]))
                row.append(int(matrix[i][j]))
            dp.append(row)
    
        for i in range(1, m):
            for j in range(1, n):
                if dp[i][j] == 0: continue
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
                ms = max(ms, dp[i][j])
        return ms ** 2