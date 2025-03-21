class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        memo = {}
        m = len(obstacleGrid)    
        n = len(obstacleGrid[0])

        if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1:
            return 0

        def pathNums(m, n) -> int:
            if m < 0 or n < 0:
                return 0
            
            if obstacleGrid[m][n] == 1:
                return 0

            if m == 0 and n == 0:
                return 1
            
            if (m, n) in memo:
                return memo[(m, n)]
            
            memo[(m, n)] = pathNums(m - 1, n) + pathNums(m, n - 1)

            return memo[(m, n)]

        return pathNums(m-1, n-1)