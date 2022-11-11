class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #Method 2
        new_index = 1
        for i in range(1,len(nums)):
            
            if nums[i] != nums[i-1]:
                nums[new_index] = nums[i]
                new_index = new_index + 1
        return new_index