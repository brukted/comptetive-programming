# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        if not slow.next:
            return
        
        prev = None
        curr = slow.next
        slow.next = None
        while curr.next:
            temp = curr
            nex = curr.next
            curr.next = prev
            prev = temp
            curr = nex
        curr.next = prev
        
        t = head
        even = head.next
        odd = curr
        i = 2
        
        while even and odd:
            if i % 2 == 0:
                t.next = odd
                odd = odd.next
            else:
                t.next = even
                even = even.next
            t = t.next
            i += 1
        
        t.next = even if even else odd
                
