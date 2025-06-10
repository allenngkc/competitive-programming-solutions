class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        diff = [0] * (n+1)
        for s, e, v in bookings:
            diff[s-1] += v
            diff[e] -= v
        arr, cur = [], 0
        for i in range(n):
            cur += diff[i]
            arr.append(cur)
        return arr