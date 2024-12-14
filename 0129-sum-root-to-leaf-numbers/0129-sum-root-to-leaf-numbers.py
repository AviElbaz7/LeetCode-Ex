# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(curr, pathS):
            if not curr:
                return 0
                
            pathS = (pathS * 10) + curr.val
            # got to a leaf node
            if not curr.left and not curr.right:
                return pathS

            left = dfs(curr.left, pathS)
            right = dfs(curr.right, pathS)

            return left + right

        return dfs(root, 0)
        