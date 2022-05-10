class Node:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()

        root = Node()
        longest = ""
        l_len = 0
        
        for word in words:
            node = root
            can_be_built = True
            
            for idx, ch in enumerate(word):
                if ch not in node.children:
                    node.children[ch] = Node()
                node = node.children[ch]
                if idx != len(word) - 1:
                    can_be_built = can_be_built and node.is_word
            
            node.is_word = True
            
            if can_be_built and len(word) > l_len:
                l_len = len(word)
                longest = word
        
        return longest
