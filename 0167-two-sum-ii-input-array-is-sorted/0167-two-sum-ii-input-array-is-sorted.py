class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        d = {}
        
        for i in range(len(numbers)):
            first_num = numbers[i]
            second_num = target - first_num
            if first_num in d:
                return [d[first_num],i+1]
            else: 
                d[second_num] = i+1
            
            
        