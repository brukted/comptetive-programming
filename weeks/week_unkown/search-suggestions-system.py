class TrieNode():
    def __init__(self):
        self.children = [None] * 26
        self.is_word = False

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        root = TrieNode()
        
        for product in products:
            node = root
            for ch in product:
                idx = ord(ch) - 97
                if not node.children[idx]:
                    node.children[idx] = TrieNode()
                node = node.children[idx]
            node.is_word = True
        
        ans = []
        stack = []
        
        def dfsWord(start):
            if start.is_word:
                ans[-1].append("".join(stack))
                
            if len(ans[-1]) == 3:
                return
            
            for i in range(26):
                stack.append(chr(97+i))
                if start.children[i]:
                    dfsWord(start.children[i])
                
                stack.pop()
                if len(ans[-1]) == 3:
                    return
        
        node = root
        
        for i in range(len(searchWord)):
            idx = ord(searchWord[i]) - 97
            node = node.children[idx]
            stack.append(searchWord[i])
            
            if not node: # Character not in trie
                break
            
            ans.append([])
            dfsWord(node)
        
        for _ in range(len(searchWord) - len(ans)):
            ans.append([])

        return ans
