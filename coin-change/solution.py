import sys

class Solution(object):
    invalid_int = sys.maxint -1

    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # will amount will be too large?
        if amount == 0:
            return 0

        T = [self.invalid_int for x in range(amount+1)] # include 0
        T[0] = 0

        for i in range(0, len(coins)):
            for j in range(0, amount+1):
                if j >= coins[i]:
                    T[j] = min(T[j], 1 + T[j-coins[i]])

        if T[amount] == self.invalid_int:
            return -1
        return T[amount]

