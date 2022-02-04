# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Find the middle of the linked list
        sPrev = None
        slow = head
        fast = head
        while fast and fast.next:
            sPrev = slow
            slow = slow.next
            fast = fast.next.next
        # Reverse the second half
        prev = None
        curr = slow
        nex = None
        while curr != None:
            nex = curr.next
            curr.next = prev
            prev = curr
            curr = nex

        # Test if palindrom
        i = prev
        j = head
        while i and j:
            if i.val != j.val:
                return False
            i = i.next
            j = j.next
        return True
