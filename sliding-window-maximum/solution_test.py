import unittest
import solution

class TestSolution(unittest.TestCase):
    def test_case0(self):
        sol = solution.Solution()
        self.assertEqual([3,3,5,5,6,7], sol.maxSlidingWindow([1,3,-1,-3,5,3,6,7],3))
        self.assertEqual([1,-1], sol.maxSlidingWindow([1,-1],1))
        self.assertEqual([9,9,10,10,10,10,10,10,10,9,9,9,8,8], sol.maxSlidingWindow([-6,-10,-7,-1,-9,9,-8,-4,10,-5,2,9,0,-7,7,4,-2,-10,8,7],7))

if __name__ == '__main__':
    unittest.main()
