class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        Convert the judge on specific numbers to the judge on the indexes.
        The smallest positive number not appear in the given list has only two cases:
            1). N+1; 
            2). The smallest number in [0: N].
        If the number in list are all unique positives and smaller than N+1, the answer of this question is actually (N+1);
        If the number in list are all positives and smaller than N+1, but there are duplicates, the answer of this question is the smallest number in [1: N] that not appear in the given list;
        If the number in list are not all positives, the answer must in [1: N].
        Besides, the question requires that the time-complexity must be O(n) and the space-complexity must be O(1), so we cannot use sort algorithm and exploit extra lists. 
        Basic ideas:
            1. If a number is not positive (<=0), we reset it to (N+1);
            2. If a number is in [1, N], we set the nums[number-1] to its negative-format.
        Finally, if all numbers are negative, the answer of this question is (N+1);
        Otherwise, the index of the first positive number is the answer of this question.
        """
        # Convert all negatives and zeros to (N+1).
        for i, num in enumerate(nums):
            if num <= 0:
                nums[i] = len(nums) + 1

        # Label the valid index to the negative-format.
        for i, num in enumerate(nums):
            num = abs(num)
            if 0 < num <= len(nums):
                nums[num-1] = -abs(nums[num-1])
        
        result_num = len(nums) + 1
        for i, num in enumerate(nums):
            if num > 0:
                result_num = i+1
                break
        return result_num
