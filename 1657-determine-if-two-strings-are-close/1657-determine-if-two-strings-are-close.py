class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        
        d1, d2 = {}, {}
        s1, s2 = [], []
        
        for c in word1:
            if c not in d1:
                s1.append(c)
                d1[c] = 0
            d1[c] += 1
        
        for c in word2:
            if c not in d2:
                s2.append(c)
                d2[c] = 0
            d2[c] += 1
        
        s1.sort()
        s2.sort()

        if s1 != s2:
            return False
        
        c1 = [v for _,v in d1.items()]
        c2 = [v for _,v in d2.items()]
        c1.sort()
        c2.sort()

        if c1 != c2:
            return False
        
        return True
        
        