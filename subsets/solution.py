class Solution(object):
    def all_combinations(self, val, s):
        a_s = s.copy() # as is argumented set
        # first, add (val) itself
        a_s.add((val,))
        for ele in s:
            lst = list(ele)
            lst.append(val)
            lst.sort()
            a_s.add(tuple(lst))
        return a_s

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        s = set()
        s.add(())
        for num in nums:
            s = self.all_combinations(num, s)
        return list(s)

