import unittest
import solution

class TestSolution(unittest.TestCase):
    def test_case0(self):
        sol = solution.Solution()
        self.assertEqual(True, sol.isHappy(19))
        self.assertEqual(True, sol.isHappy(10))
        self.assertEqual(False, sol.isHappy(2))
        self.assertEqual(True, sol.isHappy(13))
 
if __name__ == '__main__':
    unittest.main()
