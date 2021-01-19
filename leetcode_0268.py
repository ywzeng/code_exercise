class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """ 
        Gauss Summation Formula: (0+1+2+...+n) = n(n+1)/2
        Base on this formula, we can get the sum of the nums, and then use n(n+1)/2 to minus the sum, and the result is the missing number.
        """
        missing_num = int(len(nums)*(len(nums)+1)/2 - sum(nums))
        return missing_num
