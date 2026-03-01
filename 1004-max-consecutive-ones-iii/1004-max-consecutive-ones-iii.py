class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left_p = 0
        maks = 0
        queue = deque()
        for i in range(len(nums)): 
            if nums[i] == 0:
                queue.append(i)
 
            if len(queue) > k:
                oldest_zero_index = queue.popleft()
                left_p = oldest_zero_index + 1
                
            maks = max(maks, i - left_p + 1)
        return maks