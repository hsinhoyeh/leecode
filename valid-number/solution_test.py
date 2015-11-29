import unittest
import solution

class TestSolution(unittest.TestCase):
    def test_case0(self):
        sol = solution.Solution()
        self.assertEqual(False, sol.isNumber("abc"))
        self.assertEqual(True, sol.isNumber(" 0.1"))
        self.assertEqual(True, sol.isNumber("2e10"))

if __name__ == '__main__':
    unittest.main()
