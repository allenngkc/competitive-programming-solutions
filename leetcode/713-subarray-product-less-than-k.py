class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k == 0 or k == 1: return 0
        res, prod, l = 0, 1, 0
        for r in range(len(nums)):
            prod *= nums[r]
            while l <= r and prod >= k:
                prod //= nums[l]
                l += 1
            res += (r-l+1)
        return res