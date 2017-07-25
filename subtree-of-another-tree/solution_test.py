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
        root = makeTreeFromLevelOrder([1,2,3,4,5])
        subtree = makeTreeFromLevelOrder([2,4,5])
        sol = solution.Solution()
        got = sol.isSubtree(root, subtree)
        self.assertEqual(True, got)

    def test_case1(self):
        root = makeTreeFromLevelOrder([1])
        subtree = makeTreeFromLevelOrder([0])
        sol = solution.Solution()
        got = sol.isSubtree(root, subtree)
        self.assertEqual(False, got)


    def test_case2(self):
        root = makeTreeFromLevelOrder([29,28,30,27,29,29,31,26,26,28,28,28,28,30,32,25,25,25,25,27,29,None,29,29,29,None,29,29,29,31,None,26,24,26,26,26,None,24,None,None,26,28,None,28,28,30,28,30,30,None,None,30,30,30,30,None,32,27,27,None,25,25,None,None,25,27,27,None,None,None,None,27,27,27,29,None,None,None,31,29,None,31,None,29,29,None,None,29,31,None,29,29,31,None,31,None,None,None,28,24,24,24,26,24,24,None,28,26,28,26,None,None,None,28,28,None,28,None,None,28,30,32,None,30,28,28,28,None,None,None,None,28,30,28,28,None,None,None,None,27,None,None,None,23,25,None,None,None,None,None,None,None,None,27,27,None,None,None,29,None,None,None,None,27,29,None,27,27,None,None,None,None,31,29,29,27,29,None,29,27,29,None,None,None,None,27,None,None,29,None,None,22,22,None,26,None,None,26,28,28,28,None,28,None,28,None,28,None,None,None,None,None,None,None,28,None,28,28,None,30,None,None,None,None,None,26,None,28,30,21,23,None,None,None,25,None,27,None,None,None,None,27,29,27,29,27,27,None,None,None,None,29,None,27,None,None,None,25,27,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,28,None,None,None,None,None,None,None,None,26,None,None,24,None,28,None,None,None,None,None,23])
        subtree = makeTreeFromLevelOrder([29])
        sol = solution.Solution()
        got = sol.isSubtree(root, subtree)
        self.assertEqual(True, got)

    def test_case3(self):
        root = makeTreeFromLevelOrder([3,4,5,1,2,None,None,0])
        subtree = makeTreeFromLevelOrder([4,1,2])
        sol = solution.Solution()
        got = sol.isSubtree(root, subtree)
        self.assertEqual(False, got)



if __name__ == '__main__':
    unittest.main()
