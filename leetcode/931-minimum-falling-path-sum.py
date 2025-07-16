class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        dp = [[float('')]*n for _ in range(n)]
        for i in range(n):
            dp[0][i] = matrix[0][i]

        for i in range(1, n):
            for j in range(0, n):
                for k in range(-1, 2):
                    if j+k < 0 or j+k >= n: continue
                    dp[i][j] = min(dp[i][j], dp[i-1][j+k]+matrix[i][j])
        return min(dp[n-1])


