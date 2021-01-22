class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        multiple_result = 0       # Cumulatively reocrd the multiple result.
        
        # From the low bit to high bit, namely from right to left.
        for i in range(len(num1)-1, -1, -1):
            bit_1 = ord(num1[i]) - ord('0')
            for j in range(len(num2)-1, -1, -1):
                bit_2 = ord(num2[j]) - ord('0')
                bit_result = (bit_1 * bit_2) * (10 ** (len(num2)-1-j+len(num1)-1-i))        # Determing the bit level of the multiple result based on the Multiple Vertical Law。
                multiple_result += bit_result
        return str(multiple_result)
