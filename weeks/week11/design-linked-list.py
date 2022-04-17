class LinkedListNode:
    def __init__(self,val = 0,next = None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def get(self, index: int) -> int:
        h = self._head        
        while h and index > 0:
            h = h.next
            index -= 1
        if not h:
            return -1
        return h.val

    def addAtHead(self, val: int) -> None:
        if not self._head:
            self._head = LinkedListNode(val)
            self._tail = self._head
        else:
            self._head = LinkedListNode(val,self._head)
        self._size += 1
            
    def addAtTail(self, val: int) -> None:
        if not self._head:
            self._head = LinkedListNode(val)
            self._tail = self._head
        else:
            self._tail.next = LinkedListNode(val)
            self._tail = self._tail.next
        self._size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index == self._size:
            return self.addAtTail(val)
        if index == 0:
            return self.addAtHead(val)
        if index > self._size:
            return
        prev = None
        i = self._head
        while index > 0:
            prev = i
            i = i.next
            index -= 1
        prev.next = LinkedListNode(val , i)
        self._size += 1
    
    def deleteAtIndex(self, index: int) -> None:
        if index >= self._size: # Out of bound
            return
        if index == 0: # Head
            self._head= self._head.next
            if self._size == 1: # Reset tail
                self._tail = None
            self._size -= 1
            return
        prev = None
        i = self._head
        while index > 0:
            prev = i
            i = i.next
            index -= 1
        prev.next = i.next
        if not i.next:
            self._tail = prev
        self._size -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
