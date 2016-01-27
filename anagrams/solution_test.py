import unittest
import solution

class TestSolution(unittest.TestCase):
    def test_case0(self):
        sol = solution.Solution()
        got = sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
        expect = [["ate", "eat","tea"],["nat","tan"],["bat"]]
        self.assertEqual(expect, got)

if __name__ == '__main__':
    unittest.main()
