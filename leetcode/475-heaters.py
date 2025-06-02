class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        def find_rad(a, b):
            return abs(a-b)
        heaters.sort()
        houses.sort()
        r, ans = 0, float('-inf')
        for l in range(len(houses)):
            while r < len(heaters)-1 and find_rad(heaters[r+1], houses[l]) <= find_rad(heaters[r], houses[l]):
                r += 1
            rad = find_rad(houses[l], heaters[r])
            ans = max(ans, rad)
        return ans