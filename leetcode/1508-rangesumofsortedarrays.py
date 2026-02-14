class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        res, n = [], len(nums)

        for i in range(n):
            for j in range(i, n):
                res.append(sum(nums[i:j+1]))
        res.sort()

        return sum(res[left-1:right]) % (10**9+7)