class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        
        def recursive_iter(current_n, S):
            if current_n == n:
                return S[k - 1] 
            
            inverted = "".join('1' if bit == '0' else '0' for bit in S)
            reversed_inverted = inverted[::-1]

            return recursive_iter(current_n + 1, S + "1" + reversed_inverted)

        return recursive_iter(1, "0")
            