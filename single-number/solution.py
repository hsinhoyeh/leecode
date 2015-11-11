class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 1:
            return -1

        base = nums[0]
        for idx in range(1, len(nums)):
            base ^= nums[idx]
        return base
