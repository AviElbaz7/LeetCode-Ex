# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.number_of_path = 0
        def dfs(node, cur_sum):
            if not node:
                return
            
            cur_sum += node.val
            if cur_sum == targetSum:
                self.number_of_path += 1
            
            dfs(node.left, cur_sum)
            dfs(node.right, cur_sum)
        
        def traverse(node):
            if not node:
                return
            dfs(node, 0)
            traverse(node.left)
            traverse(node.right)

        traverse(root)
        return self.number_of_path