class LinkedListNode:
    def __init__(self, val):
        self.next = None
        self.prev = None
        self.val = val

    def __str__(self):
        return str(self.val) + " -> " + str(self.next)


class LRUCache:

    def __init__(self, capacity: int):
        self.head = None
        self.tail = None
        self.capacity = capacity
        self.hashMap = {}  # key : (LinkedListNode)
        self.size = 0

    def remove(self, key):
        node = self.hashMap[key]
        self.hashMap.pop(key)
        if node.prev:
            node.prev.next = node.next
        else:  # node is the head
            self.head = node.next
        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev
        self.size -= 1

    def putNode(self, node):
        if self.tail:
            self.tail.next = node
        node.prev = self.tail
        node.next = None
        self.tail = node
        if not self.head:
            self.head = self.tail
        self.size += 1
        self.hashMap[node.val[0]] = node

    def get(self, key: int) -> int:
        # print("Get",key,self.head,self.hashMap)
        if key in self.hashMap:
            node = self.hashMap[key]
            self.remove(key)
            self.putNode(node)
            val = self.tail.val[1]
            # print(self.head)
            return val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        # print("Put",(key,value),self.head)
        # If full remove the least recently used and the not replace
        if self.size == self.capacity and not key in self.hashMap:
            self.remove(self.head.val[0])
        # If doesn't exist there is no need to remove from the list
        if key in self.hashMap:
            self.remove(key)
        tu = key, value
        node = LinkedListNode(tu)
        self.putNode(node)
        # print(self.hashMap,self.head)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
