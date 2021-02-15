class Solution:
    def addDigits(self, num: int) -> int:
        if num < 10:
            return num
        else:
            temp_num = 0
            while num > 0:
                temp_num += num % 10
                num //= 10
            return self.addDigits(temp_num)
