class Solution:
    def minPartitions(self, n: str) -> int:
        return max([int(i, 10) for i in n])