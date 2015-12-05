import unittest
import solution

class TestSolution(unittest.TestCase):

    def test_case0(self):
        sol = solution.Solution()
        self.assertEqual(
            [0],
            sol.grayCode(0))

        self.assertEqual(
            [0, 1, 3, 2],
            sol.grayCode(2))

        self.assertEqual(
            [0, 1, 3, 2, 6, 7, 5, 4],
            sol.grayCode(3))

if __name__ == '__main__':
    unittest.main()
