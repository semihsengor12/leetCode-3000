class Solution:
    def minOperations(self, s: str) -> int:
        "010101010101..." or "10101010101010..." 
        try1 = 0
        try2 = 0
        for i in range(len((s))):
            if i % 2 == 0:
                if s[i] == '0':
                    try2 += 1
                else:
                    try1 += 1

            else:
                if s[i] == '0':
                    try1 += 1
                else:
                    try2 += 1
        return min(try1, try2)