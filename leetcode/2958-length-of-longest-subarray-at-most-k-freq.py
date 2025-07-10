class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        """
            [1,2,1,2,1,2] k = 1
             
            length <= 10^5
            Max allowed: O(nlogn)

            Core Observation
            k = 2
            Data Type: Stores current state (Freq. of curr elements)
            -> Hashmap 1:3, 2:2
            [1,2,1,2,1,2]
               l     r
            
            [x,x,x,x,x,x,x,x,x]
                   l    r

            0. Initalize the variables, hashmap, l, r, res
            1. Loop the array with l, r pointer untill invaild state
            2. Shift L pointer untill valid state

            Note: r pointer will always increment forward 
        """
        
        l, res, freq = 0, 0, {}
        for r in range(len(nums)):
            if nums[r] not in freq:
                freq[nums[r]] = 0
            freq[nums[r]] += 1

            while freq[nums[r]] > k:
                freq[nums[l]] -= 1
                l += 1

            res = max(res, r-l+1)
        return res
            
        
            

