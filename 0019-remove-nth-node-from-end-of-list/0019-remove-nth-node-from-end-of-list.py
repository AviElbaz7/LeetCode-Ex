# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        counter = 0
        while curr is not None:
            curr = curr.next
            counter += 1
        if n == counter:
            return head.next
        curr = head
        for i in range(counter-n-1):
            curr = curr.next
        curr.next = curr.next.next
        return head