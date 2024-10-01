class Solution:
    hashtable = {}
    def climbStairs(self, n: int) -> int:
        if n in Solution.hashtable:
            return Solution.hashtable[n]
        if n == 0 or n == 1:
            return 1
        
        Solution.hashtable[n] = self.climbStairs(n-1) + self.climbStairs(n-2)

        return Solution.hashtable[n]