class Solution:
    def minPartitions(self, n: str) -> int:
        for s in "987654321":
            if s in n:
                return int(s)