class Solution:
    def reverse(self, x: int) -> int:
        reverse_num = 0
        is_minus = False
        if x < 0:
            is_minus = True
            x = abs(x)
        while x != 0:
            reverse_num = x % 10 + reverse_num * 10
            x = x // 10
        reverse_num = reverse_num if not is_minus else -reverse_num
        if reverse_num < pow(-2, 31) or reverse_num > pow(2, 31)-1:
            return 0
        else:
            return reverse_num
