class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            minn = nums[i]
            maxx = nums[i]
            for j in range(i,len(nums)):
                minn = min(minn,nums[j])
                maxx = max(maxx,nums[j])
                ans += maxx - minn
        return ans
