import unittest
import solution

class TestSolution(unittest.TestCase):
    maxDiff = None

    def test_case0(self):
        sol = solution.Solution()
        self.assertEqual(3, sol.coinChange([1, 2, 5], 11))
        self.assertEqual(-1, sol.coinChange([2], 3))
        self.assertEqual(0, sol.coinChange([1,3,5], 0))
        self.assertEqual(1, sol.coinChange([1,3,5], 1))
        self.assertEqual(21, sol.coinChange([19,28,176,112,30,260,491,128,70,137,253], 8539))

if __name__ == '__main__':
    unittest.main()
