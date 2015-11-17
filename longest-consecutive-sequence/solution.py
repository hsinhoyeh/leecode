class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hash = {}
        for num in nums:
            hash[num] = False

        bound_maximum = len(nums)
        max_consecutive_count = 1
        # keys is an ordered list
        for key in hash.keys():
            consecutive_count = 1
            # test right continue(i.e. positive)
            rc = True
            rc_key = key
            while rc:
                if (rc_key +1) not in hash:
                    rc = False
                    continue
                rc_key = rc_key + 1
                consecutive_count += 1

            # test left continue(i.e. negative)
            lc = True
            lc_key = key
            while lc:
                if (lc_key -1) not in hash:
                    lc = False
                    continue
                lc_key = lc_key - 1
                consecutive_count += 1

            # update
            if consecutive_count > max_consecutive_count:
                max_consecutive_count = consecutive_count

            # earily return: if max_len == the remain #keys (logical maximum bound)
            if max_consecutive_count == bound_maximum:
                return max_consecutive_count

            # minus 1 since we keep forward on the key space
            bound_maximum -= 1
        return max_consecutive_count

