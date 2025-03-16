class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        q = deque()
        rows, cols = len(board), len(board[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for r in range(rows):
            for c in range(cols):
                if (r == rows - 1 or r == 0 or c == cols - 1 or c == 0) and board[r][c] == "O":
                    q.append([r, c])
                    board[r][c] = "S"
        
        while q:
            length = len(q)
            for i in range(length):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr <= rows - 1 and 0 <= nc <= cols - 1 and board[nr][nc] == "O":
                        board[nr][nc] = "S"
                        q.append([nr, nc])
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "S":
                    board[r][c] = "O"