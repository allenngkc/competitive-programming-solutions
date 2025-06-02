class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        arr, res = [], 0
        for i in bank:
            n = 0
            for ch in i:
                if ch == '1': n += 1
            if n != 0: arr.append(n)
        for i in range(1, len(arr)):
            res += arr[i] * arr[i-1]
        return res