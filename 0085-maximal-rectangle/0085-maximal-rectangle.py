class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        
        def largestRectangleArea(heights: List[int]) -> int:
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
        maks = 0
        prev = [0]*len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '0':
                    prev[j] = 0
                else:
                    prev[j] += 1
            maks = max(maks, largestRectangleArea(prev))
        return maks

        