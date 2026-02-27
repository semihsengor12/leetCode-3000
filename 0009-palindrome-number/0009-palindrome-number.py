class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x < 10:
            return True
        result = []

        while x:
            dig = x % 10
            result.append(dig)
            x = x // 10
        return result == result[::-1]