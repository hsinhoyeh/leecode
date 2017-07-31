class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        # start from string tail
        rs = s[::-1]
        rt = t[::-1]
        rt_start = 0

        for i in range(0, len(rs)):
            pos = rt[rt_start:].find(rs[i])
            if pos == -1:
                return False
            rt_start = rt_start + pos +1
        return True
