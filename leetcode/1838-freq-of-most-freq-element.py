class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans, l, r, tot = 0, 0, 0, 0
        while r < len(nums):
            tot += nums[r]
            while nums[r] * (r-l+1) > tot+k:
                tot -= nums[l]
                l += 1
            ans = max(ans, r-l+1)
            r += 1
        return ans