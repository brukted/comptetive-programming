# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        h = None
        tail = None
        i = head
        j = head
        while j != None:
            while j != None and i.val == j.val:
                j = j.next
            # Duplicate node
            if j != i.next:
                i = j
                continue
            # Unique node
            if h == None:
                h = i
                tail = i
            else:
                tail.next = i
                tail = tail.next
            i = j
        if tail:
            tail.next = None
        return h
