class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = len(nums)
        if k == 1: return 1
        for l in range(len(nums)-1):
            r = l+1
            if nums[l] != nums[r]: continue
            while r < k and nums[l] == nums[r]:
                r += 1
            c, i = 2, r
            while i < k:
                nums[l+c] = nums[i]
                i, c = i+1, c+1
            k = min(k - (r-l-2), k)
        return k