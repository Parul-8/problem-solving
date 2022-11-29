class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        dict_map = { ')':'(','}':'{',']':'[' }
        
        for char in s:
            if char in dict_map:
                top = stack.pop() if stack else '#' 
                
                if dict_map[char] != top:
                    return False
                
            
            else:
                stack.append(char)
        return not stack
        