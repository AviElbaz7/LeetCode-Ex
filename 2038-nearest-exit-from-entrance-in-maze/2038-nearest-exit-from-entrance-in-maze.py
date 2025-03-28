class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        q = deque()
        rows, cols = len(maze), len(maze[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        q.append(entrance)
        minimum_steps = 1
        visited = set()
        visited.add(tuple(entrance))

        while q:
            n = len(q)
            for i in range(n):
                x, y = q.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] == "." and (nx, ny) not in visited:
                        q.append([nx, ny])
                        visited.add((nx, ny))
                        if nx == (rows - 1) or ny == (cols - 1) or nx == 0 or ny == 0:
                            return minimum_steps
            minimum_steps += 1
        return -1