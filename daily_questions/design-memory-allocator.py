class Allocator:
    def __init__(self, n: int):
        self.memory = [-1 for _ in range(n)]
        self.n = n

    def allocate(self, size: int, mID: int) -> int:
        i, j = 0, -1

        while i < self.n:
            if self.memory[i] == -1:
                j = i
                while j < self.n and self.memory[j] == -1 and j - i != size:
                    j += 1
                if j - i == size:
                    for idx in range(i, j):
                        self.memory[idx] = mID
                    return i
                else:
                    i = j
            else:
                i += 1
        return -1

    def free(self, mID: int) -> int:
        freed = 0
        for i in range(self.n):
            if self.memory[i] == mID:
                self.memory[i] = -1
                freed += 1
        return freed


# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.free(mID)
