class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        total_max, curr_max = 0, 0
        q = deque()
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        rows, cols = len(grid), len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    grid[r][c] = 0
                    curr_max = 1
                    q.append([r, c])
                    while q:
                        i, j = q.popleft()
                        for dr, dc in directions:
                            nr, nc = i + dr, j + dc
                            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                                q.append([nr, nc])
                                grid[nr][nc] = 0
                                curr_max += 1
                    total_max = max(total_max, curr_max)
        return total_max

