class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        flag = False

        for i in s:
            if i == '0':
                flag = True
            elif i == '1' and flag:
                return False

        return True


        
