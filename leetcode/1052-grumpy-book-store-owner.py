class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        l, r, n, curr = 0, minutes-1, len(customers), 0
        for i in range(n):
            if l <= i and i <= r: curr += customers[i]
            else: curr += (customers[i] if grumpy[i] == 0 else 0)
        ans = curr
        while r < n-1:
            curr -= (customers[l] if grumpy[l] == 1 else 0)
            l, r = l+1, r+1
            curr += (customers[r] if grumpy[r] == 1 else 0)
            ans = max(ans, curr)
        return ans
        """
                l    r 
            C = [1,0,1,2,1,1,7,5]
            G = [0,1,0,1,0,1,0,1]
            M = 3
            
            Core observations:
            1. Two pointer, l and r, both increment by one each iteration
            2. l shift -> if prev = 1 then we decrement
            3. r shift -> if next = 1 then we increment
            4. have the inital state precomputed

            Coding:
            1. Precomputation of init window -> Precomputation done
            2. Loop the window
        """