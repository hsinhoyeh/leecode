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
        index = index + 1
        top = queue.popleft()

        if index >= len(lst):
            break;

        if not lst[index]:
            top.left = None
        else:
            top.left = TreeNode(lst[index])
            queue.append(top.left)

        index = index + 1
        if index > len(lst):
            break;

        if not lst[index]:
            top.right = None
        else:
            top.right = TreeNode(lst[index])
            queue.append(top.left)
    return root

class TestSolution(unittest.TestCase):
    def test_case0(self):
        root = makeTreeFromLevelOrder([])
        sol = solution.Solution()
        got = sol.minDepth(root)
        self.assertEqual(0, got)


    def test_case1(self):
        root = makeTreeFromLevelOrder([1,2,3,4,5])
        sol = solution.Solution()
        got = sol.minDepth(root)
        self.assertEqual(2, got)

if __name__ == '__main__':
    unittest.main()
