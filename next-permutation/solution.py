class Solution(object):
    def reverse(self, nums, begin, end):
        while begin < end:
            nums[begin], nums[end] = nums[end], nums[begin]
            begin = begin +1
            end = end -1

    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # implement algorithm described in https://www.nayuki.io/page/next-lexicographical-permutation-algorithm


        #1. find the largest index where nums[i-1] < nums[i]
        wi_index=None
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                wi_index = i
        if wi_index == None:
            # no next permutation, should go to init permutation
            self.reverse(nums, 0, len(nums)-1)
            return

        #2. find the largest index where j >= i and nums[j] > nums[i-1]
        dc_index=0
        for j in range(len(nums)-1, wi_index-1, -1):
            if nums[j] > nums[wi_index-1]:
                dc_index = j
                break

        #3. swap
        nums[wi_index-1], nums[dc_index] = nums[dc_index], nums[wi_index-1]

        #4. reverse
        r_begin = wi_index
        r_end = len(nums)-1
        self.reverse(nums, r_begin, r_end)
