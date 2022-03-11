class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        alphabet_string = str(string.ascii_lowercase)
        
        for i in range(len(palindrome)):
            # Middle of the string in an odd long string
            if i == (len(palindrome) - 1) // 2 and len(palindrome) % 2 == 1:
                continue
            
            for ch in alphabet_string:
                if ch >= palindrome[i]:
                    break
                if ch != palindrome[i]:
                    return palindrome[:i] + ch + palindrome[i+1:]
        
        if len(palindrome) > 1:
            return palindrome[:-1] + chr(ord(palindrome[-1]) + 1)
        
        return ""