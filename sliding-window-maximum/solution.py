class Solution(object):

    def findMaxAndItsIndex(self, nums):
        maxnum = max(nums)
        return (maxnum, nums.index(maxnum))

    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        if len(nums) == 0:
            return []

        max_index = 0
        max_val = 0
        # NOTE: the worse case will be a decreasing input given

        ret = []
        for start_index in range(0, len(nums)-k+1):
            max_index = max_index - 1
            if max_index == -1:
                # do a full scan if we lost our maximum element
                max_val, max_index = self.findMaxAndItsIndex(nums[start_index:start_index+k])
            else:
                # check for incremental update
                newnum = nums[start_index+k-1]
                if newnum >= max_val:
                    max_val = newnum
                    max_index = k-1 # equals to len of the window
            ret.append(max_val)
        return ret

