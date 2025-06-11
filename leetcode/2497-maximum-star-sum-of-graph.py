class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        # For each node, heapify all their neibours, with limits of k, we greedily choose
        hm, n, ans = {}, len(vals), max(vals)
        for a, b in edges:
            if a not in hm: hm[a] = []
            if b not in hm: hm[b] = []
            hm[a].append(-vals[b])
            hm[b].append(-vals[a])
        for i in range(n):
            if i not in hm: continue
            heapq.heapify(hm[i])
            su = vals[i]
            for j in range(k):
                if len(hm[i]) == 0: break
                curr = -1 * heapq.heappop(hm[i])
                if curr < 0: break
                su += curr
            ans = max(ans, su)
        return ans