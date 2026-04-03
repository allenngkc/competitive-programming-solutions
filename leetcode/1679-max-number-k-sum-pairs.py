class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        n, res = len(nums), 0
        nums.sort()
        l, r = 0, n-1
        while l < r:
            su = nums[l] + nums[r]
            if su > k:
                r -= 1
            elif su < k:
                l += 1
            else: 
                res += 1
                l += 1
                r -= 1
        return res
