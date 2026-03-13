class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        
        import math

        # Helper function to check if time T is sufficient
        def can_reduce_in_time(T: int) -> bool:
            total_reduced = 0
            for w in workerTimes:
                # Using the quadratic formula to find max height x this worker can reduce
                max_x = int((-1 + math.isqrt(1 + 8 * T // w)) // 2)
                total_reduced += max_x
                
                # Early exit if we already met the goal
                if total_reduced >= mountainHeight:
                    return True
            return False

        # Define the Binary Search boundaries
        low = 0
        # Worst case: the fastest single worker does the entire mountain alone
        min_w = min(workerTimes)
        high = min_w * mountainHeight * (mountainHeight + 1) // 2

        ans = high
        
        # Standard Binary Search template
        while low <= high:
            mid = (low + high) // 2
            
            if can_reduce_in_time(mid):
                ans = mid       # Record the valid time
                high = mid - 1  # Try to find a smaller valid time
            else:
                low = mid + 1   # We need more time
                
        return ans