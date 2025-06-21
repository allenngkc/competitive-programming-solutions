class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        q = deque([(0, k, src)])
        hmap, dist = {i : [] for i in range(n)}, {i : float('inf') for i in range(n)}
        for i in flights:
            if i[0] not in hmap:
                hmap[i[0]] = []
            hmap[i[0]].append((i[1], i[2]))
        while q:
            cw, t, curr = q.popleft()
            if curr == dst and dist[curr] > cw: dist[curr] = cw
            if t == -1: continue
            for path in hmap[curr]:
                if cw <= dist[curr]:
                    dist[curr] = min(dist[curr], cw)
                    q.append((cw+path[1], t-1, path[0]))
        return dist[dst] if dist[dst] != float('inf') else -1

