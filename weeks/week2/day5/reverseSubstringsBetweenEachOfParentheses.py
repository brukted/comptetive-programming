# https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/

class Solution:
    def reverseParentheses(self, s: str) -> str:
        result = []
        temp = []
        for ch in s:
            if ch != ')':
                result.append(ch)
            else:
                while len(result) and result[-1] != '(':
                    temp.append(result.pop())
                result.pop()
                result += temp
                temp.clear()

        return "".join(result)
