class Solution_1:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        original_num = x
        reversed_num = 0
        while x > 0:
            reversed_num = x % 10 + reversed_num * 10
            x = x // 10
        return reversed_num == original_num


class Solution__2:
    def isPalindrome(self, x: int) -> bool:
        """ Double points """
        if x < 0:
            return False
        x = str(x)
        start_index, end_index = 0, len(x)-1
        while start_index <= end_index:
            if x[start_index] != x[end_index]:
                return False
            start_index += 1
            end_index -= 1
        return True
