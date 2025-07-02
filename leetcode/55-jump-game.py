class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp, s = [0]*n, 1
        dp[n-1] = 1
        for i in range(n-2, -1, -1):
            if nums[i] >= s:
                dp[i], s = 1, 1
            else:
                s += 1
                continue
        return True if dp[0] == 1 else False
