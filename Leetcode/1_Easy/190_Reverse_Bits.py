# Leetcode problem: https://leetcode.com/problems/reverse-bits/
# Difficulty: Easy
# 1. Runtime beat: 98.29%
# 1. Memory beat: 78.59%
# 2. Runtime beat: 75.29%
# 2. Memory beat: 95.64%

class Solution1:
    def reverseBits(self, n):
        n_bin = f'{str(bin(n)[2:]):0>32}'  # Convert to 32 bit binary number
        return int(str(int(n_bin[::-1]) if n >= 0 else -int(n_bin[::-1][:-1])), 2)  # cutting the end char, +/- and conver back to DEC

class Solution2:
    def reverseBits(self, n):
        n_bin = f'{str(bin(n)[2:]):0>32}'[::-1]  # Convert to 32 bit binary number and cut the end char
        return int(str(int(n_bin) if n >= 0 else -int(n_bin[:-1])), 2)  # +/- and conver back to DEC
        

sol = Solution1()
print(sol.reverseBits(n=43261596))  # Calling reverseBits func (first solution)
