# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import List, Optional


class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        monoStack = []
        result = [0]
        monoStack.append((head, 0))
        j = head.next
        i = 1
        while(j != None):
            result.append(0)
            while len(monoStack) and j.val > monoStack[-1][0].val:
                result[monoStack.pop()[1]] = j.val
            monoStack.append((j, i))
            j = j.next
            i += 1
        return result
