class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        DIR = [(-1,0), (0,-1)]   # up, left
        DIR2 = [(1,0), (0,1)]    # down, right
        n, m = len(mat), len(mat[0])

        # We looked into the future but we shouldn't, only look at prev

        for i in range(n):
            for j in range(m):
                if mat[i][j] != 0:
                    mat[i][j] = float('inf')

        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    continue
                curr = mat[i][j]
                for x, y in DIR:
                    ni, nj = i + x, j + y
                    if 0 <= ni < n and 0 <= nj < m:
                        curr = min(curr, mat[ni][nj] + 1)
                mat[i][j] = curr

        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if mat[i][j] == 0:
                    continue
                curr = mat[i][j]
                for x, y in DIR2:
                    ni, nj = i + x, j + y
                    if 0 <= ni < n and 0 <= nj < m:
                        curr = min(curr, mat[ni][nj] + 1)
                mat[i][j] = curr

        return mat