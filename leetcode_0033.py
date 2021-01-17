class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """ 
        Rotate the list from the target value to get back to the asceeding order list. 
        Maybe the target is in the list, but it is not the rotate point.
        One of the two partitions must be ordered, whether the other is ordered is not sure.
        We can check whether the target is in the ordered partition.
        If the target is in the ordered partition, we focus on this part, the other part otherwise.
        """
        if len(nums) == 1 :
            if nums[0] != target:
                return -1
            else:
                return 0
        
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            # Check whether the right part is ordered.
            # If the right partition is ordered.
            elif nums[mid] < nums[right]:
                # Check whether the target is in the right (ordered) partition.
                if nums[mid] < target and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            # If the right partition is not ordered, namely the left partition is ordered.
            else:
                # Check whether the target is in the left (ordered) partition.
                if target < nums[mid] and nums[left] <= target:
                    right = mid -1
                else:
                    left = mid + 1
        return -1
