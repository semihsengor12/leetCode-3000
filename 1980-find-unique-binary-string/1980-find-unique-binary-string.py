class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        ##llm for streak 
        ans = []
        for i in range(len(nums)):
            # If the i-th character of the i-th string is '0', use '1'
            # If it is '1', use '0'
            if nums[i][i] == '0':
                ans.append('1')
            else:
                ans.append('0')
                
        return "".join(ans)