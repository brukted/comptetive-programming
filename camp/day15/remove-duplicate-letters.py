class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        count = Counter(s)
        checked = set()
        stack = []
        
        for i in s:
            if i in checked:
                count[i] -= 1
                continue
            
            if not stack:
                stack.append(i)
                checked.add(i)
                continue
            
            if i > stack[-1]:
                stack.append(i)
                checked.add(i)
            else:
                while stack and count[stack[-1]] > 1 and i < stack[-1]:         
                    count[stack[-1]] -= 1
                    checked.remove(stack[-1])
                    stack.pop()
                stack.append(i)
                checked.add(i)
        
        return "".join(stack)