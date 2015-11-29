class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num < 10:
            return num

        left = 0
        while num > 0:
            left = left + num % 10
            num = int(num / 10)

        return self.addDigits(left)
