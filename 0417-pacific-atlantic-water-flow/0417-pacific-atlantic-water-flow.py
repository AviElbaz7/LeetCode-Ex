class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific, atlantic = [], []
        q = deque()
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        rows, cols = len(heights), len(heights[0])

        for r in range(rows):
            pacific.append((r, 0))
            atlantic.append((r, cols - 1))
            
        for c in range(cols):
            pacific.append((0, c))
            atlantic.append((rows - 1, c))
        
        def bfs(starts):
            visited = set(starts)
            q = deque(starts)
            while q:
                for i in range(len(q)):
                    x, y = q.popleft()
                    for dx, dy in directions:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < rows and 0 <= ny < cols and heights[nx][ny] >= heights[x][y] and (nx, ny) not in visited:
                            q.append((nx, ny))
                            visited.add((nx, ny))
            return visited
            
        pacific_reach = bfs(pacific)
        atlantic_reach = bfs(atlantic)

        return list(pacific_reach & atlantic_reach)