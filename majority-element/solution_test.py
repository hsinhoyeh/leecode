import unittest
import solution

class TestSolution(unittest.TestCase):
    def test_case0(self):
        sol = solution.Solution()
        got = sol.majorityElement([1, 0, 0, 0, -2, 2])
        expect = 0
        self.assertEqual(expect, got)

if __name__ == '__main__':
    unittest.main()
