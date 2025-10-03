from typing import List
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
        def atMost(nums, target):
            n, curr, l, ans = len(nums), 0, 0, 0
            for r in range(n):
                curr += nums[r]
                while l <= r and curr > target:
                    curr -= nums[l]
                    l += 1 
                # window = [1,2,3] target: 20
                ans += r - l + 1
        
        return atMost(nums, goal) - atMost(nums, goal - 1)

        





