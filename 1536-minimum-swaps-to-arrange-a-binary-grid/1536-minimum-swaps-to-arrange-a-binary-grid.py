class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        zeros = []
        
        for row in grid:
            count = 0
            for val in reversed(row):
                if val == 0:
                    count += 1
                else:
                    break
            zeros.append(count)
            
        swaps = 0
        
        for i in range(n):
            target = n - 1 - i 
            
            j = i
            while j < n and zeros[j] < target:
                j += 1
                
            if j == n:
                return -1
                
            while j > i:
                zeros[j], zeros[j-1] = zeros[j-1], zeros[j]
                swaps += 1
                j -= 1
                
        return swaps