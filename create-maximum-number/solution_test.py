import unittest
import solution

class TestSolution(unittest.TestCase):
    def test_case0(self):
        sol = solution.Solution()
        got = sol.maxNumber([3, 4, 6, 5], [9, 1, 2, 5, 8, 3], 5)
        expect = [9, 8, 6, 5, 3]
        self.assertEqual(expect, got)

    def test_case1(self):
        sol = solution.Solution()
        got = sol.maxNumber([6, 7], [6, 0, 4], 5)
        expect = [6, 7, 6, 0, 4]
        self.assertEqual(expect, got)

    def test_case2(self):
        sol = solution.Solution()
        got = sol.maxNumber([3, 9], [8, 9], 3)
        expect = [9, 8, 9]
        self.assertEqual(expect, got)

    def test_case3(self):
        sol = solution.Solution()
        got = sol.maxNumber([3, 9], [2, 9], 2)
        expect = [9, 9]
        self.assertEqual(expect, got)

    def test_case4(self):
        sol = solution.Solution()
        got = sol.maxNumber([2, 5, 6, 4, 4, 0], [7, 3, 8, 0, 6, 5, 7, 6, 2], 15)
        expect = [7, 3, 8, 2, 5, 6, 4, 4, 0, 6, 5, 7, 6, 2, 0]
        self.assertEqual(expect, got)

    def test_case5(self):
        sol = solution.Solution()
        got = sol.maxNumber([6,7,5], [4,8,1], 3)
        expect = [8, 7, 5]
        self.assertEqual(expect, got)

    def test_case6(self):
        sol = solution.Solution()
        got = sol.maxNumber([4,6,9,1,0,6,3,1,5,2,8,3,8,8,4,7,2,0,7,1,9,9,0,1,5,9,3,9,3,9,7,3,0,8,1,0,9,1,6,8,8,4,4,5,7,5,2,8,2,7,7,7,4,8,5,0,9,6,9,2], [9,9,4,5,1,2,0,9,3,4,6,3,0,9,2,8,8,2,4,8,6,5,4,4,2,9,5,0,7,3,7,5,9,6,6,8,8,0,2,4,2,2,1,6,6,5,3,6,2,9,6,4,5,9,7,8,0,7,2,3], 60)
        expect = [9,9,9,9,9,9,9,9,9,9,9,9,9,8,8,6,8,8,4,4,5,7,5,2,8,2,7,7,7,4,8,5,0,9,6,9,2,0,2,4,2,2,1,6,6,5,3,6,2,9,6,4,5,9,7,8,0,7,2,3]
        self.assertEqual(expect, got)

if __name__ == '__main__':
    unittest.main()
