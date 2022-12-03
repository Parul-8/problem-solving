from collections import Counter
class Solution(object): 
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        i = 0
        d = {}
        for j in range(len(s)):
            
            if s[j] in d:
                i = max(i,d[s[j]])
            d[s[j]] = j+1
            ans = max(ans,j-i+1)
        return ans
        
        

        