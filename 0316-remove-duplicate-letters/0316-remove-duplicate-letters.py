class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        freq = dict()
        seen = set()
        for i in s:
            freq[i] = freq.get(i, 0) + 1
        
        for i in range(len(s)):
            char = s[i]
            freq[char] -= 1
            if char in seen:
                continue 
            while stack and stack[-1] > char and freq[stack[-1]] > 0:
                popped_c = stack.pop()
                seen.remove(popped_c)

            seen.add(char)
            stack.append(char)

        return "".join(stack)