import unittest
import solution

class TestSolution(unittest.TestCase):

    def test_case0(self):
        sol = solution.Solution()
        got = sol.isSubsequence("ace", "abcde")
        self.assertEqual(True, got)

if __name__ == '__main__':
    unittest.main()
