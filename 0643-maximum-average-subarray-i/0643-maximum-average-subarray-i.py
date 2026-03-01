class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        if len(nums) < k:
            return 0.0
        

        left = 0
        current_sum = 0
        minimum = float('-inf')

        for i in range(len(nums)):
            current_sum += nums[i]

            if i - left +1 > k:
                current_sum -= nums[left]
                left += 1
            if i - left+1 == k:
                minimum = max(minimum, current_sum/k)
        
        return minimum