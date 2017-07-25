# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        ret = self.dfs(root, 1)
        return ret

    def dfs(self, root, depth):
        if not root:
            return depth
        left = None
        right = None
        if root.left:
            left = self.dfs(root.left, depth+1)
        if root.right:
            right = self.dfs(root.right, depth+1)
        if left is None and right is None:
            return depth
        if left is None:
            return right
        if right is None:
            return left
        return min(left, right)
