import math

class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 0:
            return [0]

        ret = []
        for c in range(1, n+1): #[1, n+1)
            if c == 1:
                ret = [0, 1]
                continue

            # get previous state
            prev_lst = list(ret)
            prev_lst.reverse()
            base = int(math.pow(2, c-1))
            result_lst = list(ret)
            for ele in prev_lst:
                result_lst.append(ele + base)
            ret = result_lst
        return ret
