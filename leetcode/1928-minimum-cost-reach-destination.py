class Solution:
    def minCost(self, maxTime: int, edges: List[List[int]], passingFees: List[int]) -> int:
        graph, n = {}, -1
        for i,j,t in edges:
            n = max(i, j, n)
            if i not in graph:
                graph[i] = []
            if j not in graph:
                graph[j] = []
            graph[i].append((j,t))
            graph[j].append((i,t))
        n += 1
        
        min_cost = [float('inf')] * n
        pq = [(0,passingFees[0],0)]
        while pq:
            t, c, node = heapq.heappop(pq)
            if min_cost[node] < c: continue
            min_cost[node] = min(c, min_cost[node])
            if node not in graph: continue
            for nei, nei_t in graph[node]:
                if nei_t + t <= maxTime and min_cost[nei] >= c + passingFees[nei]:
                    heapq.heappush(pq, (nei_t+t, c+passingFees[nei], nei))

        return min_cost[n-1] if min_cost[n-1] != float('inf') else -1
