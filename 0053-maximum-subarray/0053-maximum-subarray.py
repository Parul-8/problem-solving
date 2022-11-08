class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum = 0
        cur_sum = 0
        maxsum_sofar = nums[0]
        for j in range(len(nums)):
            cur_sum = cur_sum + nums[j]
            maxsum_sofar = max(maxsum_sofar,cur_sum)
            if(cur_sum<0):
                cur_sum = 0
        return maxsum_sofar
            
            
            
            