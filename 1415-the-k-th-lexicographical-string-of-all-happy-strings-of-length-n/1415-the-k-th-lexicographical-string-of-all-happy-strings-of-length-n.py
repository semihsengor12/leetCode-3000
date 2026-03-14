class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        result = []
        
        def backtrack(current: str) -> bool:
            if len(current) == n:
                result.append(current)
                return len(result) == k  # Stop early once we hit the kth string
            
            for char in ['a', 'b', 'c']:
                if current and current[-1] == char:
                    continue  # Skip — would create adjacent duplicate
                if backtrack(current + char):
                    return True  # Propagate early exit
            
            return False
        
        backtrack("")
        return result[k - 1] if len(result) >= k else ""