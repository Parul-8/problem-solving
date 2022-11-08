class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        s = list(sentence)
        s.sort()
        s = set(s)
        if (len(s) == 26):
            return True
        else:
            return False
        