class TrieNode:
    def __init__(self):
        self.children = {}

class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words.sort(key = lambda x : len(x), reverse = True)
        
        root = TrieNode()
        length = 0
        
        for word in words:
            word = word[::-1]
            
            node = root
            new_word = False
            
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                    new_word = True
                
                node = node.children[ch]
            
            if new_word:
                length += len(word) + 1
        
        return length
