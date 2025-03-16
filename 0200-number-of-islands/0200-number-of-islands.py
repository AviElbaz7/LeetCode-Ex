class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        total = 0
        rows, cols = len(grid), len(grid[0])
        q = deque()
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    total += 1
                    q.append((r, c))
                    grid[r][c] = "0"
                    while q:
                        i, j = q.popleft()
                        for dr, dc in directions:
                            nr, nc = i + dr, j + dc
                            if 0 <= nr <= rows - 1 and 0 <= nc <= cols - 1 and grid[nr][nc] == "1":
                                grid[nr][nc] = "0"
                                q.append((nr, nc))
        return total