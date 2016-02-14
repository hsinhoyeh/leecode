class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return self.find_k_th(nums, k)

    def find_k_th(self, nums, k):
        if len(nums) ==1:
            return nums[0]

        pivot = nums[-1] # use the last element as pivot

        # reorder the nums so that larger-than-pivots > pivot > smaller-than-pivot
        left = 0
        right = len(nums)-1
        while True:
            while left < right and nums[left] > pivot:
                left = left +1
            while right > left and nums[right] <= pivot: # last element is always untouched.
                right = right -1
            if right == left:
                break
            # swap
            nums[left], nums[right] = nums[right], nums[left]

        # swap with pivot
        nums[left], nums[-1] = nums[-1], nums[left]
        if k == left +1:
            return nums[left]
        else:
            if k > left+1:
                return self.find_k_th(nums[left+1:], k-left-1)
            return self.find_k_th(nums[:left], k) # reduce one element per time, which should be worse case

