class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n, vis = len(isConnected), set()
        m, r = len(isConnected[0]), 0

        def bfs(node):
            if node in vis: return
            vis.add(node)
            for i in range(m):
                if i == node: continue
                if isConnected[node][i] == 1:
                    bfs(i)

        for i in range(n):
            if i not in vis: r += 1
            bfs(i)
        return r
        
