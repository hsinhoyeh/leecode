import unittest
import solution

class TestSolution(unittest.TestCase):
    def test_case0(self):
        sol = solution.Solution()
        i1 = solution.Interval(1,3)
        i2 = solution.Interval(2,4)
        i_expect = solution.Interval(1,4)
        i_got = sol.merge([i1, i2])
        self.assertEqual(1, len(i_got))
        self.assertEqual(i_expect.start, i_got[0].start)
        self.assertEqual(i_expect.end, i_got[0].end)

    def test_case1(self):
        sol = solution.Solution()
        i1 = solution.Interval(1,3)
        i2 = solution.Interval(2,4)
        i3 = solution.Interval(2,3)
        i_expect = solution.Interval(1,4)
        i_got = sol.merge([i1, i2, i3])
        self.assertEqual(1, len(i_got))
        self.assertEqual(i_expect.start, i_got[0].start)
        self.assertEqual(i_expect.end, i_got[0].end)



if __name__ == '__main__':
    unittest.main()
