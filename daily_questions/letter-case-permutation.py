class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ans, curr = [], [None] * len(s)

        def solve(i=0):
            if i == len(s):
                ans.append("".join(curr))
            else:
                curr[i] = s[i].lower()
                solve(i + 1)

                if s[i].isalpha():
                    curr[i] = s[i].upper()
                    solve(i + 1)

        solve()
        return ans
