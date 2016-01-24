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
        got = sol.fourSum([1, 0, -1, 0, -2, 2], 0)
        expect = [[-1, 0, 0, 1], [-2, -1, 1, 2], [-2, 0, 0, 2]]
        self.assertSetEqual(
            self.list_of_list_to_set(expect),
            self.list_of_list_to_set(got))

        got = sol.fourSum([1, 0, 0, 0, 0, 2], 0)
        expect = [[0, 0, 0, 0]]
        self.assertSetEqual(
            self.list_of_list_to_set(expect),
            self.list_of_list_to_set(got))

    def test_case1(self):
        sol = solution.Solution()
        got = sol.fourSum([-491,-489,-470,-428,-416,-413,-394,-390,-377,-373,-362,-357,-349,-328,-282,-270,-266,-247,-175,-156,-133,-122,-116,-102,-91,-57,-44,-42,-37,-24,-2,20,42,55,58,71,123,136,139,151,155,164,165,193,212,223,294,299,309,313,318,327,341,357,374,375,390,392,413,427,453,457,459,466,497,499],-3742)
        expect = []
        self.assertSetEqual(
            self.list_of_list_to_set(expect),
            self.list_of_list_to_set(got))

if __name__ == '__main__':
    unittest.main()
