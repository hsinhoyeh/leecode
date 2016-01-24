import unittest
import solution

class TestSolution(unittest.TestCase):
    def test_case0(self):
        sol = solution.Solution()
        self.assertEqual(True,
            sol.searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]],5))

        self.assertEqual(False,
            sol.searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]],20))


if __name__ == '__main__':
    unittest.main()
