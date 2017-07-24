# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """

        ret = []
        queue = deque([root])
        while True:
            current_size = len(queue)
            if current_size == 0:
                break
            sublist = []
            for i in range(0, current_size):
                top = queue.popleft()
                left = top.left
                right = top.right
                val = top.val

                sublist.append(val)

                if left:
                    queue.append(left)
                if right:
                    queue.append(right)
            ret.append(float(sum(sublist))/ len(sublist))
        return ret
