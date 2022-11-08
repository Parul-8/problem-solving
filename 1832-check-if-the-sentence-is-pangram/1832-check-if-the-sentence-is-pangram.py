class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        l1 = list('abcdefghijklmnopqrstuvwxyz')
        l1.sort()
        s1 = ''.join(list(set(l1)))
        l2 = list(sentence)
        l2.sort()
        s2 = ''.join(list(set(l2)))
        if s1 == s2:
            return True
        else:
            return False
        