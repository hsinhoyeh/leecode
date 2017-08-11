import unittest
import solution

class TestSolution(unittest.TestCase):
    def test_case0(self):
        sol = solution.Solution()
        got = sol.rob([1, 0, 1, 2, 1, 4])
        self.assertEqual(7, got)

    def test_case1(self):
        sol = solution.Solution()
        got = sol.rob([183,219,57,193,94,233,202,154,65,240,97,234,100,249,186,66,90,238,168,128,177,235,50,81,185,165,217,207,88,80,112,78,135,62,228,247,211])
        self.assertEqual(3365, got)

    def test_case2(self):
        sol = solution.Solution()
        got = sol.rob([155,44,52,58,250,225,109,118,211,73,137,96,137,89,174,66,134,26,25,205,239,85,146,73,55,6,122,196,128,50,61,230,94,208,46,243,105,81,157,89,205,78,249,203,238,239,217,212,241,242,157,79,133,66,36,165])
        self.assertEqual(4517, got)

if __name__ == '__main__':
    unittest.main()
