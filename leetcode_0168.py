class Solution:
    def convertToTitle(self, n: int) -> str:
        res = []
        while n > 0:
            n -= 1
            remainder = n % 26
            res += [chr(remainder+65)]
            n = n // 26
        return ''.join(res[::-1])
