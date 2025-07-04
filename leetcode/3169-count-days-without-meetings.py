class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.append([0,0])
        meetings.append([days+1,days+1])
        meetings.sort()
        res, pe = 0, 0
        for i in range(1, len(meetings)):
            s, e = meetings[i][0], meetings[i][1]
            if pe < s:
                res += (s-pe-1)
            pe = max(pe, e)
        return res