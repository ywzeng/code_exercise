class Solution:
    def titleToNumber(self, s: str) -> int:
        """ Convert 26 to 10. """
        res = 0
        for i, c in enumerate(s[::-1]):
            # ord(c) - 65 + 1
            res += (ord(c) - 64) * 26**i
        return res
