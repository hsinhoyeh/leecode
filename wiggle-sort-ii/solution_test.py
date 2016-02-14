import unittest
import solution

class TestSolution(unittest.TestCase):

    def well_ordered(self, nums):
        print "assert :%s"%nums
        # check even number
        for i in range(0, len(nums), 2):
            left = i -1
            right = i +1
            if right < len(nums) and nums[i] >= nums[right]:
                return False
            if left >=0 and nums[i] >= nums[left]:
                return False
        # check odd number
        for i in range(1, len(nums), 2):
            left = i -1
            right = i +1
            if right < len(nums) and nums[i] <= nums[right]:
                return False
            if left >= 0 and nums[i] <= nums[left]:
                return False
        return True
 
    def test_basic(self):
        self.assertTrue(self.well_ordered([1, 4, 1, 5, 1, 6]))
        self.assertFalse(self.well_ordered([4, 1, 1, 5, 1, 6]))
        self.assertFalse(self.well_ordered([1, 3, 2, 2, 1, 3]))

    def test_case0(self):
        sol = solution.Solution()
        seq = [1, 5, 1, 1, 6, 4]
        sol.wiggleSort(seq)
        self.assertTrue(self.well_ordered(seq))

        seq = [4,5,5,5,5,6,6,6]
        sol.wiggleSort(seq)
        self.assertTrue(self.well_ordered(seq))

        seq = [1,3,2,2,3,1]
        sol.wiggleSort(seq)
        self.assertTrue(self.well_ordered(seq))

        seq = [3,2,3,3,2,1,1,2,3,1,1,3,2,1,2,2,2,2,1]
        sol.wiggleSort(seq)
        self.assertTrue(self.well_ordered(seq))

        seq = [1,2,2,5,2,1,5,2,1,3,4,4,1,5,2]
        sol.wiggleSort(seq)
        self.assertTrue(self.well_ordered(seq))

if __name__ == '__main__':
    unittest.main()
