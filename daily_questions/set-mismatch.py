class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        all_xor = reduce(xor, nums) ^ reduce(xor, range(1, len(nums) + 1))

        for i in range(len(nums)):
            cIdx = nums[i] - 1

            while cIdx < len(nums) and cIdx != i:
                if nums[i] == nums[cIdx]:
                    return [nums[i], all_xor ^ nums[i]]

                nums[i], nums[cIdx] = nums[cIdx], nums[i]
                cIdx = nums[i] - 1
