# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()
        curr = head
        while curr:
            if curr in seen:
                break
            seen.add(curr)
            curr = curr.next
        else:
            return False
        return True