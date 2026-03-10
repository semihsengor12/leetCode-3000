class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 10**9 + 7
        
        # dp[i][j][0] is arrays with i zeros, j ones, ending in 0
        # dp[i][j][1] is arrays with i zeros, j ones, ending in 1
        dp = [[[0, 0] for _ in range(one + 1)] for _ in range(zero + 1)]
        
        # Base Cases: Single blocks within the limit
        for i in range(min(zero, limit) + 1):
            dp[i][0][0] = 1
        for j in range(min(one, limit) + 1):
            dp[0][j][1] = 1
            
        for i in range(1, zero + 1):
            for j in range(1, one + 1):
                # Calculate dp[i][j][0]
                val0 = (dp[i-1][j][0] + dp[i-1][j][1]) % MOD
                if i > limit:
                    # Subtract cases where we added a 0 to a block that was already 'limit' long
                    val0 = (val0 - dp[i - limit - 1][j][1] + MOD) % MOD
                dp[i][j][0] = val0
                
                # Calculate dp[i][j][1]
                val1 = (dp[i][j-1][0] + dp[i][j-1][1]) % MOD
                if j > limit:
                    # Subtract cases where we added a 1 to a block that was already 'limit' long
                    val1 = (val1 - dp[i][j - limit - 1][0] + MOD) % MOD
                dp[i][j][1] = val1
                
        return (dp[zero][one][0] + dp[zero][one][1]) % MOD