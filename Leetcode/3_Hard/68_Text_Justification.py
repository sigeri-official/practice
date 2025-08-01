# Leetcode problem: https://leetcode.com/problems/text-justification
# Difficulty: Hard
# Runtime beat: 100.00%
# Memory beat: 62.86%
# © Sigeri

class Solution:
    def justify(self, row, maxW):
        length = len("".join(row))
        spaces = 0
        free = 0
        if len(row) != 1:
            spaces = (maxW - length) // (len(row)-1)
            free = (maxW - length) % (len(row)-1)
        else:
            free = maxW - len(row[0])
        text = ""
        for i in range(len(row)-1):
            spaces_per_word = spaces
            if free != 0:
                spaces_per_word += 1
                free -= 1
            text += str(row[i])+" "*spaces_per_word
        text += row[-1] if len(row) != 1 else row[0]+" "*free
        return text
    def fullJustify(self, words, maxWidth):
        matrix = []
        row_list = []
        for i, word in enumerate(words):
            if sum([len(i) for i in list(row_list + [word])]) + len(row_list) <= maxWidth:
                row_list.append(word)
                if i == len(words)-1:
                    matrix.append(row_list)
            else:
                matrix.append(row_list)
                row_list = [word]
                if i == len(words)-1:
                    matrix.append([word])
        for i in range(len(matrix)):
            matrix[i] = self.justify(matrix[i], maxWidth)
        for i in range(len(matrix[-1])):
            matrix[-1] = self.justify([matrix[-1].replace('  ', ' ')], maxWidth)
        return matrix


sol = Solution()
print(sol.justify(["justification."], 18))
print(sol.fullJustify(words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16))
