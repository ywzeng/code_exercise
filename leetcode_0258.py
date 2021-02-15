class Solution_Math:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        else:
            return num%9 if num%9 != 0 else 9

        
class Solution_Stupid:
    def addDigits(self, num: int) -> int:
        if num < 10:
            return num
        else:
            temp_num = 0
            while num > 0:
                temp_num += num % 10
                num //= 10
            return self.addDigits(temp_num)
