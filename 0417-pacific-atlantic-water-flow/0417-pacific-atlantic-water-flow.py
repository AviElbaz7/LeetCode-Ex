class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []

        pacific, atlantic = [], []
        rows, cols = len(heights), len(heights[0])

        for r in range(rows):
            pacific.append((r, 0))
            atlantic.append((r, cols - 1))
        for c in range(cols):
            pacific.append((0, c))
            atlantic.append((rows - 1, c))
        
        def bfs(starting_points):
            q = deque(starting_points)
            visited = set(starting_points)
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            while q:
                for i in range(len(q)):
                    r, c = q.popleft()
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < rows and 0 <= nc < cols and heights[nr][nc] >= heights[r][c] and (nr, nc) not in visited:
                            q.append([nr, nc])
                            visited.add((nr, nc))
            return visited
        
        to_pacific = bfs(pacific)
        to_atlantic = bfs(atlantic)

        return list(to_pacific & to_atlantic)