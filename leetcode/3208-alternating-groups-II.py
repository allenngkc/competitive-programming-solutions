class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        for c in colors[:k-1]: colors.append(c)
        l, ans = 0, 0
        for r in range(1, len(colors)):
            if colors[r] == colors[r-1]: l = r
            if r-l+1 == k:
                ans += 1
                l += 1
        return ans