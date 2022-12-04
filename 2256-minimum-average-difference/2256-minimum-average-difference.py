class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        # diff = a1 - a2
        # a1 = (sum of numbers from index 0 to i) /(i+1)
        # a2 = (sum of numbers from index i+1 to n-1)/(n-i-1)
        
        n = len(nums)
        leftSum = 0
        totalSum = sum(nums)
        ans = [inf,inf]
        
        for i,v in enumerate(nums):
            leftSum += v
            
            leftAvg = leftSum // (i+1)
            rightSum = totalSum - leftSum 
            rightAvg = rightSum //(n-i-1) if (n-i-1) != 0 else 0
            
            abs_avg = abs(leftAvg-rightAvg)
            print(abs_avg)
            
            ans = min(ans,[abs_avg,i])
            
        return ans[1]
        