class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Stack(object):
    data = []
    def __init__(self):
        self.data = []
    def push(self, x):
        self.data.append(x)
    def pop(self):
        return self.data.pop()
    def top(self):
        return self.data[0]
    def is_empty(self):
        return len(self.data) == 0

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []

        ins = Stack()
        out = Stack()

        ins.push(root)
        while not ins.is_empty():
            s = ins.pop()
            out.push(s)
            if s.left is not None:
                ins.push(s.left)
            if s.right is not None:
                ins.push(s.right)

        ret = []
        while not out.is_empty():
            x = out.pop()
            ret.append(int(x.val))
        return ret
