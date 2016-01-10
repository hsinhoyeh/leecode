class Solution(object):
    def inRange(self, target, lower, upper):
        if target >= lower and target <= upper:
            return True
        return False

    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        if len(nums) < 1:
            return 0

        bound_results = 0
        last_combined_results = []
        for num in nums:
            if last_combined_results:
                for index in range(0, len(last_combined_results)):
                    middle_result = last_combined_results[index] + num
                    last_combined_results[index] = middle_result
                    if self.inRange(middle_result, lower, upper):
                        bound_results = bound_results + 1
            if self.inRange(num, lower, upper):
                bound_results = bound_results + 1
            last_combined_results.append(num)
        return bound_results
