class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        heap = [-a,-b,-c]
        res = 0
        while heap:
            c1, c2 = -heapq.heappop(heap), -heapq.heappop(heap)
            if c1 == 0 or c2 == 0: return res
            heapq.heappush(heap, -(c1-1))
            heapq.heappush(heap, -(c2-1))
            res += 1
        return res


        