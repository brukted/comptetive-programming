class Node:
    def __init__(self, count = 0,prev = None, next = None):
        self.prev = prev
        self.next = next
        self.count = count
        self.keys = set()

class AllOne:

    def __init__(self):
        self.key_to_node_map = {}
        self.head = Node()
        self.tail = self.head

    def remove_node(self, node):
        if node == self.tail:
            self.tail = node.prev
            self.tail.next = None
        else:
            node.next.prev, node.prev.next = node.prev, node.next
    
    def inc(self, key: str) -> None:
        if key not in self.key_to_node_map:
            self.key_to_node_map[key] = self.head
            self.head.keys.add(key)
            return self.inc(key)

        node = self.key_to_node_map[key]
        if node == self.tail:
            self.tail = Node(node.count + 1, node)
            node.next = self.tail
        if node.next.count != node.count + 1:
            new_node = Node(node.count + 1, node, node.next)
            node.next.prev = node.next = new_node
        
        node.keys.remove(key)
        node.next.keys.add(key)

        self.key_to_node_map[key] = node.next
        if node.count != 0 and len(node.keys) == 0:
            self.remove_node(node)
    
    def dec(self, key: str) -> None:
        node = self.key_to_node_map[key]

        if node.prev.count != node.count - 1:
            prev = node.prev
            new_node= Node(node.count - 1, prev, node)
            node.prev = prev.next = new_node
        
        prev = node.prev
        node.keys.remove(key)

        if node.count != 1:
            prev.keys.add(key)
            self.key_to_node_map[key] = prev
        else:
            self.key_to_node_map.pop(key)
        
        if len(node.keys) == 0:
            self.remove_node(node)

    def getMaxKey(self) -> str:
        if self.tail.count == 0:
            return ""
        
        for k in self.tail.keys:
            return k

    def getMinKey(self) -> str:
        if self.tail.count == 0:
            return ""
        for k in self.head.next.keys:
            return k
        
# hello = 2
# leet = 1


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
