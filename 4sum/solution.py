class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        if len(nums) < 4:
            return []

        snums = sorted(nums)

        count = {} # used for pruning
        for num in snums:
            if num not in count:
                count[num] = 0
            count[num] = count[num] + 1

        # build a cache which keyed as sum of two integer and value is the possiblity tuple
        cache = {}
        for i in range(0, len(snums)):
            for j in range(i+1, len(snums)):
                ival = snums[i]
                jval = snums[j]
                keyed = ival + jval
                if keyed not in cache:
                    cache[keyed] = []
                cache[keyed].append((ival, jval))

        rset = set()
        # then go over the keys in cache twice
        for ki in cache.keys():
            kj = target - ki
            if kj not in cache:
                continue
            # evaluate possible tuples
            for ti in cache[ki]:
                for tj in cache[kj]:
                    t_candidate = ti + tj
                    if not self.isSubset(t_candidate, count):
                        continue
                    # merge tuple and push to result set
                    # we use set to avoid duplicate set
                    rset.add(tuple(sorted(t_candidate)))

        ret = []
        for rele in rset:
            ret.append(list(rele))
        return ret


    def isSubset(self, tuple_candidate, count_map):
        # clone a count map
        c = dict(count_map)
        for ele in tuple_candidate:
            if ele not in c:
                return False

            if c[ele] <= 0:
                return False
            c[ele] = c[ele] - 1
        return True

