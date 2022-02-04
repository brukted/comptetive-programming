# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        sPrev = None
        slow = head
        fast = head
        while n != 0:
            fast = fast.next
            n -= 1
        while fast != None:
            sPrev = slow
            slow = slow.next
            fast = fast.next
        if sPrev == None:
            return slow.next
        else:
            sPrev.next = slow.next
            return head
