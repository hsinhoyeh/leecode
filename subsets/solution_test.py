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
        self.assertSetEqual(
            self.list_of_list_to_set(
                [[3],[1],[2],[1,2,3],[1,3],[2,3],[1,2],[]]),
            self.list_of_list_to_set(sol.subsets([1,2,3])))

    def test_case1(self):
        sol = solution.Solution()
        self.assertSetEqual(
            self.list_of_list_to_set(
            [[],[4],[1],[1,4],[0],[0,4],[0,1],[0,1,4]]),
            self.list_of_list_to_set(sol.subsets([4,1,0])))


if __name__ == '__main__':
    unittest.main()
