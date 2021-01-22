class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] += 1
        carry = True if digits[-1] >= 10 else False
        carry_bit_index = len(digits)-1
        while carry:
            digits[carry_bit_index] -= 10
            if carry_bit_index == 0:
                digits.insert(0, 1)
                break
            carry_bit_index -= 1
            digits[carry_bit_index] += 1
            carry = True if digits[carry_bit_index] >= 10 else False
        return digits
