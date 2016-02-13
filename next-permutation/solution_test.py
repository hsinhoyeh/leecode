import unittest
import solution

class TestSolution(unittest.TestCase):
    def test_case0(self):
        sol = solution.Solution()
        state = [1,2,3]
        
        sol.nextPermutation(state)
        self.assertEqual([1,3,2], state)

        sol.nextPermutation(state)
        self.assertEqual([2,1,3], state)

    def test_case1(self):
        sol = solution.Solution()
        state = [3,2,1]
 
        sol.nextPermutation(state)
        self.assertEqual([1,2,3], state)

if __name__ == '__main__':
    unittest.main()
