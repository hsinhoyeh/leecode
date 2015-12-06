import unittest
import solution

class TestSolution(unittest.TestCase):
    def test_case0(self):
        sol = solution.Solution()
        self.assertEqual(False, sol.isAdditiveNumber("1"))
        self.assertEqual(True, sol.isAdditiveNumber("112358"))
        self.assertEqual(True, sol.isAdditiveNumber("199100199"))
        self.assertEqual(False, sol.isAdditiveNumber("0235813"))
        self.assertEqual(True, sol.isAdditiveNumber("12122436"))
        self.assertEqual(True, sol.isAdditiveNumber("101"))
        self.assertEqual(True, sol.isAdditiveNumber("111122335588143"))

if __name__ == '__main__':
    unittest.main()
