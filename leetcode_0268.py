class Solution_Gauss_Summation_Formula:
    def missingNumber(self, nums: List[int]) -> int:
        """ 
        Gauss Summation Formula: (0+1+2+...+n) = n(n+1)/2
        Base on this formula, we can get the sum of the nums, and then use n(n+1)/2 to minus the sum, and the result is the missing number.
        """
        missing_num = int(len(nums)*(len(nums)+1)/2 - sum(nums))
        return missing_num

    
class Solution_XOR:
    def missingNumber(self, nums: List[int]) -> int:
        """
        Use XOR.
        Actually, applying exactly the same XOR operation twice on a number will not change that number.
        a XOR b XOR b == a.
        So, applying the XOR operation to the nums list by [0, len(nums)] will get the missing number.
        """
        missing_num = len(nums)
        for i in range(len(nums)):
            missing_num ^= i ^ nums[i]
        return missing_num
