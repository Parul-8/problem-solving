from collections import Counter
class Solution(object): 
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = Counter()
        i=0
        j=0
        ans = 0
        
        while(j<len(s)):
            d[s[j]]+=1
      
            while(d[s[j]] > 1):
                d[s[i]]-=1
                i+=1
      
            ans = max(ans,j-i+1)
            j+=1
        return ans
        
        

        