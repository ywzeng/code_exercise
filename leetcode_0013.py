class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100, 
                        'XC': 90, 'L': 50, 'XL': 40, 'X': 10, 'IX': 9, 
                        'V': 5, 'IV': 4, 'I': 1}

        result_num = 0
        i = 0
        while i < len(s):
            if i < len(s)-1 and roman_dict[s[i]] < roman_dict[s[i+1]]:
                result_num += roman_dict[s[i]+s[i+1]]
                i += 2
                continue
            result_num += roman_dict[s[i]]
            i += 1
        return result_num
