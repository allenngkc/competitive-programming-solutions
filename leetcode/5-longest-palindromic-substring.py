class Solution:
    def longestPalindrome(self, s: str) -> str:
        res, it, jt, n = 1, 0, 0, len(s)
        dp = [[0]* n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
            if i+1 < n and s[i] == s[i+1]:
                dp[i][i+1] = 2
                res, it, jt = 2, i, i+1

        for j in range(2, n):
            for i in range(j-2+1):
                if dp[i+1][j-1] != 0 and s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1]+2
                else:
                    dp[i][j] = 0
                if dp[i][j] > res:
                    res, it, jt = dp[i][j], i, j

        return s[it:jt+1]
