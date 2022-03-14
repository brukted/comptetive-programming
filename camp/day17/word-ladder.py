class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # Impossible
        if endWord not in wordList:
            return 0
        
        letters = string.ascii_lowercase
        
        # Build word graph
        adj_map = {}
        wordSet = set()
        for word in wordList:
            wordSet.add(word)
            adj_map[word] = set()
        
        wordSet.add(beginWord)
        adj_map[beginWord] = set()
        
        for word in wordSet:
            for i in range(len(word)):
                for letter in letters:
                    relatedWord = word[:i] + letter +  word[i+1:]
                    if relatedWord in wordSet and relatedWord not in adj_map[word]:
                        adj_map[word].add(relatedWord)
                        adj_map[relatedWord].add(word)
            
        visited = {beginWord}
        bfsDeq = deque([(beginWord,1)]) # word , depth
        
        while bfsDeq:
            current_word , depth = bfsDeq.popleft()
            for word in adj_map[current_word]:
                if word not in visited:
                    if word == endWord:
                        return depth + 1
                    bfsDeq.append((word,depth + 1))
                    visited.add(word)
        
        return 0
        