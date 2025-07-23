class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        """
        [14, 3, 19, 3], bricks = 17, ladders = 0
        """

        n, eddie = len(heights), []
        for i in range(1, n):
            if heights[i] <= heights[i-1]: continue

            diff = heights[i]-heights[i-1]
            if ladders > 0:
                heapq.heappush(eddie, diff)
                ladders -= 1
            else:
                if len(eddie) == 0: heapq.heappush(eddie, float('inf'))
                if bricks < min(eddie[0], diff): return i-1

                if diff < eddie[0]:
                    bricks -= diff
                else:
                    curr = heapq.heappop(eddie)
                    bricks -= curr
                    heapq.heappush(eddie, diff)
        return n-1
                    

