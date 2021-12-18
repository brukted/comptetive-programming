# https://leetcode.com/problems/design-circular-deque/

class MyCircularDeque:

    def resolveIndex(self, idx: int) -> int:
        if idx >= 0:
            return idx % self.size
        else:
            return self.size-(idx*-1)

    def __init__(self, k: int):
        self.mList = [0] * k
        self.size = k
        # Keeps track of the first element
        self.front = 0
        # Keeps track of the last avilable place at the back of the deck
        self.back = 0
        self.leng = 0

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.front = self.resolveIndex(self.front - 1)
        self.mList[self.front] = value
        self.leng += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.mList[self.back] = value
        self.back = self.resolveIndex(self.back + 1)
        self.leng += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.front = self.resolveIndex(self.front+1)
        self.leng -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.back = self.resolveIndex(self.back - 1)
        self.leng -= 1
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.mList[self.front]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.mList[self.resolveIndex(self.back - 1)]

    def isEmpty(self) -> bool:
        return self.leng == 0

    def isFull(self) -> bool:
        return self.leng == self.size


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
