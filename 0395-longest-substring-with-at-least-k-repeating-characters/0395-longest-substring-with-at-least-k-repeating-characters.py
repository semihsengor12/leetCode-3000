class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        maks = float('-inf')
        freq = dict()
        for i in s:
            freq[i] = freq.get(i,0) + 1
        

        for char, count in freq.items():
            if count < k:
                stringList = s.split(char)
                for i in stringList:
                    maks = max(self.longestSubstring(i,k), maks)

                return maks

        return len(s)

