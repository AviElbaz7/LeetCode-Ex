# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        elif not p or not q:
            return False
        else:
            q = deque([(p, q)])
            while q:
                n1, n2 = q.popleft()
                if not n1 and not n2:
                    continue
                if (n1 and not n2) or (n2 and not n1) or n1.val != n2.val:
                    return False
                q.append((n1.left, n2.left))
                q.append((n1.right, n2.right))
        return True