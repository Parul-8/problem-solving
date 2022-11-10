class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ans = []
        for i in range(len(nums)):
            if nums[i] == val:
                nums[i] = -1
            else:
                ans.append(nums[i])
                
        nums.sort(reverse=True)
        
        return len(ans)
                