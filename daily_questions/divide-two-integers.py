class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = 1 if (dividend <= 0 and divisor <= 0 or dividend >= 0 and divisor >= 0) else -1
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        ans = 0
        
        while dividend >= divisor:
            best, i = 0, 1
            for i < 32 and dividend >> i >= divisor:
                best = i
                i += 1
            
            ans += 2 ** best
            dividend -= divisor << max(best, 1)
            
        
        return min(max(ans * sign, -(2 ** 31)), 2 ** 31 - 1)