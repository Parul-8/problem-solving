class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        d = {}
        for i in range(len(nums)):
            #n = nums[i]
            second = target - nums[i]
            if nums[i] in d:
                return [d[nums[i]],i]
            else:
                d[second] = i #storing (target - currentNumber) in dict as key and index of                               #current number as value in dict
        
        
        
        