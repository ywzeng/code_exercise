class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """ Double pointers. One starts from the head, the other starts from the tail. """
        left, right = 0, len(numbers)-1
        while left < right:
            temp_sum = numbers[left] + numbers[right]
            if temp_sum == target:
                return [left+1, right+1]
            elif temp_sum < target:
                left += 1
            else:
                right -= 1
