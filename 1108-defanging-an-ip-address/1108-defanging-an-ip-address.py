class Solution:
    def defangIPaddr(self, address: str) -> str:
        l = list(address)
        ans = []
        for i in l:
            if i == '.':
                ans.append('[.]')
                
            else:
                ans.append(i)
        return ''.join(ans)
        