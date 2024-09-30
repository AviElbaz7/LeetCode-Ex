# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        if not root:
            return result
        queue = []
        queue.append(root)
        left = True
        while queue:
            levelarr = []
            for i in range(len(queue)):
                curr = queue.pop(0)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                if left:
                    levelarr.append(curr.val)
                else:
                    levelarr.insert(0, curr.val)
            left = not left
            result.append(levelarr)
        return result