# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        stack = [root]
        res = []
        if not root:
            return res

        leftToRight = True
        while stack:
            temp = []
            length = len(stack)
            for i in range(length):
                curr = stack.pop(0)
                if leftToRight:
                    temp.append(curr.val)
                else:
                    temp.insert(0, curr.val)
                if curr.left:
                    stack.append(curr.left)
                if curr.right:
                    stack.append(curr.right)
            leftToRight = not leftToRight
            res.append(temp)
        return res