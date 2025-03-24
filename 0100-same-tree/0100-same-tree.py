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
            q1, q2 = deque(), deque()
            q1.append(p)
            q2.append(q)
            while q1 or q2:
                for i in range(max(len(q1), len(q2))):
                    if (q1 and not q2) or (q2 and not q1):
                        return False
                    print(q1, q2)
                    node1, node2 = q1.popleft(), q2.popleft()
                    if node1.val != node2.val:
                        return False
                    if (node1.left and not node2.left) or (node2.left and not node1.left):
                        return False
                    if (node1.right and not node2.right) or (node2.right and not node1.right):
                        return False
                    if node1.left:
                        q1.append(node1.left)
                    if node1.right:
                        q1.append(node1.right)
                    if node2.left:
                        q2.append(node2.left)
                    if node2.right:
                        q2.append(node2.right)
        return True