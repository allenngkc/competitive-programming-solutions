class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        # hs = {i: 0 for i in range(n)}
        graph, n = {}, len(edges)
        for i in range(n):
            a, b = edges[i]
            if a not in graph: graph[a] = []
            if b not in graph: graph[b] = []
            graph[a].append((b, -succProb[i]))
            graph[b].append((a, -succProb[i]))
        
        q, v = [(-1, start_node)], set()
        while q:
            ev, node = heapq.heappop(q)
            if node == end_node: return ev*-1
            if node not in graph: continue
            v.add(node)
            for d in graph[node]:  
                if d[0] in v: continue
                heapq.heappush(q, (d[1]*ev*-1, d[0]))
        return 0