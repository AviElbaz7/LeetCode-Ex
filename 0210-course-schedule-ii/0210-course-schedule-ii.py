class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        order = []
        adj_l = defaultdict(list)
        for a, b in prerequisites:
            adj_l[a].append(b)
        
        unvisited, visiting, visited = 0, 1, 2
        state = [unvisited] * numCourses

        def dfs(node):
            if state[node] == visited:
                return True
            if state[node] == visiting:
                return False
            
            state[node] = visiting
            for neighbor in adj_l[node]:
                if not dfs(neighbor):
                    return False
            state[node] = visited
            order.append(node)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []

        return order