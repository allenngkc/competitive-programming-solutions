class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        MOD = (10**9) + 7
        nums.sort()
        n = len(nums)
        r, ans = n-1, 0
        for l in range(n):
            while r >= 0 and nums[l]+nums[r] > target:
                r -= 1
            if r >= l:
                ans += 2**(r-l)
        return ans % MOD