class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        dd = dominoes
        # [RRRR]
        # [0 0000 0]
        n = len(dominoes)
        res = [0] * n

        j = 0
        for i in range(n):
            if dd[i] == 'R': j = n
            elif dd[i] == 'L': j = 0
            else: j = max(0, j-1)

            res[i] += j

        j = 0
        for i in range(n-1, -1, -1):
            if dd[i] == 'L': j = -n
            elif dd[i] == 'R': j = 0
            else: j = min(j+1, 0)
            
            res[i] += j
        
        ress = ""
        for i in res:
            if i > 0: ress += 'R'
            elif i < 0: ress += 'L'
            else: ress += '.'
        return ress

            