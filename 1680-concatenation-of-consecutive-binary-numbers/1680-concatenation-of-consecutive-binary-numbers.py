class Solution:
    def concatenatedBinary(self, n: int) -> int:
        total = 0
        total_digs = 0
        MOD = 10**9 +7
        for i in range(1, n+1):
            if i & (i-1) == 0:
                total_digs += 1
            total = ((total << total_digs) | i) % MOD

        return total        