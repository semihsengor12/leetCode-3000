class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        total_steps = m + n -2
        
        return math.comb(total_steps, m-1)
        