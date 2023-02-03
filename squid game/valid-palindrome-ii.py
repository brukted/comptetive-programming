class Solution:
    @lru_cache(None)
    def is_palindrome(self, s, i, j):
        if s[i] != s[j]:
            return False

        if i + 1 < j - 1:
            return self.is_palindrome(s, i + 1, j - 1)

        return True

    def validPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1

        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
                continue
            return self.is_palindrome(s, i + 1, j) or self.is_palindrome(s, i, j - 1)

        return True
