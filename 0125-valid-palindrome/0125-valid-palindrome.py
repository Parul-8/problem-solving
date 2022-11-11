class Solution:
    def isPalindrome(self, s: str) -> bool:
        ans =[]
        for i in s:
            if i.islower() or i.isdigit():
                ans.append(i)
            elif i.isupper():
                ans.append(i.lower())
        newS = ''.join(ans)
        
        l = 0
        r = len(newS)-1
        while(l<r):
            if(newS[l]!=newS[r]):
                return False
            l+=1
            r-=1
        return True
        