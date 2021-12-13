# https://leetcode.com/problems/sorting-the-sentence/

class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split()
        dic = []
        for word in words:
            word = word.strip()
            dic.append([int(word[-1:]), word[:-1]])
        dic.sort()
        sentence = dic[0][1]
        for i in range(1, len(dic)):
            sentence += " " + dic[i][1]
        return sentence
