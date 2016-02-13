import unittest
import solution

class TestSolution(unittest.TestCase):
    def test_case0(self):
        sol = solution.Solution()
        self.assertEqual(2, sol.searchInsert([1,3,5,6], 5))
        self.assertEqual(1, sol.searchInsert([1,3,5,6], 2))
        self.assertEqual(4, sol.searchInsert([1,3,5,6], 7))
        self.assertEqual(0, sol.searchInsert([1,3,5,6], 0))

if __name__ == '__main__':
    unittest.main()
