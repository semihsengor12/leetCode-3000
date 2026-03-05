class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainder_map = {0: -1} 
        running_sum = 0
        
        for i in range(len(nums)):
            running_sum += nums[i]
            
            remainder = running_sum % k
            
            if remainder in remainder_map:
                if i - remainder_map[remainder] >= 2:
                    return True
            else:
                remainder_map[remainder] = i
                
        return False
        
