class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        store, n, l, res = {}, len(fruits), 0, 0
        for r in range(n):
            curr = fruits[r]
            if curr not in store:
                store[curr] = 0
            store[curr] += 1
            while len(store) > 2:
                prev = fruits[l]
                store[prev] -= 1
                if store[prev] == 0:
                    del store[prev]
                l += 1
            res = max(res, r-l+1)
        return res
            
