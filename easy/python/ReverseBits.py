'''
Reverse bits of a given 32 bits unsigned integer.

For example, given input 43261596 (represented in binary as 00000010100101000001111010011100), return 964176192 (represented in binary as 00111001011110000010100101000000).
'''
class Solution(object):
    def reverseBits(self, n):
        for i in range(0, 16):
            n = self.swap(n, i, 31 - i)
        return n

    def swap(self, n, i, j):
        ith = (n >> i) & 1
        jth = (n >> j) & 1

        if ith ^ jth:
            return n ^ ((1 << i) | (1 << j))
        return n

if __name__ == "__main__":
    assert 964176192 == Solution().reverseBits(43261596)