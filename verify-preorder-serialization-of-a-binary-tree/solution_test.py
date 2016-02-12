import unittest
import solution

class TestSolution(unittest.TestCase):
    def test_case0(self):
        sol = solution.Solution()
        self.assertEqual(True,
            sol.isValidSerialization("9,3,4,#,#,1,#,#,2,#,6,#,#"))

        self.assertEqual(False,
            sol.isValidSerialization("1,#"))

        self.assertEqual(False,
            sol.isValidSerialization("9,#,#,1"))

        self.assertEqual(False,
            sol.isValidSerialization("#,#,#"))

        self.assertEqual(False,
            sol.isValidSerialization("#,#,3,5,#"))

        self.assertEqual(False,
            sol.isValidSerialization("#,7,6,9,#,#,#"))

if __name__ == '__main__':
    unittest.main()
