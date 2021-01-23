class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        Because nums1 and nums2 are all ordered lists, if nums2[j] is greater than nums1[i], then nums2[j:] are all greater than nums1[i].
        """
        nums1[:] = nums1[:m]        # Left value, nums[:] equals to the enumeration of nums[0], nums[1], ...
        compare_pointer = 0     # Move on the nums1 list.
        for num in nums2:
            while compare_pointer < len(nums1) and num >= nums1[compare_pointer]:
                compare_pointer += 1
            nums1.insert(compare_pointer, num)
            compare_pointer += 1
        print(nums1)
