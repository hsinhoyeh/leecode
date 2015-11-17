import unittest
import solution

class TestSolution(unittest.TestCase):
    def test_case0(self):
        sol = solution.Solution()
        self.assertEqual(
                4,
                sol.longestConsecutive([100, 4, 200, 1, 3, 2]))

    def test_case1(self):
        sol = solution.Solution()
        self.assertEqual(
                1,
                sol.longestConsecutive([0]))

    def test_case2(self):
        sol = solution.Solution()
        self.assertEqual(
                2,
                sol.longestConsecutive([-1, 0]))

    def test_case3(self):
        sol = solution.Solution()
        self.assertEqual(
                3,
                sol.longestConsecutive([-1, 0, 1]))

    def test_case4(self):
        sol = solution.Solution()
        self.assertEqual(
                4,
                sol.longestConsecutive([-7,7,-6,6,-1,2,5,-5,-2,8]))

if __name__ == '__main__':
    unittest.main()
