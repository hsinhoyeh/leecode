import unittest
import solution

class TestSolution(unittest.TestCase):
    def test_basic(self):
        sol = solution.Solution()

        # given [000000...10] = 2
        self.assertEqual(0, sol.bit_n(2, 0))
        self.assertEqual(1, sol.bit_n(2, 1))

        bit64 = 64 * [0]
        bit64[1]=1
        self.assertEqual(2, sol.num_from_bits(bit64))

        # given [111111...11] = -1
        self.assertEqual(1, sol.bit_n(-1, 0))
        self.assertEqual(1, sol.bit_n(-1, 63))
        self.assertEqual(-1, sol.num_from_bits(64 * [1]))

        # given [111111...100] = -4
        one64 = 64 * [1]
        one64[0] = 0
        one64[1] = 0
        self.assertEqual(-4, sol.num_from_bits(one64))

        # given [00000...011] = 3
        bit64 = 64 * [0]
        bit64[0]=1
        bit64[1]=1
        self.assertEqual(3, sol.num_from_bits(bit64))

    def test_case0(self):
        sol = solution.Solution()
        self.assertEqual(
                5,
                sol.singleNumber([1,1,1,2,2,2,5])
                )
    def test_case1(self):
        sol = solution.Solution()
        self.assertEqual(
                5,
                sol.singleNumber([1,3,5,7,9,1,3,7,9,1,3,7,9])
                )
    def test_case3(self):
        sol = solution.Solution()
        self.assertEqual(
                -4,
                sol.singleNumber([-2,-2,1,1,-3,1,-3,-3,-4,-2])
                )
    def test_case4(self):
        sol = solution.Solution()
        self.assertEqual(
                4,
                sol.singleNumber([2,2,1,1,3,1,3,3,4,2])
                )

if __name__ == '__main__':
    unittest.main()
