class Solution(object):

    def int_in_bits(self):
        return 64 * [0]

    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 1:
            return -1

        int_in_bit = self.int_in_bits()
        for idx in range(0, len(nums)):
            for bit in range(0, len(int_in_bit)):
                int_in_bit[bit] += self.bit_n(nums[idx], bit)
                if int_in_bit[bit] == 3: # reset for every three times
                    int_in_bit[bit] = 0

        return self.num_from_bits(int_in_bit)

    def num_from_bits(self, bits):
        sign = bits[-1] # last one is the sign bit
        if sign: # negative, use 2'complementory
            twos = self.int_in_bits()
            for bit in range(0, len(twos)-1): #ignore the sign bit
                twos[bit] = 1 ^ bits[bit]
            return -(self.num_from_bits(twos) + 1)
        num = 0
        for bit in range(0, 64):
            if bits[bit]:
                num += 1<< bit
        return num

    def bit_n(self, num, n):
        return num & (1 << n) > 0
