class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        n, res = len(nums), float('-inf')
        r = n-1

        for l in range(n//2):
            res = max(res, nums[l]+nums[r])
            r -= 1
        return res
        