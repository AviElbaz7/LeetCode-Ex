class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        directions = [(1, 0), (-1, 0), (0,-1), (0, 1)]
        min_minutes = 0
        first_minute = True
        fresh = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append([r, c])
                elif grid[r][c] == 1:
                    fresh += 1
        
        while q:
            n = len(q)
            for i in range(n):
                x, y = q.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                        if first_minute:
                            min_minutes += 1
                            first_minute = False
                        fresh -= 1
                        q.append([nx, ny])
                        grid[nx][ny] = 2
            first_minute = True
        
        # for r in range(rows):
        #     for c in range(cols):
        #         if grid[r][c] == 1:
        #             return -1
        
        return min_minutes if fresh == 0 else -1