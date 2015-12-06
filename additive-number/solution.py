import math

class NextNum(object):
    def __init__(self, num, start_index, max_len=None):
        self.num = num
        self.start_index = start_index
        self.end_index = start_index
        self.max_len = max_len
        self.last_val = None

    def next(self, nlen=1): # default, lookup the number with len=1
        # none of value is leading with 0
        # make sure that we won't go further
        if self.last_val == 0:
            return None
        self.last_val = self._next(nlen)
        return self.last_val

    def _next(self, nlen=1):
        self.end_index += nlen
        if self.end_index > len(self.num):
            return None

        if self.start_index > len(self.num):
            return None

        if self.max_len:
            if int(math.fabs(self.end_index - self.start_index)) > self.max_len:
                return None

        if self.num[self.start_index] == '0':
            return 0
        return int(self.num[self.start_index: self.end_index])

class Solution(object):
    def findDigits(self, anum):
        return int(math.log(anum, 10)) + 1

    # return the last index of found
    # otherwise, return None
    def findLast(self, num, lst_first_two_nums):
        sum_of_2 = sum(lst_first_two_nums)
        digits = self.findDigits(sum_of_2)
        nn2 = NextNum(num, 0)
        if nn2.next(digits) == sum_of_2:
            return nn2.end_index
        return None


    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        # fix the first two numbers
        # NOTE: the length of the first number and second shouldn't exceed n/2
        # since first + second = thrid.
        half_num = int(len(num)/2)
        nn0 = NextNum(num, 0, half_num)
        val0 = nn0.next()
        while val0 != None:
            # number 2 is start from the end of number 1
            nn1 = NextNum(num, nn0.end_index, half_num)
            val1 = nn1.next() 
            while val1 != None:
                digits = self.findDigits(val0 + val1)
                if len(num) < nn1.end_index + digits:
                    # no need to check
                    break
                index = self.findLast(num[nn1.end_index:], [val0, val1])
                if index:
                    index = index + nn1.end_index

                tval0, tval1 = val0, val1
                while index != len(num): # not end, we should keep looking
                    if index == None:
                        break
                    tval0, tval1 = tval1, tval0 + tval1
                    subindex = self.findLast(num[index:], [tval0, tval1])
                    if subindex:
                        index = index + subindex
                    else:
                        index = subindex
                if index == len(num):
                    return True
                val1 = nn1.next()
            val0 = nn0.next()
        return False
