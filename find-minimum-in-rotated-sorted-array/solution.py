#!/bin/python
class Solution(object):

    def find_min_2(self, nums):
        if nums[0] > nums[1]:
            return nums[1]
        return nums[0]

    def duplicate_finder(self, pivot):
        def exitOnDuplicated(num):
            if pivot == num:
                return True
            return False
        return exitOnDuplicated

    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return -1 # unable to handle
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return self.find_min_2(nums)

        # elements >= 3
        exit_when_deprecated = self.duplicate_finder(nums[0])
        minp = nums[0]

        for idx in range(1, len(nums)):
            val = nums[idx]
            if exit_when_deprecated(val):
                return minp
            if minp > val:
                minp = val
        return minp

