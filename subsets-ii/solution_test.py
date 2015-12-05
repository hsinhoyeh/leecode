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
                [[2],[1],[1,2,2],[2,2],[1,2],[]]),
            self.list_of_list_to_set(sol.subsetsWithDup([1,2,2])))

if __name__ == '__main__':
    unittest.main()
