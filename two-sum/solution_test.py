import unittest
import solution

class TestSolution(unittest.TestCase):
    def test_case0(self):
        sol = solution.Solution()
        self.assertEqual([1,2], sol.twoSum([2,7,11,15], 9))
        self.assertEqual([2,3], sol.twoSum([3,2,4], 6))
        self.assertEqual([1,4], sol.twoSum([0,4,3,0], 0))
        self.assertEqual([3,5], sol.twoSum([-1,-2,-3,-4,-5], -8))

if __name__ == '__main__':
    unittest.main()
