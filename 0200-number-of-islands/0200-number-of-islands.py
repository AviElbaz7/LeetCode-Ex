class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        total = 0
        n, m = len(grid), len(grid[0])
        q = deque()
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    total += 1
                    q.append([i, j])
                    grid[i][j] = "0"
                    while q:
                        xx, yy = q.popleft()
                        for x, y in directions:
                            nx, ny = xx + x, yy + y
                            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == "1":
                                grid[nx][ny] = "0"
                                q.append([nx, ny])
        return total

