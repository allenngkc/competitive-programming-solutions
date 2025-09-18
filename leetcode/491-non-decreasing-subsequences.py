class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        """
        [4, 3, 2, 1]
        """
        n = len(nums)
        visited = set()
        ans = []
        def bt(curr, i):
            nonlocal visited
            # print(i, ":", curr)
            if len(curr) >= 3:
                visited.add(tuple(curr))

            if i >= n: return
            
            # take
            if curr[-1] <= nums[i]:
                bt(curr + [nums[i]], i + 1)
            
            # not take
            bt(curr, i + 1)

        bt([-101], 0)

        for i in visited:
            ans.append(list(i)[1:])
        return ans