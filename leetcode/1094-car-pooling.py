class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        """
        [+2, 0, +3, 0, -2, 0, -3]
        """
        diff, curr = [0]*1001, 0
        for i in trips:
            diff[i[1]] += i[0]
            diff[i[2]] 

        for i in diff:
            curr += i
            if curr > capacity: return False
        return True

        