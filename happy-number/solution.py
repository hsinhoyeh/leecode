class Solution(object):

    seen = {}
    def testHappy(self, n):
        left = 0
        while n > 0:
            a = n % 10
            left = left + a * a
            n = int(n / 10)
        return left

    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        left = n
        while True:
            left = self.testHappy(left)
            if left == 1:
                return True
            if left in self.seen:
                return False
            self.seen[left] = True
