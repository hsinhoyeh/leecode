import unittest
import solution

class TestSolution(unittest.TestCase):
    def test_case1(self):
        sol = solution.Solution()
        got = sol.findSubstring(
                "barfoothefoobarman",
                ["foo", "bar"])
        self.assertEqual([0,9], got)

    def test_case2(self):
        sol = solution.Solution()
        got = sol.findSubstring(
                "wordgoodgoodgoodbestword",
                ["word","good","best","good"])
        self.assertEqual([8], got)

    def test_case3(self):
        sol = solution.Solution()
        got = sol.findSubstring(
                "lingmindraboofooowingdingbarrwingmonkeypoundcake",
                ["fooo","barr","wing","ding","wing"])
        self.assertEqual([13], got)

    def test_case4(self):
        sol = solution.Solution()
        got = sol.findSubstring(
                "lingmindraboofooowingdingbarrwingmonkeypoundcake",
                ["fooo","barr","wing","ding","wing","fooo","barr","wing","ding","wing","fooo","barr","wing","ding","wing","fooo","barr","wing","ding","wing","fooo","barr","wing","ding","wing","fooo","barr","wing","ding","wing","fooo","barr","wing","ding","wing","fooo","barr","wing","ding","wing"])
        self.assertEqual([], got)

    def test_case5(self):
        sol = solution.Solution()
        got = sol.findSubstring(
                "a",
                ["a", "a"])
        self.assertEqual([], got)

    def test_case6(self):
        sol = solution.Solution()
        got = sol.findSubstring(
                "aaaaaa",
                ["aaa", "aaa"])
        self.assertEqual([0], got)

    def test_case7(self):
        sol = solution.Solution()
        got = sol.findSubstring(
                "abababab",
                ["a", "b", "a"])
        self.assertEqual([0, 2, 4], got)

    def test_case8(self):
        sol = solution.Solution()
        got = sol.findSubstring(
                "mississippi",
                ["is"])
        self.assertEqual([1, 4], got)

if __name__ == '__main__':
    unittest.main()
