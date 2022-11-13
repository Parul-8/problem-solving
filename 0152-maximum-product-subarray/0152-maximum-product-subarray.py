class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        max_so_far = nums[0]
        min_so_far = nums[0]
        result = max_so_far
        for i in range(1,len(nums)):
            cur = nums[i]
            temp = max(cur, max_so_far*cur, min_so_far*cur)#using temp bcoz we will be                                                   #needing max_So_far for further calculation
            min_so_far = min(cur, max_so_far*cur, min_so_far*cur)
            
            max_so_far = temp
            
            result = max(result,max_so_far)
            
        return  result
            
            
        