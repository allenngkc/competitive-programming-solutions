class Solution:
    def balancedString(self, s: str) -> int:
        lmap = {"Q": 0, "W": 1, "E": 2, "R": 3}
        n = len(s)
        tar = n // 4
        cnt = [0] * 4
        
        for ch in s:
            cnt[lmap[ch]] += 1
        
        diff = [max(0, x - tar) for x in cnt]
        
        # already balanced
        if diff == [0, 0, 0, 0]:
            return 0
        
        def valid(window):
            for i in range(4):
                if window[i] < diff[i]:
                    return False
            return True
        
        l = 0
        window = [0] * 4
        res = n
        
        for r in range(n):
            idx = lmap[s[r]]
            if diff[idx] > 0:
                window[idx] += 1
            
            while valid(window) and l <= r:
                res = min(res, r - l + 1)
                left_idx = lmap[s[l]]
                if diff[left_idx] > 0:
                    window[left_idx] -= 1
                l += 1
        
        return res