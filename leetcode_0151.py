class Solution_Fuck:
    def reverseWords(self, s: str) -> str:
        return ' '.join(s.split()[::-1])


class Solution_Normal:
    def reverseWords(self, s: str) -> str:
        """ Stack. """
        stack = []
        left, right = 0, 0
        while left < len(s):
            if s[left] == ' ':
                left += 1
            else:
                right = left+ 1 
                while right < len(s) and s[right] != ' ':
                    right += 1
                stack += [s[left: right]]
                left = right + 1
        s = ' '.join(stack[::-1])
        return s
