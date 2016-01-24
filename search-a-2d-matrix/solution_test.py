import unittest
import solution

class TestSolution(unittest.TestCase):
    def test_case0(self):
        sol = solution.Solution()
        self.assertEqual(True,sol.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]], 3))

if __name__ == '__main__':
    unittest.main()
