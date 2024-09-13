# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        prev = dummy
        for i in range(left - 1):
            prev = prev.next
        
        reversed_start = prev.next
        current = reversed_start.next
        for i in range(right - left):
            reversed_start.next = current.next
            current.next = prev.next
            prev.next = current
            current = reversed_start.next
        
        return dummy.next