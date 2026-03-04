class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        row = len(mat)
        col = len(mat[0])
        rows = [0]*row
        columns = [0]*col
        for i in range((row)):
            for j in range((col)):
                if mat[i][j] == 1:
                    rows[i] += 1
                    columns[j] += 1
        total = 0
        
        for i in range(row):
            if rows[i] != 1:
                continue
            for j in range(col):
                if columns[j] != 1:
                    continue
                if mat[i][j] == 1:
                    total +=1
        


        return total
                
 
