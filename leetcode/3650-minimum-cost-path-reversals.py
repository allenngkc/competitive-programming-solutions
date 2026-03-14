class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        dist = [10e9] * n
        visited = [False] * n
        dist[0], g = 0, {}

        for i, j, w in edges:
            if i not in g: g[i] = set()
            if j not in g: g[j] = set()
            g[i].add((j,w))
            g[j].add((i,2*w))

        pq = [(0,0)]
        while pq:
            cost, node = heapq.heappop(pq)
            if dist[node] < cost or visited[node]: continue
            if node == n-1: return cost
            dist[node] = cost
            visited[node] = True
            if node not in g: continue
            for j, w in g[node]:
                if dist[j] < cost+w: continue
                heapq.heappush(pq, (cost+w, j))
        return dist[n-1] if dist[n-1] != 10e9 else -1


