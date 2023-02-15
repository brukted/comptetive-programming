class Solution:
    def numSquarefulPerms(self, nums):
        def solve(ans, path):
            if not ans:
                res.add(tuple(path))

            for i in range(len(ans)):
                if i>0 and ans[i] == ans[i-1]:
                    continue
                if path and not (sqrt(path[-1] + ans[i]) == floor(sqrt(path[-1] + ans[i]))):
                    continue

                solve(ans[:i] + ans[i+1:], path + [ans[i]])

        res = set()
        solve(nums, [])
        return len(res)
