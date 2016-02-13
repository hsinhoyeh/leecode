class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """

        # generate 1~n in a list
        nums = range(1, n+1)

        seq = self.pick_nth(nums, k-1)
        strseq = [str(n) for n in seq]
        return "".join(strseq)

    def get_n_perm(self, n):
        ret = 1
        for val in range(n, 0, -1):
            ret = ret * val
        return ret

    def pick_nth(self, nums, k):
        if k == 0:
            return nums

        ret = []
        while k > 0:
            n_perm = self.get_n_perm(len(nums)-1)
            leading_index = int(float(k) / float(n_perm))
            k = k % n_perm
            ret.append(nums[leading_index])
            nums.pop(leading_index)
        ret.extend(nums)
        return ret
