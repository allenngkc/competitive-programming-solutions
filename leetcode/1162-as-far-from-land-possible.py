class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dp = [[float('inf')]*(n) for _ in range(n)]
        DIR = [(1,0), (-1,0), (0,1), (0,-1)]
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1: dp[i][j] = 0
        
        for i in range(0, n):
            for j in range(0, n):
                if grid[i][j] == 1: continue
                for d in DIR:
                    x, y = d[0], d[1]
                    if i+x < 0 or i+x >= n or j+y < 0 or j+y >=n: continue
                    dp[i][j] = min(dp[i+x][j+y]+1, dp[i][j])
        for i in range(n-1, -1, -1):
            for j in range(n-1, -1, -1):
                if grid[i][j] == 1: continue
                for d in DIR:
                    x, y = d[0], d[1]
                    if i+x < 0 or i+x >= n or j+y < 0 or j+y >=n: continue
                    dp[i][j] = min(dp[i+x][j+y]+1, dp[i][j])

        ans = 0
        for x in range(n):
            for y in range(n):
                if dp[x][y] > ans:
                    ans = dp[x][y]

        return ans if ans != 0 and ans != float('inf') else -1
        