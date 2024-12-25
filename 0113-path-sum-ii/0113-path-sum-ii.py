# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        def dfs(currNode, currList, target):
            if not currNode:
                return

            target -= currNode.val
            currList.append(currNode.val)

            if target == 0 and not currNode.left and not currNode.right:
                res.append(currList.copy())

            dfs(currNode.left, currList, target)
            dfs(currNode.right, currList, target)

            currList.pop()
            return
        dfs(root, [], targetSum)
        return res