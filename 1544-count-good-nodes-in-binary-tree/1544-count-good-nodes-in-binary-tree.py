# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.total = 0
        def dfs(node, max_val_until):
            if not node:
                return
            
            if node.val >= max_val_until:
                max_val_until = node.val
                self.total += 1

            dfs(node.left, max_val_until)
            dfs(node.right, max_val_until)
        
        dfs(root, root.val)
        return self.total