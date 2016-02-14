class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        max_product = nums[0]
        min_product = nums[0]
        current_max = max(max_product, min_product)

        for idx in range(1, len(nums)):
            temp_max = max_product * nums[idx]
            temp_min = min_product * nums[idx]
            max_product = max(max(temp_max, temp_min), nums[idx])
            min_product = min(min(temp_max, temp_min), nums[idx])
            current_max = max(current_max, max(max_product, min_product))

        return current_max
