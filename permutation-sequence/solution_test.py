import unittest
import solution

class TestSolution(unittest.TestCase):
    def test_case0(self):
        sol = solution.Solution()
        self.assertEqual("2314", sol.getPermutation(4, 9))
        self.assertEqual("123", sol.getPermutation(3, 1))
        self.assertEqual("132", sol.getPermutation(3, 2))
        self.assertEqual("21", sol.getPermutation(2, 2))

if __name__ == '__main__':
    unittest.main()
