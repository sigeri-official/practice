# Leetcode problem: https://leetcode.com/problems/string-to-integer-atoi/
# Difficulty: Medium
# Runtime beat: 100.00%
# Memory beat: 95.48%

class Solution:
    def myAtoi(self, s):
        def validate(nm, trshld = pow(2, 31)):  # Limiting the number to 32 bit
            if -trshld > nm:
                return -trshld  # Lower treshold
            if nm > trshld-1:
                return trshld-1  # Upper treshold
            else:
                return nm  # Default state, under the treshold
        formatted_s = ''
        changed_sign = False
        sign = True  # +/-
        for c in s:
            if formatted_s != '' and not c.isdigit():  # If we have min 1 char and c is not a digit
                return validate(int(formatted_s) if sign else -int(formatted_s))
            if c == ' ' and changed_sign:  # If c is a space and sign was changed
                return 0
            elif not (c.isdigit() or c == '-' or c == '+' or c == ' '):  # It is not starting with a number/-/+/space
                return 0
            elif c == '-' or c == '+':  # Recognize the sign
                if not changed_sign:  # Runs at the first change
                    sign = False if c == '-' else True
                else:  # Already changed and wanted to change again
                    return 0
                changed_sign = True
            elif c.isdigit():  # If c is a valid char / digit
                formatted_s += c

        try: num = int(formatted_s)  # Try to convert the string to integer
        except: num = 0
        num = num if sign else -num  # Applying the sign
        return validate(num)  # Validate and return the number


sol = Solution()
print(sol.myAtoi("42"))  # Call myAtoi function
