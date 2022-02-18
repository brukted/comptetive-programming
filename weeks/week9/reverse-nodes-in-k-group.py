# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def reverseSubList(self, head, end):
        prev = None
        current = head
        while(current is not end):
            next = current.next
            current.next = prev
            prev = current
            current = next
        return prev

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        preHead = None
        start = head
        new = None

        i = head
        n = 0
        # When n == k, i is at the end of the sub list with k length
        while i != None:
            if n != k:
                i = i.next
                n += 1
            else:
                end = i
                new_head = self.reverseSubList(start, end)
                start.next = end
                if preHead:
                    preHead.next = new_head
                if not new:
                    new = new_head
                preHead = start
                start = end
                i = i.next
                n = 1
        # When n % k == 0, there is a k long sub list that is not flipped
        if n == k:
            end = i
            new_head = self.reverseSubList(start, end)
            start.next = end
            if preHead:
                preHead.next = new_head
            if not new:
                new = new_head
        return new
