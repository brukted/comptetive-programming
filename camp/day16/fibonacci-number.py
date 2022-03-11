class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        
        n_1 , n_2 = 0 , 1
        k = 1
        
        while k != n:
            n_1 , n_2 = n_2 , n_1 + n_2
            k += 1
        
        return n_2