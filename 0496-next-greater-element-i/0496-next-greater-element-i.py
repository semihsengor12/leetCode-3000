class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        indices = dict()
        for i in range(len(nums2)):
            num = nums2[i]
            while stack and stack[-1] < num:
                popped_c = stack.pop()
                indices[popped_c] = num
            stack.append(num)
        
        res = []
        for i in nums1:
            res.append(indices.get(i, -1))

        return res