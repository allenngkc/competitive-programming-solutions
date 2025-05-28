class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[0] = dp[1] = 1
        for i in range(2, n+1):
            for j in range(i):
                l = max(0, j)
                r = i-j-1
                dp[i] += dp[l] * dp[r]
        return dp[n]