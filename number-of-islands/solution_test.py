import unittest

from collections import deque

import solution

class TestSolution(unittest.TestCase):
    def test_case0(self):
        sol = solution.Solution()
        got = sol.numIslands(["11110","11010","11000","00000"])
        self.assertEqual(1, got)

    def test_case1(self):
        sol = solution.Solution()
        got = sol.numIslands(["11000","11000","00100","00011"])
        self.assertEqual(3, got)

    def test_case2(self):
        sol = solution.Solution()
        got = sol.numIslands(["111","010","111"])
        self.assertEqual(1, got)



if __name__ == '__main__':
    unittest.main()
