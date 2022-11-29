from random import choice
class RandomizedSet:

    def __init__(self):
        self.d = {}
        self.lst = []
        

    def insert(self, val: int) -> bool:
        if val in self.lst:
            return False
        
        
        self.d[val] = len(self.lst)
        self.lst.append(val)
        return True
    
        

    def remove(self, val: int) -> bool:
        
        if val in self.lst:
           
            last_element = self.lst[-1]
            indx = self.d[val]
            self.lst[indx] = last_element
            self.d[last_element] = indx
        
            self.lst.pop()
            del self.d[val]
            return True
        return False

    def getRandom(self) -> int:
        return choice(self.lst)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()