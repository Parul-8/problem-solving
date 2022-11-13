import re
class Solution:
    def reverseWords(self, s: str) -> str:
        #bruteforce
        #remove unncessary spaces--> string --> list --> reverse list --> string
        
        #res = " ".join(s.split())
        res = s.split()
        res.reverse()
        return ' '.join(res)
        
            