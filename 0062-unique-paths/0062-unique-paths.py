class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        def helper(m, n, memo) -> int:
            if (m, n) in memo:
                return memo[(m, n)]
            if n == 1 or m == 1:
                return 1
            
            memo[(m, n)] = helper(m - 1, n, memo) + helper(m, n - 1, memo)
            return memo[(m, n)]
        return helper(m, n, memo)