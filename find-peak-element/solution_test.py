import unittest
import solution

class TestSolution(unittest.TestCase):
    def test_case0(self):
        sol = solution.Solution()
        self.assertEqual(2, sol.findPeakElement([1, 2, 3, 1]))

if __name__ == '__main__':
    unittest.main()
