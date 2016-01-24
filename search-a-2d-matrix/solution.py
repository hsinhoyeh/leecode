class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # narrow down the search space by examing the last eleemnt in each row, which is a upper bound of the row

        for row in matrix:
            if target > row[-1]:
                continue
            if target < row[0]:
                return False # not found
            if target in row:
                return True
        return False
