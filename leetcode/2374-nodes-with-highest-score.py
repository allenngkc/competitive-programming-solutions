class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        hm = [0] * len(edges)
        for i in range(len(edges)):
            hm[edges[i]] += i
        t = max(hm)
        for i in range(len(edges)):
            if t == hm[i]: return i