# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class NodeWrapper:
    def __init__(self, node):
        self.node = node

    def __lt__(self, other):
        return self.node.val < other.node.val


class Solution:
    def addNode(self, head, tail, node):
        if head:
            tail.next = node
            return head, node
        else:
            return node, node

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heads_heap = []
        for h in lists:
            if h:
                hh = NodeWrapper(h)
                heads_heap.append(hh)
        heapq.heapify(heads_heap)
        head = None
        tail = None
        while len(heads_heap):
            # Min node is tail
            if not heads_heap[0].node.next:
                node = heapq.heappop(heads_heap).node
                head, tail = self.addNode(head, tail, node)
            else:
                h = heapq.heappop(heads_heap).node
                head, tail = self.addNode(head, tail, h)
                heapq.heappush(heads_heap, NodeWrapper(h.next))
        return head
