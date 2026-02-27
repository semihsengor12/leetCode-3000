class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) -1

        def boundFind(flag):
            left = 0
            bound= -1
            right = len(nums) -1
            while left <= right:
                mid = (left+right) //2
                if nums[mid] == target:
                    bound = mid
                    if flag:
                        right = mid -1
                    else:
                        left = mid + 1 
                elif nums[mid] > target:
                    right = mid -1
                else:
                    left = mid +1 
            return bound
        
        leftBound = boundFind(True)
        if leftBound == -1:
            return [-1, -1]
        rightBound = boundFind(False)
        

        return [leftBound, rightBound]