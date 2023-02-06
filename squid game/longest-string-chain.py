class Solution:
    def isPredecessor(self, predecessor, word):
        j = i = 0

        while i < len(predecessor):
            if predecessor[i] == word[j]:
                i += 1
            elif i != j:
                return False
            j += 1

        return True

    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=lambda word: len(word))
        graph = defaultdict(list)

        for i in range(len(words)):
            word = words[i]
            for j in range(i, len(words)):
                second_word = words[j]
                if len(second_word) == len(word):
                    continue
                elif len(second_word) > len(word) + 1:
                    break

                if self.isPredecessor(word, second_word):
                    graph[word].append(second_word)

        @cache
        def solve(word):
            ans = 0
            for next in graph[word]:
                ans = max(ans, solve(next))
            return ans + 1

        return max(map(solve, words))
