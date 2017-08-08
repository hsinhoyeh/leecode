import unittest
import solution

class TestSolution(unittest.TestCase):
    def test_case0(self):
        sol = solution.Solution()
        got = sol.maxProfit([3,2,6,5,0,3])
        self.assertEqual(4, got)

    def test_case1(self):
        sol = solution.Solution()
        got = sol.maxProfit([7, 1, 5, 3, 6, 4])
        self.assertEqual(5, got)

if __name__ == '__main__':
    unittest.main()
