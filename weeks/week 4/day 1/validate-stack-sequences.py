# https://leetcode.com/problems/validate-stack-sequences/

from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        while len(pushed):
            if not len(stack):
                stack.append(pushed.pop(0))
                continue

            if popped[0] == stack[-1]:
                stack.pop()
                popped.pop(0)
            else:
                stack.append(pushed.pop(0))

        while len(popped):
            if not len(stack) or stack[-1] != popped[0]:
                return False
            stack.pop()
            popped.pop(0)
        return True
