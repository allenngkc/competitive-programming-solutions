class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        heap, n, res = [], len(score), [""]*len(score)
        for i in range(n):
            heapq.heappush(heap, (-score[i], i)) 
        place = 1
        while heap:
            curr, index = heapq.heappop(heap)
            if place == 1:
                res[index] = "Gold Medal"
            elif place == 2:
                res[index] = "Silver Medal"
            elif place == 3:
                res[index] = "Bronze Medal"
            else:
                res[index] = str(place)
            place += 1

        return res
