class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        res, heap, v = [], [(nums1[0]+nums2[0], 0, 0)], set()
        while k:
            tot, i, j = heapq.heappop(heap)
            if (i,j) in v: continue
            v.add((i,j))
            res.append([nums1[i], nums2[j]])

            if i+1 < len(nums1):
                heapq.heappush(heap, (nums1[i+1]+nums2[j], i+1,j))
            if j+1 < len(nums2):
                heapq.heappush(heap, (nums1[i]+nums2[j+1], i,j+1))
            k -= 1
        return res

