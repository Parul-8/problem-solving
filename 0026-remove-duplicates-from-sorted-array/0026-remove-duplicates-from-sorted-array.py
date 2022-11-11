class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #Method 1
        ans = []
        for i in range(len(nums)):
            if ans and ans[-1] == nums[i]:
                nums[i] = 101 #since max limit given is 100
                
            else:
                ans.append(nums[i])
                
        nums.sort()
        return len(ans)
                