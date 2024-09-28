# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = []
        self.inOrder(root, stack)
        print(stack)
        while stack:
            val = stack.pop()
            if not stack:
                return True
            peek = stack[-1]
            if val <= peek:
                return False
        return True

    def inOrder(self, root: Optional[TreeNode], stack: List[int]) -> List[int]:
        if root is not None:
            self.inOrder(root.left, stack)
            stack.append(root.val)
            self.inOrder(root.right, stack)
        return stack