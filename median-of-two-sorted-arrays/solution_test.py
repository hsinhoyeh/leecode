import unittest
import solution

class TestSolution(unittest.TestCase):
    def test_case0(self):
        sol = solution.Solution()
        self.assertEqual(
                1,
                sol.findMedianSortedArrays([1], [1]))

    def test_case1(self):
        sol = solution.Solution()
        self.assertEqual(
                3,
                sol.findMedianSortedArrays([], [1,3,5]))

    def test_case2(self):
        sol = solution.Solution()
        self.assertEqual(
                1,
                sol.findMedianSortedArrays([1,1,1], [1,3,5]))

    def test_case3(self):
        sol = solution.Solution()
        self.assertEqual(
                4.5,
                sol.findMedianSortedArrays([4,5,5], [1,3,5]))

    def test_case4(self):
        sol = solution.Solution()
        self.assertEqual(
                5,
                sol.findMedianSortedArrays([1,3,5,7], [2,4,6,8,10])) 

    def test_case5(self):
        sol = solution.Solution()
        self.assertEqual(
                100000.5,
                sol.findMedianSortedArrays([100000], [100001]))

    def test_case6(self):
        sol = solution.Solution()
        self.assertEqual(
                2.5,
                sol.findMedianSortedArrays([1], [2,3,4]))

    def test_case7(self):
        sol = solution.Solution()
        self.assertEqual(
                2.5,
                sol.findMedianSortedArrays([], [2,3]))



if __name__ == '__main__':
    unittest.main()
