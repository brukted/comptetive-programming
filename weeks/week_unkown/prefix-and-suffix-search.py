class PrefixTrieNode:
    def __init__(self):
        self.children = {}
        self.indices = []
        
class SuffixTrieNode:
    def __init__(self):
        self.children = {}
        self.indices = set()

class WordFilter:

    def __init__(self, words: List[str]):
        self.prefix_root = PrefixTrieNode()
        self.suffix_root = SuffixTrieNode()
        
        for idx, word in enumerate(words):
            node = self.prefix_root
            
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = PrefixTrieNode()
                node = node.children[ch]
                node.indices.append(idx)
            
            word = reversed(word)
            node = self.suffix_root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = SuffixTrieNode()
                node = node.children[ch]
                node.indices.add(idx)
    
    
    def f(self, prefix: str, suffix: str) -> int:
        suffix = reversed(suffix)

        prefix_node = self.prefix_root
        for ch in prefix:
            if ch not in prefix_node.children:
                return -1
            prefix_node = prefix_node.children[ch]
        
        suffix_node = self.suffix_root
        for ch in suffix:
            if ch not in suffix_node.children:
                return -1
            suffix_node = suffix_node.children[ch]
        
        prefix_indices = prefix_node.indices
        suffix_indices = suffix_node.indices
        
        for i in range(len(prefix_indices)-1 ,-1 ,-1):
            if prefix_indices[i] in suffix_indices:
                return prefix_indices[i]
        
        return -1
