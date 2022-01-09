# https://leetcode.com/problems/k-th-symbol-in-grammar/
class Solution:
    def grammerSymbol(self, n: int, k: int, c: bool = False):
        if k == 1 or n == 1:
            if c:
                return True
            else:
                return False
        # even
        if k % 2 == 0:
            return self.grammerSymbol(n-1, k//2, not c)
        else:
            return self.grammerSymbol(n-1, (k//2)+1, c)

    def kthGrammar(self, n: int, k: int) -> int:
        if k == 1:
            return 0
        a = self.grammerSymbol(n, k)
        if a:
            return 1
        else:
            return 0
