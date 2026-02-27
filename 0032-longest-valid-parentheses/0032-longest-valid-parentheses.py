class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        maxL = 0

        for i in range(len(s)):
            char = s[i]
            
            if char == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                currentL = i - stack[-1]
                maxL = max(maxL, currentL)

        return maxL
        
        
        