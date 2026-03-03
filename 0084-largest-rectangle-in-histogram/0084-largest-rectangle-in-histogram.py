class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights:
            return 0 

        stack = []
        heights.append(0) 
        maks = 0
        
        for i in range(len(heights)):
            current_height = heights[i]
            start_index = i 
            
            while stack and current_height < stack[-1][0]:
                popped_height, popped_index = stack.pop()
                
                width = i - popped_index
                maks = max(maks, popped_height * width)
                

                start_index = popped_index
                
            stack.append([current_height, start_index])
            
        return maks
            
