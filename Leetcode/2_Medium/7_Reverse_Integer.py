# Leetcode problem: https://leetcode.com/problems/reverse-integer/
# Difficulty: Medium
# Runtime beat: 64.53%
# Memory beat: 57.44%
# © Sigeri

class Solution:
    def reverse(self, x):
        num = int(str(x)[::-1]) if x >= 0 else -int(str(x)[::-1][:-1])  # Convert to str -> Reversing ([::-1]) -> Conver back to int -> +/-
        treshold = pow(2, 31)  # Setting treshold (32 bits)
        return num if -treshold < num < treshold-1 else 0  # Returning the right number and applying the threshold

sol = Solution()
print(sol.reverse(x=123))  # Call reverse func

