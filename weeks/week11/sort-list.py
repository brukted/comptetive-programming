# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        def merge(left,right):
            if not left or not right:
                return left if not left else right
            
            new_head = None
            
            if left.val < right.val:
                new_head = left
                left = left.next
            else:
                new_head = right
                right = right.next
            
            new_end = new_head
            
            while left and right:
                if left.val < right.val:
                    new_end.next = left
                    left = left.next
                else:
                    new_end.next = right
                    right = right.next
                new_end = new_end.next
            
            new_end.next = left if left else right
            
            return new_head
        
        def mergeSort(node):
            if not node.next:
                return node
            
            left_end = node
            h = node
            while h.next and h.next.next:
                left_end = left_end.next
                h = h.next.next
            
            right = left_end.next
            left_end.next = None
            left = node
            
            left = mergeSort(left)
            right = mergeSort(right)
            return merge(left,right)
            
        return mergeSort(head)
