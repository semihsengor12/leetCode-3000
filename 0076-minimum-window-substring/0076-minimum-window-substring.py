class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        freq = {}
        for char in t:
            freq[char] = freq.get(char, 0) + 1

        need = len(freq)
        have = 0

        new_freq = {}
        left_p = 0
        
        best_coords = [-1, -1]
        min_len = float('inf')

        for i in range(len(s)):
            char = s[i]
            new_freq[char] = new_freq.get(char, 0) + 1

            if char in freq and new_freq[char] == freq[char]:
                have += 1

            while have == need:
                
                if (i - left_p + 1) < min_len:
                    min_len = (i - left_p + 1)
                    best_coords = [left_p, i]

                left_char = s[left_p]
                new_freq[left_char] -= 1

                if left_char in freq and new_freq[left_char] < freq[left_char]:
                    have -= 1
                
                left_p += 1

        l, r = best_coords
        return s[l : r+1] if min_len != float('inf') else ""