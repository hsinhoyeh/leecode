import unittest
import solution

class TestSolution(unittest.TestCase):
    def test_case0(self):
        sol = solution.Solution()
        self.assertEqual(-2, sol.maxProduct([-2]))
        self.assertEqual(2, sol.maxProduct([0,2]))
        self.assertEqual(6, sol.maxProduct([2,3,-2,4]))
        self.assertEqual(80, sol.maxProduct([2,-5,-2,4]))
        self.assertEqual(24, sol.maxProduct([-2,3,-4]))
        self.assertEqual(108, sol.maxProduct([-1,-2,-9,-6]))

if __name__ == '__main__':
    unittest.main()
