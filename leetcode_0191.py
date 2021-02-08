class Solution:
    def hammingWeight(self, n: int) -> int:
        """ Bit calculation. """
        count = 0
        while n:
            # 0000111 & 1 is 1
            # 0000110 & 1 is 0
            temp = n & 1
            count += temp
            n = n >> 1
        return count
