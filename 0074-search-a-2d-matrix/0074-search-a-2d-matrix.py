class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        columns = len(matrix[0])
        rows = len(matrix)
        left = 0
        right = rows-1

        while left < right:
            mid = (left+right)//2 

            if target > matrix[mid][-1]:
                left = mid +1
            else:
                right = mid
        if matrix[left][0] > target:
            return False
        newArea = matrix[left]
        left = 0
        right = columns-1
        while left <= right:
            mid = (left+right)//2
            if newArea[mid] == target:
                return True
            elif target > newArea[mid]:
                left = mid +1
            else:
                right = mid -1
        return False

        
