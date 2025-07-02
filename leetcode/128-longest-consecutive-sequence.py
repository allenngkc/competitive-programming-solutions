class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset, res = set(nums), 0
        for i in numset:
            if i - 1 not in numset:
                y = i + 1
                while y in numset:
                    y += 1
                res = max(res, y-i)
        return res