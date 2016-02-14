import unittest
import solution

class TestSolution(unittest.TestCase):

    def test_case0(self):
        sol = solution.Solution()

        self.assertEqual(5, sol.findKthLargest([5,2,4,1,3,6,0], 2))
        self.assertEqual(3, sol.findKthLargest([3,3,3,3,3,3,3], 1))
        self.assertEqual(5, sol.findKthLargest([3,2,1,5,6,4], 2))
        self.assertEqual(9, sol.findKthLargest([9,8,7,6,5,4,3,2,1], 1))
        self.assertEqual(8, sol.findKthLargest([9,8,7,6,5,4,3,2,1], 2))
        self.assertEqual(1, sol.findKthLargest([9,8,7,6,5,4,3,2,1], 9))

    def test_case1(self):
        sol = solution.Solution()

        self.assertEqual(3, sol.findKthLargest([3,3,3,3,4,3,3,3,3], 5))

if __name__ == '__main__':
    unittest.main()
