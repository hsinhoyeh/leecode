class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """

        tokens = preorder.split(",")

        #  cases
        #    #   : true (#\#: 1, #num=0)

        #    3
        #   # #  : true (#\#: 2, #num=1)

        #    3
        #   1 #
        #  # #   : true (#\#: 3, #num=2)

        slot = 0
        for token in tokens:
            if slot < 0:
                return False
            if token == "#":
                slot -= 1
            else:
                slot += 1
        return slot+1 == 0

