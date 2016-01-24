import unittest
import solution

class TestSolution(unittest.TestCase):
    def test_case0(self):
        sol = solution.Solution()

        got = sol.majorityElement([])
        self.assertEqual(0, len(got))

        got = sol.majorityElement([1])
        expect = [1]
        self.assertEqual(sorted(expect), sorted(got))

        got = sol.majorityElement([2, 2])
        expect = [2]
        self.assertEqual(sorted(expect), sorted(got))

        got = sol.majorityElement([1, 2])
        expect = [1, 2]
        self.assertEqual(sorted(expect), sorted(got))

        got = sol.majorityElement([1, 2, 3])
        expect = []
        self.assertEqual(sorted(expect), sorted(got))

        got = sol.majorityElement([6, 6, 6, 7, 7])
        expect = [6, 7]
        self.assertEqual(sorted(expect), sorted(got))

        got = sol.majorityElement([1, 0, 0, 0, -2, 2])
        expect = [0]
        self.assertEqual(sorted(expect), sorted(got))

        got = sol.majorityElement([1,2,2,1,3,1,3,1,2,2,1])
        expect = [1,2]
        self.assertEqual(sorted(expect), sorted(got))

if __name__ == '__main__':
    unittest.main()
