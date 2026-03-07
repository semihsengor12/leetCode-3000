class Solution:
    def minFlips(self, s: str) -> int:


        ##llm help to keep the streak sorry
        n = len(s)
        # 1. Unroll the circle
        s = s + s 
        
        # 2. Build the only two possible valid targets
        target1 = []
        target2 = []
        for i in range(len(s)):
            target1.append('0' if i % 2 == 0 else '1')
            target2.append('1' if i % 2 == 0 else '0')
            
        ans = float('inf')
        diff1 = 0
        diff2 = 0
        
        # 3. The Sliding Window
        left = 0
        for right in range(len(s)):
            # Add the incoming character to our error counts if it mismatches
            if s[right] != target1[right]: diff1 += 1
            if s[right] != target2[right]: diff2 += 1
            
            # If our window is too large, drop the oldest character
            if right - left + 1 > n:
                if s[left] != target1[left]: diff1 -= 1
                if s[left] != target2[left]: diff2 -= 1
                left += 1
                
            # If we have exactly a full string's worth of characters, check the score
            if right - left + 1 == n:
                ans = min(ans, diff1, diff2)
                
        return ans