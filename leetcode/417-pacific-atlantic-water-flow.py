class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n, m, pq, aq = len(heights), len(heights[0]), deque(), deque() # n = 3, m = 2
        DIR = [(0,1), (1,0), (-1,0), (0,-1)]
        def bfs(queue):
            v = set()
            while queue:
                i, j = queue.popleft()
                if (i,j) in v: continue
                v.add((i,j))
                for xi, xj in DIR:
                    if 0 <= i+xi < n and 0 <= j+xj < m and heights[i+xi][j+xj] >= heights[i][j]:
                        queue.append((i+xi, j+xj))
            return list(v)
        for i in range(m):
            pq.append((0, i))
            aq.append((n-1, i))
        for i in range(n):
            pq.append((i, 0))
            aq.append((i, m-1))
        pv, av, res = bfs(pq), bfs(aq), []        
        for i in pv:
            if i in av: 
                res.append(i)
        return res

        

                