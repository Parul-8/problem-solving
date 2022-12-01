class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        mid = int(len(s)/2)
        s1 = s[0:mid]
        s2 = s[mid:]
        count1 = 0
        count2 = 0
        
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        
        for char in s1:
            if char in vowels:
                count1+=1
        for char in s2:
            if char in vowels:
                count2+=1
        if count1 == count2:
            return True
        return False
        
        