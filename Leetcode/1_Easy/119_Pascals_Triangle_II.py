# Leetcode problem: https://leetcode.com/problems/pascals-triangle-ii/
# Difficulty: Easy
# Runtime beat: 100.00%
# Memory beat: 96.91%
# © Sigeri

class Solution:
    def getRow(self, rowIndex):
        lst = [[1]]
        for i in range(rowIndex):
            row = [1]
            for j in range(len(lst[i])-1):
                row.append(lst[i][j]+lst[i][j+1])  # Add the new number
            lst.append(row)
            row.append(1)
        return lst[-1] if rowIndex != 0 else [1]

sol = Solution()
print(sol.getRow(rowIndex=3))  # Print the list