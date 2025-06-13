class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        l, a, res = 0, -1, 0
        for r in range(len(nums)):
            if nums[r] > right:
                l = r+1
            elif nums[r] < left:
                if a-l+1 < 0: continue
                res += a-l+1
            else:
                res += r-l+1
                a = r
        return res