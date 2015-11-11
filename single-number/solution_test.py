import unittest
import solution

class TestSolution(unittest.TestCase):
    def test_case0(self):
        sol = solution.Solution()
        self.assertEqual(
                5,
                sol.singleNumber([1,2,3,4,5,4,3,2,1])
                )
    def test_case1(self):
        sol = solution.Solution()
        self.assertEqual(
                5,
                sol.singleNumber([14,5,14])
                )



if __name__ == '__main__':
    unittest.main()
