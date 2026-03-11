class Solution:
    def bitwiseComplement(self, n: int) -> int:
        string = bin(n)[2::]
        count = 0
        print(string)
        for i in string:
            count *= 2
            if i == '0':
                count += 1
        
        return count



        
        return unsigned