class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # implement Boyer-Moore Algorithm
        candidate = None
        count = 0
        for num in nums:
            if candidate == num:
                count = count + 1
            elif count == 0:
                candidate = num
                count = 1
            else:
                count = count -1
        return candidate
