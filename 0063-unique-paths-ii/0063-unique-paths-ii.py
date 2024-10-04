class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        memo = {}
        m = len(obstacleGrid)  # Number of rows
        n = len(obstacleGrid[0])  # Number of columns

        # If the start or end has an obstacle, return 0 immediately
        if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1:
            return 0

        def pathNums(m, n) -> int:
            # Base case: If out of bounds, return 0
            if m < 0 or n < 0:
                return 0
            
            # If current cell is an obstacle, return 0
            if obstacleGrid[m][n] == 1:
                return 0
            
            # Base case: If at the start (0, 0), return 1
            if m == 0 and n == 0:
                return 1

            # Check memoized results
            if (m, n) in memo:
                return memo[(m, n)]

            # Recursively calculate the number of unique paths from top and left cells
            memo[(m, n)] = pathNums(m - 1, n) + pathNums(m, n - 1)
            return memo[(m, n)]

        # Start the recursion from the bottom-right corner
        return pathNums(m - 1, n - 1)
