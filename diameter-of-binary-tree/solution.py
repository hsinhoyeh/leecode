# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    max_sum_depth_of_a_node = 0
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.postOrder(root)
        return self.max_sum_depth_of_a_node


    def postOrder(self, root):
        leftDepth = 0
        rightDepth = 0
        if not root:
            return 0
        if root.left:
            leftDepth = self.postOrder(root.left) + 1
        if root.right:
            rightDepth = self.postOrder(root.right) + 1
        sumDepth = leftDepth + rightDepth
        if sumDepth > self.max_sum_depth_of_a_node:
            self.max_sum_depth_of_a_node = sumDepth
        return max(leftDepth, rightDepth)
