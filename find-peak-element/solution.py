class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        left, current, right = None, None, None
        for index in range(0, len(nums)):
            current = nums[index]
            if index == 0:
                left = None
            else:
                left = nums[index-1]
            if index == len(nums) -1:
                right = None
            else:
                right = nums[index+1]

            if left is None and current > right:
                return index
            if right is None and current > left:
                return index
            if current > left and current > right:
                return index
        return -1

