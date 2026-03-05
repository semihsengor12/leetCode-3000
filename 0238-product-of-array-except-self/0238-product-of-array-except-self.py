class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1]*n
        product = 1
        for i in range(n):
            ans[i] = product
            product *= nums[i]
        right_p = 1
        for i in range(n-1,-1,-1):
            ans[i] *= right_p
            right_p *= nums[i]

            
        return ans
