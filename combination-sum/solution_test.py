import unittest
import solution

class TestSolution(unittest.TestCase):
    def list_of_list_to_set(self, lsts):
        sset = set()
        for ele in lsts:
            sset.add(tuple(ele))
        return sset

    def test_case0(self):
        sol = solution.Solution()
        got = sol.combinationSum([2,3,6,7], 7)
        expect = [[7],[2,2,3],]
        self.assertSetEqual(self.list_of_list_to_set(expect), self.list_of_list_to_set(got))

    def test_case1(self):
        sol = solution.Solution()
        got = sol.combinationSum([1], 2)
        expect = [[1,1]]
        self.assertSetEqual(self.list_of_list_to_set(expect), self.list_of_list_to_set(got))

    def test_case2(self):
        sol = solution.Solution()
        got = sol.combinationSum([1,2], 3)
        expect = [[1,1,1], [1,2]]
        self.assertSetEqual(self.list_of_list_to_set(expect), self.list_of_list_to_set(got))



if __name__ == '__main__':
    unittest.main()
