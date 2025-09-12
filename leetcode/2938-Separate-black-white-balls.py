class Solution:
    def minimumSteps(self, s: str) -> int:
        """
        0000111000
        """
        arr = []
        for i in s: arr.append(int(i))

        r, n, ans = len(s)-1, len(s), 0
        for l in range(0, n):
            if arr[l] == 0: continue

            while r >= 0 and arr[r] == 1:
                r -= 1
            if l >= r: return ans
            arr[r], arr[l] = 1, 0
            ans += r-l
        return ans