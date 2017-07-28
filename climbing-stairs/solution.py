class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        width = n + 1
        height = int(n/2) +2
        found = 0

        mp = [ [0 for x in range(width)] for y in range (height)]
        # init row0/col0
        for x in range(1, width):
            mp[0][x] = 1
        for y in range(1, height):
            mp[y][0] = 1

        for x in range (1, width):
            for y in range(1, height):
                val = y *2 + x
                if val <= n:
                    mp[y][x] = mp[y][x-1] + mp[y-1][x]
                if val == n:
                    found = found + mp[y][x]
                if val > n:
                    break
        if n %2 ==0:
            found = found +1
        return found + 1 # include all 1's
