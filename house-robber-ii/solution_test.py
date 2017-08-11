import unittest
import solution

class TestSolution(unittest.TestCase):
    def test_case0(self):
        sol = solution.Solution()
        got = sol.rob([1,2,3,4])
        self.assertEqual(6, got)

    def test_case1(self):
        sol = solution.Solution()
        got = sol.rob([1,1,1])
        self.assertEqual(1, got)



if __name__ == '__main__':
    unittest.main()
