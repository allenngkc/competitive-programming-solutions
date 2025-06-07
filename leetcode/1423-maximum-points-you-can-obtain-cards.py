class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        l, r, n, ans = 0, 0, len(cardPoints), 0
        pre, post, ps, pos = [0]*(k+1), [0]*(k+1), 0, 0
        for i in range(1, k+1):
            ps, pos = ps + cardPoints[i-1], pos + cardPoints[n-i]
            pre[i], post[i] = ps, pos 
        while k:
            if post[k+r]-post[r] > pre[k+l]-pre[l]:
                ans += cardPoints[n-r-1]
                r += 1
            else:
                ans += cardPoints[l]
                l += 1
            k -= 1
        return ans

