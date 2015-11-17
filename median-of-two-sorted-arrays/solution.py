class Solution(object):

    def median_of_list(self, nums1):
        lens = len(nums1)
        med = int(lens/2)
        if lens % 2 ==0:
            return float(nums1[med-1] + nums1[med]) / 2
        return nums1[med]

    def min(self, num1, num2):
        if num1 < num2:
            return num1
        return num2

    def kth_in_sorted_arrays(self, kth, nums1, nums2):
        long_lst = nums1
        short_lst = nums2
        if len(nums1) < len(nums2):
            short_lst = nums1
            long_lst = nums2

        # if short list is exhausted
        if len(short_lst) == 0:
            return long_lst[kth-1]

        if kth == 1:
            return self.min(short_lst[0], long_lst[0])

        # compare k/2th position of nums1 and nums2
        h1 = int(kth / 2)
        if kth%2 != 0:
            h1 = h1 + 1
        # adjust postion according to short list
        if len(short_lst) < h1:
            h1 = len(short_lst)

        r2 = kth - h1 # remains

        h1_index = h1-1 #convert to array index
        r2_index = r2-1
        if short_lst[h1_index] == long_lst[r2_index]:
            return short_lst[h1_index]
        if short_lst[h1_index] < long_lst[r2_index]:
            return self.kth_in_sorted_arrays(kth-h1, short_lst[h1:], long_lst)
        if short_lst[h1_index] > long_lst[r2_index]:
            return self.kth_in_sorted_arrays(kth-r2, short_lst, long_lst[r2:])

        # otherwise, no such case
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1) == 0 and len(nums2) == 0:
            return 0
        if len(nums1) == 0:
            return self.median_of_list(nums2)
        if len(nums2) == 0:
            return self.median_of_list(nums1)

        is_even = (len(nums1) + len(nums2))%2==0
        med_position = int((len(nums1) + len(nums2))/ 2)
        if is_even:
            v1 = self.kth_in_sorted_arrays(med_position, nums1, nums2)
            v2 = self.kth_in_sorted_arrays(med_position+1, nums1, nums2)
            return (float(v1+v2)/2)
        return self.kth_in_sorted_arrays(med_position+1, nums1, nums2)




