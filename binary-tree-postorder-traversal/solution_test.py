import unittest
import solution

class TestSolution(unittest.TestCase):
    index = 0
    def take(self, inputs):
        if self.index >= len(inputs):
            return "#"
        ret = inputs[self.index]
        self.index = self.index + 1
        return ret

    def construction(self, inputs):
        token = self.take(inputs)
        if token == "#":
            return None
        node = solution.TreeNode(token)
        node.left = self.construction(inputs) # build left
        node.right = self.construction(inputs) # build right
        return node

    def test_case0(self):
        given = "1,#,2,3"
        tokens = given.split(",")
        root = self.construction(tokens)

        sol = solution.Solution()
        got = sol.postorderTraversal(root)
        self.assertEqual([3,2,1], got)

if __name__ == '__main__':
    unittest.main()
