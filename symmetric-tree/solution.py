# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        right=[]
        left=[]
        self.rightFirst(right, root)
        self.leftFirst(left, root)
        return right == left



    def rightFirst(self, buffer, root):
        if not root:
            return

        buffer.append(root.val)

        if root.right:
            self.rightFirst(buffer, root.right)
        else:
            buffer.append("#")

        if root.left:
            self.rightFirst(buffer, root.left)
        else:
            buffer.append("#")

    def leftFirst(self, buffer, root):
        if not root:
            return

        buffer.append(root.val)

        if root.left:
            self.leftFirst(buffer, root.left)
        else:
            buffer.append("#")
        if root.right:
            self.leftFirst(buffer, root.right)
        else:
            buffer.append("#")
