class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        total = 0
        left_p = 0
        mins = float('inf')
        for i in range(len(nums)):
            total += nums[i]

            while total >= target:
                mins = min(mins, i-left_p+1)
                total -= nums[left_p]
                left_p += 1
            if mins == 1:
                return 1
    

        return mins if mins != float('inf') else 0