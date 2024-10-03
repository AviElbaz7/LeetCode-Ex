class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        """
            idea:
                We need to make a graph like structure for the given edges and then we can run a bfs or a dfs on this adjacency list and if the source and destination are both seen then we can go ahead and say true if we go through the entire
                traversal and don't see the src and destination then we know that this is not possible so we can return false.

                We'll visit each node once so we will have O(n) time and there will be a stack or a queue for either traversal function we decide on doing. So, space is O(n) as well.
        """
        adjacency_list = {}

        if not edges:
            return True

        # we know that the graph can be bidirectional so we need to make sure that we go both ways in our adjacency list creation 
        
        for node in edges:
            src = node[0]
            dst = node[1]

            if src in adjacency_list:
                adjacency_list[src].append(dst)
            else:
                adjacency_list[src] = [dst]

            if dst in adjacency_list:
                adjacency_list[dst].append(src)
            else:
                adjacency_list[dst] = [src]

        
        # first we should even check if the src is in our adjacency list in the first place:
        if source not in adjacency_list.keys():
            return False

        # bfs approach:
        q = collections.deque()

        # now, we can start the source and go through all possible nodes that it can visit and those nodes neighbors and so on
        q.append(source)
        visited = set()

        while q:
            qlen = len(q)
            for _ in range(qlen):
                curr_node = q.popleft()
                if curr_node == destination:
                    return True
                if curr_node not in visited:
                    for nei in adjacency_list[curr_node]:
                        q.append(nei)

                # we've added all neighbors to the queue so we can say that this node has been visited 
                visited.add(curr_node)


        # we didn't find it so we can return false
        return False


