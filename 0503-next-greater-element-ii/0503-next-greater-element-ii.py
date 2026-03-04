class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [-1] * n
        stack = [] 
        
        for i in range(2 * n):
            current_index = i % n 
            current_val = nums[current_index]
            
            while stack and current_val > nums[stack[-1]]:
                popped_index = stack.pop()
                ans[popped_index] = current_val
                
            if i < n:
                stack.append(current_index)
                
        return ans