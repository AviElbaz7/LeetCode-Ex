# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = deque()
        q.append(root)
        level_height = 1
        final_min_height_with_max_sum = 1
        max_level_sum = float('-inf')

        while q:
            cur_level_sum = 0
            n = len(q)
            for i in range(n):
                node = q.popleft()
                cur_level_sum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if max_level_sum < cur_level_sum:
                max_level_sum = cur_level_sum
                final_min_height_with_max_sum = level_height
            level_height += 1

        return final_min_height_with_max_sum