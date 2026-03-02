class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0
        count = 0

        for i in range(k):
            if s[i] in "aeiou":
                count += 1
        maks = count

        for i in range(k,  len(s)):
            if s[i-k] in "aeiou":
                count -= 1
            if s[i] in "aeiou":
                count += 1
            maks = max(maks, count)

        return maks