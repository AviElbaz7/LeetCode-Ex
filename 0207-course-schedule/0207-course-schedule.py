class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_l = defaultdict(list)
        state = [0] * numCourses
        unvisited = 0
        visiting = 1
        visited = 2
        for a, b in prerequisites:
            adj_l[a].append(b)
        
        def dfs(node):
            if state[node] == visited:
                return True
            if state[node] == visiting:
                return False

            state[node] = 1
            for neighbor in adj_l[node]:
                if not dfs(neighbor):
                    return False
            state[node] = 2
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True