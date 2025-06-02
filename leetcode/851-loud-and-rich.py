class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n, graph, up = len(quiet), {}, set()
        arr = []
        ans = [i for i in range(n)]
        for a, b in richer:
            if a not in graph:
                graph[a] = []
            graph[a].append(b)
        for i in range(n):
            arr.append((quiet[i], i))
        arr.sort()
        q = deque()
        for curr in arr:
            if curr[1] in up or curr[1] not in graph: continue
            for g in graph[curr[1]]:
                q.append((quiet[g], g))

            while q:
                quiett, node = q.popleft()
                if node in up: continue
                up.add(node)

                if curr[0] < quiett:
                    ans[node] = curr[1]
                    if node not in graph: continue
                    for nei in graph[node]:
                        q.append((quiet[nei], nei))
        return ans
            
