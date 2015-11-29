class Solution(object):

    def num_count(self, nums):
        hash = {}
        for num in nums:
            self.hash_push(hash, num)
        return hash

    def hash_pop(self, hash, item):
        if item in hash and hash[item]==1:
            del hash[item]
        else:
            hash[item] = hash[item] - 1

    def hash_push(self, hash, item):
        if item not in hash:
            hash[item] = 1
        else:
            hash[item] = hash[item] + 1

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        rets = []
        setret = set()
        hash = self.num_count(nums)

        for first_index in range(0, len(nums)):
            # pop "first", so hash can represent the subspace of [nums] without "first"
            first = nums[first_index]
            self.hash_pop(hash, first)

            # clone a hash, so we can keep project the subspace
            dup_hash = dict(hash)

            for second_index in range(first_index+1, len(nums)):
                second = nums[second_index]
                left = 0 - first - second

                self.hash_pop(dup_hash, second)
                tested = left in dup_hash
                if tested:
                    # force monotonical order
                    setret.add(tuple(sorted([first, second, left])))
        for val in setret:
            rets.append(list(val))
        return rets
