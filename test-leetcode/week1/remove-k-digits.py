class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
    
        for n in num:
            while k and stack and stack[-1] > int(n):
                stack.pop()
                k -= 1
            stack.append(int(n))
        
        while k:
            stack.pop()
            k -= 1
        
        
        return str(int("".join(map(str, stack)))) if stack else "0"