class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip(' ')
        if len(s) == 0:
            return 0
        result = ''
        # 1. The first character is '+' or '-'.
        is_minus = False
        if ord(s[0]) in [43, 45]:
            if ord(s[0]) == 45:
                is_minus = True
            for c in s[1:]:
                if ord(c) not in range(48, 58):
                    break
                result += c
        # 2. The first character is digit.
        elif ord(s[0]) in range(48, 58):
            result += s[0]
            for c in s[1:]:
                if ord(c) not in range(48, 58):
                    break
                result += c
        if result:
            result = int(result) if not is_minus else -int(result)
            if result < -pow(2, 31):
                return -pow(2, 31)
            elif result > pow(2, 31)-1:
                return pow(2, 31)-1
            else:
                return result
        else:
            return 0
