class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        tot = sum(matchsticks)
        if tot % 4 != 0: return False
        target = tot // 4
        used = [0] * len(matchsticks)
        def bt(curr, edge):
            if edge == 4: 
                return True
            prev = -1
            for i, s in enumerate(matchsticks):
                if used[i] or s > curr or s == prev: continue
                used[i] = 1
                # --- decide what the next curr (remaining length) should be ---
                if s == curr:
                    # This stick *exactly* completes the current side.
                    next_curr = target          # start fresh on the next side
                    next_edges = edge + 1      # we just completed one side
                else:
                    # The side isn’t finished yet; we still have space to fill.
                    next_curr = curr - s   # remaining length on *this* side
                    next_edges = edge         # still on the same side

                # --- recurse with those values ---
                if bt(next_curr, next_edges):
                    return True
                used[i] = 0    
                prev = s
                if curr == target or s == curr: break
            return False
        return bt(target, 0)