class Solution(object):
    def greatThan(self, lst1, lst2):
        return max(lst1, lst2) == lst1

    def keepLargestWithOrder(self, nums, keep_count):
        if len(nums) < keep_count:
            return ([], False)
        drop = len(nums) - keep_count
        out = []
        for num in nums:
            while drop and out and out[-1] < num:
                out.pop()
                drop -= 1
            out.append(num)
        return (out[:keep_count], True)

    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """

        largest = []
        for size1 in range(0, k+1):
            size2 = k - size1
            (fnums1, enough1) = self.keepLargestWithOrder(nums1, size1)
            (fnums2, enough2) = self.keepLargestWithOrder(nums2, size2)
            if not enough1 or not enough2:
                continue
            merged = self.merge(fnums1, fnums2, k)
            if self.greatThan(merged, largest):
                largest = merged
        return largest

    def merge(self, nums1, nums2, k):
        if not nums1 and not nums2:
            return []
        if len(nums1) + len(nums2) < k:
            return []
        # if nums1 = [0,9,6,9,2]
        # if nums2 = [0,2,4,2,2,1,6,6,5,3,6,2,9,6]
        # nums1 > nums2
        return [max(nums1, nums2).pop(0) for _ in nums1 + nums2]
