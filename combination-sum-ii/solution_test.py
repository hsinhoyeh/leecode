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
        got = sol.combinationSum2([10,1,2,7,6,1,5], 8)
        expect = [[1,7],[1,2,5],[2,6],[1,1,6]]
        self.assertSetEqual(self.list_of_list_to_set(expect), self.list_of_list_to_set(got))

if __name__ == '__main__':
    unittest.main()
