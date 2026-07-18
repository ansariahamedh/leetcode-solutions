class Solution:
    def isAnagram(self, s:str, t:str) -> bool:
        word1 = {}
        word2 = {}

        for ch in s:
            if ch in word1:
                word1[ch] += 1
            else:
                word1[ch] = 1

        for ch in t:
            if ch in word2:
                word2[ch] += 1
            else:
                word2[ch] = 1

        if word1 == word2:
            return True
        else:
            return False