class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        n, mr = len(nums), [None] * len(nums)
        mr[-1] = nums[-1]
        for i in range(n-2, -1,-1):
            mr[i] = max(mr[i+1], nums[i])

        l, res = 0, 0
        for r in range(1, n):
            while l < r and nums[l] > mr[r]:
                l += 1
            res = max(res, r-l)
        return res




