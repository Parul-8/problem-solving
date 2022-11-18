class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l_s = list(s)
        l_t = list(t)
        l_s.sort()
        l_t.sort()
        print(l_s,l_t)
        if ''.join(l_s) == ''.join(l_t):
            return True
        return False
        