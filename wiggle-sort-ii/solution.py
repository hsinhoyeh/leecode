class Solution(object):
    # having median value by sorting will cost the time complexity to o(nlogn)
    # but there are plenty of replacements, so we won't worry about that
    def median(self, lst):
        lst = sorted(lst)
        if len(lst) < 1:
                return None
        if len(lst) %2 == 1:
                return lst[((len(lst)+1)/2)-1]
        else:
                return float(sum(lst[(len(lst)/2)-1:(len(lst)/2)+1]))/2.0
    def pivot(self, nums):
        return self.median(nums)

    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        p_value = self.pivot(nums)

        # having a v_index will make the index access easier
        # which provides the following mapping
        # v(0) = 1
        # v(1) = 3
        # v(2) = 5
        # v(3) = 7
        # v(4) = 0
        # v(5) = 2
        # v(6) = 4
        # v(7) = 6
        # v(8) = 8
        def v_index(i):
            n = len(nums)
            return (1+2*(i)) % (n|1)

        first=0 # > median
        mid=0 # == median
        last = len(nums)-1

        while mid <= last:
            if nums[v_index(mid)] > p_value:
                nums[v_index(first)], nums[v_index(mid)] = nums[v_index(mid)], nums[v_index(first)]
                first = first +1
                mid = mid +1
            elif nums[v_index(mid)] < p_value:
                nums[v_index(mid)], nums[v_index(last)] = nums[v_index(last)], nums[v_index(mid)]
                last = last -1
            else:
                mid = mid +1
