import unittest
import solution

class TestSolution(unittest.TestCase):
    def test_case0(self):
        sol = solution.Solution()
        got = sol.climbStairs(1)
        self.assertEqual(1, got)

    def test_case1(self):
        sol = solution.Solution()
        got = sol.climbStairs(3)
        self.assertEqual(3, got)

    def test_case2(self):
        sol = solution.Solution()
        got = sol.climbStairs(4)
        self.assertEqual(5, got)


    def test_case3(self):
        sol = solution.Solution()
        got = sol.climbStairs(5)
        self.assertEqual(8, got)



if __name__ == '__main__':
    unittest.main()
