# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        closingTags = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        stack = []
        for p in s:
            if not p in closingTags.keys():
                stack.append(p)
            else:
                if not stack.pop() == closingTags[p]:
                    break
        return len(stack) == 0
