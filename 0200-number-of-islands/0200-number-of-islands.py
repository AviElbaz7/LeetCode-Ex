class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        total = 0
        rows, cols = len(grid), len(grid[0])

        def dfs(i, j):
            if i < 0 or i > rows - 1 or j < 0 or j > cols - 1 or grid[i][j] != "1":
                return
            
            grid[i][j] = "0"
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)
            return

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    total += 1
                    dfs(r, c)
        return total
                    