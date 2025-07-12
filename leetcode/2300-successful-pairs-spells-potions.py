class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        n,m = len(spells), len(potions)
        res, st = [0] * n, [(s,i) for i,s in enumerate(spells)]
        st.sort()
        R = m 
        for i in range(n):
            l = 0
            while l < R:
                mid = (l + R) // 2
                if (potions[mid] * st[i][0]) >= success:
                    R = mid
                else:
                    l = mid+1
            res[st[i][1]] = m-R
        return res
    