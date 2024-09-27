# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        length = 1
        hashmap = {}
        while curr is not None and curr.next is not None:
            length += 1
            curr = curr.next
            if curr.next is None:
                break
        curr = head
        if head == None or length == 1:
            return head
        for i in range(length-1, -1, -1):
            hashmap[i] = curr.val
            curr = curr.next
        curr = head
        for i in range(length):
            curr.val = hashmap[i]
            curr = curr.next
        return head