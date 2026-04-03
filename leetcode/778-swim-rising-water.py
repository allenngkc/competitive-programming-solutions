class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        DIR = [(1,0), (0,1), (-1,0), (0,-1)]
        visited = set()
        n = len(grid)
        q = [(grid[0][0], 0, 0)]
        while q:
            d, x, y = heapq.heappop(q)
            if x == n-1 and y == n-1: return d
            if (x,y) in visited: continue
            visited.add((x,y))
            for xi, yj in DIR:
                nx, ny = x+xi, y+yj
                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    continue
                if d >= grid[nx][ny]:
                    heapq.heappush(q, (d, nx, ny))
                else:
                    heapq.heappush(q, (grid[nx][ny], nx, ny))
        return -1

