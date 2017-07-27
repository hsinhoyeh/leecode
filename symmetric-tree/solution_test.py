import unittest

from collections import deque

import solution

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def levelOrder(lst, root):
    if not root:
        return

    queue = deque([root])
    while len(queue) > 0:
        top = queue.popleft()
        if not top:
            break;
        if top.left:
            queue.append(top.left)
        if top.right:
            queue.append(top.right)
        lst.append(top.val)

def makeTreeFromLevelOrder(lst):
    if not lst:
        return None
    index = 0
    queue = deque([])
    root = TreeNode(lst[index])
    queue.append(root)

    while True:
        top = queue.popleft()

        index = index + 1
        if index >= len(lst):
            break;

        if lst[index] is None:
            top.left = None
        else:
            top.left = TreeNode(lst[index])
            queue.append(top.left)

        index = index + 1
        if index >= len(lst):
            break;

        if lst[index] is None:
            top.right = None
        else:
            top.right = TreeNode(lst[index])
            queue.append(top.right)
    return root

class TestSolution(unittest.TestCase):
    def test_case0(self):
        root = makeTreeFromLevelOrder([1,2,2,3,4,4,3])
        sol = solution.Solution()
        got = sol.isSymmetric(root)
        self.assertEqual(True, got)

    def test_case1(self):
        root = makeTreeFromLevelOrder([1,2,2,None,3,None,3])
        sol = solution.Solution()
        got = sol.isSymmetric(root)
        self.assertEqual(False, got)

    def test_case2(self):
        root = makeTreeFromLevelOrder([5,4,1,None,1,None,4,2,None,2,None])
        sol = solution.Solution()
        got = sol.isSymmetric(root)
        self.assertEqual(False, got)


if __name__ == '__main__':
    unittest.main()
