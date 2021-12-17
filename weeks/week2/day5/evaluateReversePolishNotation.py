# https: // leetcode.com/problems/evaluate-reverse-polish-notation/
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {'+', '*', '/', '-'}
        for i in tokens:
            if i in ops:
                b, a = stack.pop(), stack.pop()
                if i == '+':
                    stack.append(a+b)
                elif i == '*':
                    stack.append(a*b)
                elif i == '/':
                    stack.append(trunc(a/b))
                elif i == '-':
                    stack.append(a-b)
            else:
                stack.append(int(i))
        return stack.pop()
