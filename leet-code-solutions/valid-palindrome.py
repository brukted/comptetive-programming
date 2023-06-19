class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(filter(lambda c: c.isalnum(), s.lower()))
        return all(map(lambda i : s[i] == s[~i], range(len(s) // 2)))