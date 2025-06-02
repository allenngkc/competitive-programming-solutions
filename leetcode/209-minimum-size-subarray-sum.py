class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target: return 0
        n, res, l, cs = len(nums), len(nums), 0, 0
        for r in range(n):
            cs += nums[r]
            if cs >= target:
                while l <= r and cs >= target:
                    res = min(res, r-l+1)
                    cs -= nums[l]
                    l += 1                
        return res