class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res, dist = sum(nums[:3]), abs(sum(nums[:3])-target)

        for i in range(len(nums)-2):
            l, r = i+1, len(nums)-1
            while l < r:
                c = nums[l]+nums[r]+nums[i]
                if abs(c-target) < dist:
                    dist = abs(c-target)
                    res = c
                if c < target: l += 1
                else: r -= 1
        return res