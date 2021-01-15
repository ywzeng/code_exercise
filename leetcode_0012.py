class Solution:
    def intToRoman(self, num: int) -> str:
        num_list = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        roman_list = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        
        result_str = ''
        for i in range(len(num_list)):
            while num >= num_list[i]:
                result_str += roman_list[i]
                num -= num_list[i]

        return result_str
