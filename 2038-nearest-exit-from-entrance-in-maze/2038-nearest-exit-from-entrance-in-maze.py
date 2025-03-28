class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        q = deque()
        rows, cols = len(maze), len(maze[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        q.append(entrance)
        minimum_steps = 0
        visited = set()
        visited.add(tuple(entrance))

        while q:
            n = len(q)
            for i in range(n):
                x, y = q.popleft()
                if (x == (rows - 1) or y == (cols - 1) or x == 0 or y == 0) and [x, y] != entrance:
                    return minimum_steps
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] == "." and (nx, ny) not in visited:
                        q.append([nx, ny])
                        visited.add((nx, ny))
            minimum_steps += 1
        return -1