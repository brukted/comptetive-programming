class WordDictionary:
    class Node:
        def __init__(self):
            self.children = {}
            self.is_end = False
    
    def __init__(self):
        self.root = self.Node()

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = self.Node()
            node = node.children[ch]
        node.is_end = True

    def search(self, word: str) -> bool:
        return self._serachRec(word, 0, self.root)
    
    def _serachRec(self,word,idx,node) -> bool:
        char = word[idx]        
        
        if char == ".":
            if idx == len(word) - 1:
                for child_node in node.children.values():
                    if child_node.is_end:
                        return True
                return False
            
            for child_node in node.children.values():
                if self._serachRec(word, idx + 1, child_node):
                    return True
            return False
        
        else:
            if idx == len(word) - 1:
                return char in node.children and node.children[char].is_end
            
            return self._serachRec(word, idx + 1, node.children[char]) if char in node.children else False
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
