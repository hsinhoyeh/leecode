import unittest
import solution

class TestSolution(unittest.TestCase):
    def test_case1(self):
        return

        sol = solution.Solution()
        board = [
           ['o','a','a','n'],
           ['e','t','a','e'],
           ['i','h','k','r'],
           ['i','f','l','v']
        ]
        words = ["oath","pea","eat","rain"]
        expect = sorted(["eat","oath"])
        got = sorted(sol.findWords(board, words))
        self.assertEqual(expect, got)

    def test_case2(self):
        return

        sol = solution.Solution()
        board = [
           ['o','a','a','n'],
           ['e','t','a','e'],
           ['i','h','a','a'],
           ['i','f','l','v']
        ]
        words = ["aa","aaa","aaaa","aaaaa", "aaaaaa"]
        expect = sorted(["aa","aaa","aaaa","aaaaa"])
        got = sorted(sol.findWords(board, words))
        self.assertEqual(expect, got)

    def test_case101(self):
        return

        sol = solution.Solution()
        board = [
           ['a','a','a','a'],
           ['a','a','a','a'],
           ['a','a','a','a']
        ]
        words = ["aaaaaaaaaaaa","aaaaaaaaaaaaa","aaaaaaaaaaab"]
        expect = sorted(["aaaaaaaaaaaa"])
        got = sorted(sol.findWords(board, words))
        self.assertEqual(expect, got)

    def test_case102(self):
        return

        sol = solution.Solution()
        board = [
           ['a','a','a','a'],
           ['a','a','a','a'],
           ['a','a','a','a'],
           ['b','c','d','e'],
           ['f','g','h','i'],
           ['j','k','l','m'],
           ['n','o','p','q'],
           ['r','s','t','u'],
           ['v','w','x','y'],
           ['z','z','z','z']
        ]

        words = ["aaaaaaaaaaaaaaaa","aaaaaaaaaaaaaaab"]
        expect = sorted([])
        got = sorted(sol.findWords(board, words))
        self.assertEqual(expect, got)

    def test_case103(self):
#        return

        sol = solution.Solution()
        board = [
           ['b', 'a', 'a', 'b', 'a', 'b'],
           ['a', 'b', 'a', 'a', 'a', 'a'],
           ['a', 'b', 'a', 'a', 'a', 'b'],
           ['a', 'b', 'a', 'b', 'b', 'a'],
           ['a', 'a', 'b', 'b', 'a', 'b'],
           ['a', 'a', 'b', 'b', 'b', 'a'],
           ['a', 'a', 'b', 'a', 'a', 'b']
        ]

        words = ["bbaabaabaaaaabaababaaaaababb","aabbaaabaaabaabaaaaaabbaaaba","babaababbbbbbbaabaababaabaaa","bbbaaabaabbaaababababbbbbaaa","babbabbbbaabbabaaaaaabbbaaab","bbbababbbbbbbababbabbbbbabaa","babababbababaabbbbabbbbabbba","abbbbbbaabaaabaaababaabbabba","aabaabababbbbbbababbbababbaa","aabbbbabbaababaaaabababbaaba","ababaababaaabbabbaabbaabbaba","abaabbbaaaaababbbaaaaabbbaab","aabbabaabaabbabababaaabbbaab","baaabaaaabbabaaabaabababaaaa","aaabbabaaaababbabbaabbaabbaa","aaabaaaaabaabbabaabbbbaabaaa","abbaabbaaaabbaababababbaabbb","baabaababbbbaaaabaaabbababbb","aabaababbaababbaaabaabababab","abbaaabbaabaabaabbbbaabbbbbb","aaababaabbaaabbbaaabbabbabab","bbababbbabbbbabbbbabbbbbabaa","abbbaabbbaaababbbababbababba","bbbbbbbabbbababbabaabababaab","aaaababaabbbbabaaaaabaaaaabb","bbaaabbbbabbaaabbaabbabbaaba","aabaabbbbaabaabbabaabababaaa","abbababbbaababaabbababababbb","aabbbabbaaaababbbbabbababbbb","babbbaabababbbbbbbbbaabbabaa"]
        expect = sorted(["aabbbbabbaababaaaabababbaaba", "abaabbbaaaaababbbaaaaabbbaab", "ababaababaaabbabbaabbaabbaba"])
        got = sorted(sol.findWords(board, words))
        self.assertEqual(expect, got)

if __name__ == '__main__':
    unittest.main()
