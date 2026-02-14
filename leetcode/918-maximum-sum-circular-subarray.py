class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        cMax, cMin, n = nums[0], nums[0], len(nums)
        rMax, rMin = nums[0], nums[0]
        for i in range(1, n):
            cMax = max(cMax+nums[i], nums[i])
            cMin = min(cMin+nums[i], nums[i])
            rMax = max(rMax, cMax)
            rMin = min(rMin, cMin)

        if rMin == sum(nums): return rMax
        return max(rMax, sum(nums)-rMin)