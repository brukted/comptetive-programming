from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        mono = []
        s = 0
        water = 0
        for h in height:
            if not len(mono):
                mono.append(h)
                s = h
                continue
            # Smaller wall so append
            if h < s:
                mono.append(h)
            else:
                while len(mono):
                    water += s - mono.pop()
                s = h
                mono.append(h)
        mono.reverse()
        if len(mono) > 1:
            water += self.trap(mono)
        return water
