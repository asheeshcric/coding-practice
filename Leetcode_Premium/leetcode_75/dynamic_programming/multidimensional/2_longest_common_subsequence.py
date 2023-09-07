"""
Given two strings text1 and text2, return the length of their longest common subsequence. 
If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters 
(can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.

"""


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # First, create a 2D matrix of size (m+1)x(n+1)
        # The last row and col are dummy cells with zero values
        # At each cell, we have two conditions: (a) Letters match (b) Don't

        lcs = [[0 for col in range(len(text2) + 1)] for row in range(len(text1) + 1)]

        for row in range(len(text1) - 1, -1, -1):
            for col in range(len(text2) - 1, -1, -1):
                if text1[row] == text2[col]:
                    # It's a match and we can increase the LCS count
                    lcs[row][col] = 1 + lcs[row + 1][col + 1]
                else:
                    lcs[row][col] = max(lcs[row + 1][col], lcs[row][col + 1])

        return lcs[0][0]
