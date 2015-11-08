import unittest
import solution

class TestSolution(unittest.TestCase):
    def test_case0(self):
        sol = solution.Solution()
        self.assertEqual(0, sol.findMin([0]))

    def test_case2(self):
        sol = solution.Solution()
        self.assertEqual(0, sol.findMin([0, 1]))

    def test_case3(self):
        sol = solution.Solution()
        self.assertEqual(0, sol.findMin([1, 0]))

    def test_case4(self):
        sol = solution.Solution()
        self.assertEqual(0, sol.findMin([4, 5, 6, 7, 0, 1, 2]))

    def test_case5(self):
        sol = solution.Solution()
        self.assertEqual(0, sol.findMin([7, 6, 5, 4, 3, 2, 1, 0, 8]))

if __name__ == '__main__':
    unittest.main()
