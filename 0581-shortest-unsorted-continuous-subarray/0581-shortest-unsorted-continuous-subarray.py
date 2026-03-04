class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:

        ## help with an LLM
        n = len(nums)
        stack = []
        left_boundary = n
        right_boundary = -1
        
        for i in range(n):
            while stack and nums[stack[-1]] > nums[i]:
                popped_index = stack.pop()
                left_boundary = min(left_boundary, popped_index)
            stack.append(i)
            
        stack.clear()
        
        for i in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] < nums[i]:
                popped_index = stack.pop()
                right_boundary = max(right_boundary, popped_index)
            stack.append(i)
            
        if right_boundary - left_boundary < 0:
            return 0
            
        return right_boundary - left_boundary + 1