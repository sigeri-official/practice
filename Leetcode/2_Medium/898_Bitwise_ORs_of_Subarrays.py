# Leetcode problem: https://leetcode.com/problems/bitwise-ors-of-subarrays/
# Difficulty: Medium
# Runtime beat: 100.00%
# Memory beat: 95.48%

class Solution:
    def subarrayBitwiseORs(self, arr):
        def sor(lst):
            num = arr[0]
            for i in lst:
                num = num | i
            return num
        amount = set()
        for i in range(len(arr)):
            for j in range(i, len(arr)):
                if abs(i-j) < len(arr):
                    amount.add(sor(arr[i:j]))
                    print(f'{i = }, {j = }     {arr[i] = :4} | {bin(arr[i])[2:]:8} {arr[j] = :4} | {bin(arr[j])[2:]:8} {bin(arr[i]|arr[j])[2:]:8}    {arr = }, {amount = }')

        return len(amount)

sol = Solution()
print(sol.subarrayBitwiseORs(arr=[1,1,2]))



class Solution1:
    def subarrayBitwiseORs(self, arr):
        return len(set(arr[i]+arr[j] for i in range(len(arr)) for j in range(i, len(arr))))


