class Solution:
    def largestRectangleArea(self, arr: List[int]) -> int:
        monoStack = [(-inf, -1, None)]
        ans = 0
        
        for idx, num in enumerate(arr):        
            while monoStack and monoStack[-1][0] >= num:
                mV, mI, mS = monoStack.pop()
                ans = max(ans, (mI - mS + idx - 1 - mI) * mV)
            monoStack.append((num, idx, monoStack[-1][1]))
        
        for (mV, mI, mS) in monoStack[1:]:
            ans = max(ans, (mI - mS + len(arr) - 1 - mI) * mV)
        
        return ans
