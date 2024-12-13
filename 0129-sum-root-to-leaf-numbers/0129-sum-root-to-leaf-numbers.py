# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        total = 0
        def dfs(curr, pathS):
            nonlocal total
            if not curr:
                return 0
                
            pathS = (pathS * 10) + curr.val
            if not curr.left and not curr.right:
                total += pathS
                return pathS

            left = dfs(curr.left, pathS)
            right = dfs(curr.right, pathS)

            return left + right
        val = dfs(root, 0)
        return total
        