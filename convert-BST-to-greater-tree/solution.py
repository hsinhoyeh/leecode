# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    buffer = []

    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.buffer = []
        self.inorder(root)

        # accumulate from last one to the first one
        self.buffer.reverse()

        sum_so_far = 0
        for i in range(0, len(self.buffer)):
            curval = self.buffer[i]
            self.buffer[i] = curval + sum_so_far
            sum_so_far = sum_so_far + curval
        self.buffer.reverse()

        # then mapping the value back with inorder traverse
        self.inorderWithMappingValue(root)
        return root

    def inorder(self, root):
        if not root:
            return
        if root.left:
            self.inorder(root.left)
        self.buffer.append(root.val)
        if root.right:
            self.inorder(root.right)

    def inorderWithMappingValue(self, root):
        if not root:
            return
        if root.left:
            self.inorderWithMappingValue(root.left)
        root.val = self.buffer[0]
        del self.buffer[0]
        if root.right:
            self.inorderWithMappingValue(root.right)

