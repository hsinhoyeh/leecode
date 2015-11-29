import unittest
import solution

class TestSolution(unittest.TestCase):
    def test_case0(self):
        wd = solution.WordDictionary()
        wd.addWord("bad")
        wd.addWord("dad")
        wd.addWord("mad")
        self.assertEqual(False, wd.search("pad"))
        self.assertEqual(True, wd.search("bad"))
        self.assertEqual(True, wd.search(".ad"))
        self.assertEqual(True, wd.search("b.."))
        self.assertEqual(False, wd.search(".da"))

    def test_case1(self):
        wd = solution.WordDictionary()
        self.assertEqual(False, wd.search("a"))

    def test_case2(self):
        wd = solution.WordDictionary()
        wd.addWord("a")
        wd.addWord("a")
        self.assertEqual(True,wd.search("."))
        self.assertEqual(True,wd.search("a"))
        self.assertEqual(False,wd.search("aa"))
        self.assertEqual(True,wd.search("a"))
        self.assertEqual(False,wd.search(".a"))
        self.assertEqual(False,wd.search("a."))

    def test_case3(self):
        wd = solution.WordDictionary()
        wd.addWord("at")
        wd.addWord("and")
        wd.addWord("an")
        wd.addWord("add")
        self.assertEqual(False,wd.search("a"))
        self.assertEqual(False,wd.search(".at"))
        wd.addWord("bat")
        self.assertEqual(True,wd.search(".at"))
        self.assertEqual(True,wd.search("an."))
        self.assertEqual(False,wd.search("a.d."))
        self.assertEqual(False,wd.search("b."))
        self.assertEqual(True,wd.search("a.d"))
        self.assertEqual(False,wd.search("."))


if __name__ == '__main__':
    unittest.main()
