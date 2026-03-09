class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        ## llm for streak
        MOD = 10**9 + 7
        
        # Initialize a 3D DP table with zeros
        # dp[i][j][0] tracks valid arrays ending in a 0
        # dp[i][j][1] tracks valid arrays ending in a 1
        dp = [[[0, 0] for _ in range(one + 1)] for _ in range(zero + 1)]
        
        # --- Base Cases ---
        # Arrays purely made of 0s (We can only build these up to the limit)
        for i in range(1, min(zero, limit) + 1):
            dp[i][0][0] = 1
            
        # Arrays purely made of 1s (We can only build these up to the limit)
        for j in range(1, min(one, limit) + 1):
            dp[0][j][1] = 1
            
        # --- The DP Transitions ---
        for i in range(1, zero + 1):
            for j in range(1, one + 1):
                
                # 1. Calculating valid arrays ending in 0
                # Standard transition: add a 0 to previous valid arrays
                dp[i][j][0] = (dp[i - 1][j][0] + dp[i - 1][j][1]) % MOD
                
                # Subtract out the specific arrays that just formed exactly (limit + 1) zeros
                if i > limit:
                    dp[i][j][0] = (dp[i][j][0] - dp[i - 1 - limit][j][1] + MOD) % MOD
                    
                # 2. Calculating valid arrays ending in 1
                # Standard transition: add a 1 to previous valid arrays
                dp[i][j][1] = (dp[i][j - 1][0] + dp[i][j - 1][1]) % MOD
                
                # Subtract out the specific arrays that just formed exactly (limit + 1) ones
                if j > limit:
                    dp[i][j][1] = (dp[i][j][1] - dp[i][j - 1 - limit][0] + MOD) % MOD
                    
        # The final answer is the sum of valid arrays ending in 0 and ending in 1
        return (dp[zero][one][0] + dp[zero][one][1]) % MOD