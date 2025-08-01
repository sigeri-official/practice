# Leetcode problem: https://leetcode.com/problems/pascals-triangle/
# Difficulty: Easy
# Runtime beat: 100.00%
# Memory beat: 98.14%
# © Sigeri

class Solution:
    def generate(self, rows):
        lst = [[1]]
        for i in range(rows-1):
            row = [1]
            for j in range(len(lst[i])-1):
                row.append(lst[i][j]+lst[i][j+1])  # Add the new number
            lst.append(row)
            row.append(1)
        return lst if rows != 0 else []

sol = Solution()
for row in sol.generate(rows=6):  # Write out every line
    print(f"{str(row):^20}")
print(sol.generate(rows=6))  # Print the list