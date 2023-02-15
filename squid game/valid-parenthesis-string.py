class Solution:
    def checkValidString(self, s: str) -> bool:
        @cache
        def solve(idx, opens):
            if idx == len(s):
                return opens == 0
            
            if opens < 0:
                return False

            if s[idx] == '(':
                return solve(idx + 1, opens + 1)
            elif s[idx] == ')':
                return solve(idx + 1, opens - 1)
            
            return solve(idx + 1, opens - 1) or solve(idx + 1, opens + 1) or solve(idx + 1, opens)
        
        return solve(0, 0)
