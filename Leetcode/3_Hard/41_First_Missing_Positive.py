# Leetcode problem: https://leetcode.com/problems/first-missing-positive/
# Difficulty: Hard
# Runtime beat: 88.33%
# Memory beat: 6.10%
# © Sigeri

class Solution:
    def firstMissingPositive(self, nums):
        nums = list(set([i for i in nums if i > 0]))  # Deleting repetitions
        nums.sort()  # Sort the list in ascending order
        for i in range(len(nums)):
            if nums[i] - 1 != i:  # The first number what is not in the order
                return i+1  # Return the missing number
        return len(nums)+1  # Return the next number

sol = Solution()
print(sol.firstMissingPositive(nums=[1,2,0]))  # Call firstMissingPositive function
