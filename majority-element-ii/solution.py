class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        if len(nums) < 1:
            return []

        # implement Boyer-Moore Algorithm
        candidate1 = None
        count1 = 0
        candidate2 = None
        count2 = 0
        for num in nums:
            if candidate1 == num:
                count1 = count1 + 1
            elif candidate2 == num:
                count2 = count2 + 1
            elif count1 == 0:
                candidate1 = num
                count1 = 1
            elif count2 == 0:
                candidate2 = num
                count2 = 1
            else:
                count1 = count1 -1
                count2 = count2 -1

        # post filtering
        return [c for c in set([candidate1, candidate2]) if float(nums.count(c)) > float(len(nums))/3.0]
