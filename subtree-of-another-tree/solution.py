# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        s_buffer = []
        t_buffer = []
        self.postOrder(s_buffer, s)
        self.postOrder(t_buffer, t)
        return self.match_sublist(s_buffer, t_buffer)


    def match_sublist(self, src, pattern):
        for i in range(0, len(src)):
            if src[i] != pattern[0]:
                continue
            proj = src[i:]
            notmatch = False
            for j in range(0, len(pattern)):
                if proj[j] != pattern[j]:
                    notmatch = True
                    break
            if not notmatch:
                return True
        return False

    def postOrder(self, buffer, root):
        if not root:
            return
        if root.left:
            self.postOrder(buffer, root.left)
        else:
            buffer.append("#")
        if root.right:
            self.postOrder(buffer, root.right)
        else:
            buffer.append("#")
        buffer.append(root.val)
