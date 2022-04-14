class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        s = [0 for _ in range(len(nums))]
        mul = 1
        for idx , i in enumerate(nums):
            s[idx] = mul
            mul *= i
        mul = 1
        for idx in range(len(nums) - 1, -1 , -1):
            s[idx] *= mul
            mul *= nums[idx]
        return s
