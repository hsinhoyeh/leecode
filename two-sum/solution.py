class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # hash is keyed with num and value is a slice of indices
        hash = {}
        for index in range(0, len(nums)):
            if nums[index] not in hash:
                hash[nums[index]] = [index + 1]
            else:
                hash[nums[index]].append(index+1)

        snums = sorted(nums)

        first = 0
        second = len(nums)-1 # at the end of array

        while True:
            first_num = snums[first]
            second_num = snums[second]
            estimated = first_num + second_num
            if estimated > target:
                second = second - 1
            elif estimated < target:
                first = first + 1
            else:
                if first_num == second_num:
                    return hash[first_num] # quiz has assumed that we have exact one solution
                return sorted([hash[snums[first]][0], hash[snums[second]][0] ])# non-zero index with order

            if first == len(nums) or second == 0:
                return []


