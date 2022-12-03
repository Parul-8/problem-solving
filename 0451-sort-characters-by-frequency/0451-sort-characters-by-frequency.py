class Solution:
    def frequencySort(self, s: str) -> str:
        d1 = {}
        ans = ''
        for i in sorted(s):
            d1[i] = d1.get(i,0)+1
        sorted_d = dict( sorted(d1.items(),key=operator.itemgetter(1),reverse=True))        
        
        for i in sorted_d.items():
            for n in range(i[1],0,-1):
                ans = ans+i[0]
        
        return ans
                
        