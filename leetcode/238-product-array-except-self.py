class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
         i
        [1,2,3,4]

        prefix = [1,2,6,24]
        suffix = [24,24,12,4]
        """
        n, prefix, suffix, res = len(nums), [], [], []

        p, s = 1,1
        for i in range(n):
            p *= nums[i]
            s *= nums[n-i-1]
            prefix.append(p)
            suffix.append(s)
            

        for i in range(n):
            curr = 1
            # [1,2,3,4]
            if i-1 >= 0:
                curr *= prefix[i-1]
            if n-i-2 >= 0:
                curr *= suffix[n-i-2]
            res.append(curr)
        return res
