class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n, m = len(board), len(board[0])
        q = deque()
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for i in range(n):
            if board[i][0] == 'O':
                board[i][0] = 'S'
                q.append([i, 0])
            if board[i][m-1] == 'O':
                board[i][m-1] = 'S'
                q.append([i, m-1])
        
        for i in range(m):
            if board[0][i] == 'O':
                board[0][i] = 'S'
                q.append([0, i])
            if board[n-1][i] == 'O':
                board[n-1][i] = 'S'
                q.append([n-1, i])
        
        while q:
            for i in range(len(q)):
                x, y = q.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 'O':
                        board[nx][ny] = 'S'
                        q.append([nx, ny])
        for i in range(n):
            for j in range(m):
                if board[i][j] == 'O':
                    board[i][j] = 'X'

                if board[i][j] == 'S':
                    board[i][j] = 'O'

        