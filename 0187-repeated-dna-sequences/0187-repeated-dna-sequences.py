class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) < 10:
            return []
        freq = dict()
        left_p = 0
        right_p = 10

        while right_p <= len(s):
            freq[s[left_p:right_p:]] = freq.get(s[left_p:right_p:], 0) + 1
            right_p +=1
            left_p += 1
            
        return [seq for seq, count in freq.items() if count > 1]
