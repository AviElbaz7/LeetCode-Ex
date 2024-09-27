# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        curr = head
        number = ''
        while curr:
            number += str(curr.val)
            curr = curr.next
        right = len(number) - 1
        left = 0
        while left < right:
            if number[left] != number[right]:
                break
            left += 1
            right -= 1
        else:
            return True
        return False