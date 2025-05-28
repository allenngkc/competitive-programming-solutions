class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n, m, q, v = len(board), len(board[0]), deque(), set()
        DIR = [(1,0), (0,1), (-1, 0), (0, -1)]
        for i in range(m):
            if board[0][i] == 'O': q.append((0,i))
            if board[n-1][i] == 'O': q.append((n-1, i))
        for i in range(n):
            if board[i][0] == 'O': q.append((i, 0))
            if board[i][m-1] == 'O': q.append((i, m-1))
        while q:
            i,j = q.popleft()
            if (i,j) in v: continue
            v.add((i,j))
            for xi, xj in DIR:
                if 0 <= i+xi < n and 0 <= j+xj < m and board[i+xi][j+xj] == 'O':
                    q.append((i+xi, j+xj)) 
        for i in range(n):
            for j in range(m):
                if board[i][j] == 'O' and (i,j) not in v:
                    board[i][j] = 'X'
        
    