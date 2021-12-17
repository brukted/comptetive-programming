# https://leetcode.com/problems/implement-stack-using-queues/

class MyStack:

    def __init__(self):
        self.queue1 = []
        self.queue2 = []
        self.activeQueue = self.queue1
        self.altQueue = self.queue2

    def push(self, x: int) -> None:
        self.activeQueue.append(x)

    def pop(self) -> int:
        while len(self.activeQueue) != 1:
            #           enque              deque
            self.altQueue.append(self.activeQueue.pop(0))
        val = self.activeQueue.pop(0)
        self.activeQueue, self.altQueue = self.altQueue, self.activeQueue
        return val

    def top(self) -> int:
        while len(self.activeQueue) != 1:
            #           enque              deque
            self.altQueue.append(self.activeQueue.pop(0))
        val = self.activeQueue.pop(0)
        self.activeQueue, self.altQueue = self.altQueue, self.activeQueue
        self.push(val)
        return val

    def empty(self) -> bool:
        return len(self.activeQueue) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
