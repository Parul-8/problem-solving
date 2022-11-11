class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def chkPal(s,l,r):
            while(l<r):
                if s[l]!=s[r]:
                    return False
                l+=1 
                r-=1
            return True
    
        l = 0
        r = len(s)-1
        while(l<r):
            if(s[l]!=s[r]):
                return chkPal(s,l+1,r) or chkPal(s,l,r-1)
            
            l+=1
            r-=1
        return True
                
            
        