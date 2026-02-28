class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left = 0
        right = len(nums) - 1 

        while left <= right:
            mid = (left+right) // 2
            print(mid, left, right)
            if nums[mid] == target:
                return True
            if nums[right]==nums[mid]==nums[left]:
                left +=1
                right -= 1
                continue
            
            elif nums[mid] >= nums[left]: # left side is sorted
                if  nums[mid] > target >= nums[left]: 
                    right = mid -1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid +1
                else:
                    right = mid -1
        print(mid, left, right)

        return False