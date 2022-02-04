# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # Find the middle of the linked list
        slow = head
        fast = head
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the first half
        prev = None
        curr = head
        nex = None
        end = slow.next
        while curr != end:
            nex = curr.next
            curr.next = prev
            prev = curr
            curr = nex

        # Find max
        i = prev
        j = end
        max_sum = 0
        while i and j:
            max_sum = max(i.val+j.val, max_sum)
            i = i.next
            j = j.next
        return max_sum
