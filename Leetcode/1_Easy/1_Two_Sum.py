# Leetcode problem: https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):  # Iterate for the first number
            for j in range(i+1, len(nums)):  # Iterate for the second number
                if nums[i] + nums[j] == target:
                    return [i, j]  # Return the values

sol = Solution()
print(sol.twoSum(nums=[2,7,11,15], target=9))  # Call twoSum def
