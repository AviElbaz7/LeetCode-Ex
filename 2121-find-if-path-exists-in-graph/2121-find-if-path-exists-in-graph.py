class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True
        connections = {i: [] for i in range(n)}
        for edge in edges:
            connections[edge[0]].append(edge[1])
            connections[edge[1]].append(edge[0])

        if source not in connections:
            return False
        queue = deque([source])
        seen = set([source]) 
        while queue:
            curr = queue.popleft()
            if destination == curr:
                return True
            for neighbor in connections[curr]:
                if neighbor not in seen:
                    queue.append(neighbor)
                    seen.add(neighbor)
        return False