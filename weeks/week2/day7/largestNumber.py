# https://leetcode.com/problems/largest-number/submissions/

def compare(a: int, b: int):
    if int(str(a)+str(b)) > int(str(b)+str(a)):
        return -1
    else:
        return 1


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums.sort(key=functools.cmp_to_key(compare))
        if nums[0] == 0:
            return "0"
        result = ""
        for n in nums:
            result += str(n)
        return result
