"""
Given two strings s and t, return true if they are both one edit distance apart, otherwise return false.
One operation can be either a delete, an insert, or a replacement
"""


class Solution:
    def editDistance(self, word1: str, word2: str) -> int:
        """
        Returns the min number of operations required to convert "word1" to "word2"
        Dynamic programming problem - LEETCODE HARD
        Example: If word1 = "abd" and word2 = "acd", the answer should be 1 as only one operation (replace b with c) is required
        Use two pointers i and j to traverse through both the strings
        Two cases:
            1. Chars at i and j match -- means we don't need any operation
                - So, just move to the next indices (i+1, j+1)
            2. Chars do not match -- need to apply one of the three operations
                a. Insert:
                    - If you insert a char to word1, then for next round your i pointer remains the same while j moves ahead by 1 -- (i, j+1)
                b. Delete:
                    - If you delete a char in word1, then i -> i + 1 while j remains at the same position -- (i+1, j)
                c. Replace:
                    - For this operation, we are just replace the char in word1 with the char in word2 at position j
                    - So, updated pointers will be (i+1, j+1) but at the cost of one operation like the above two

        - Use a 2D caching array that stores the number of operations required for each substring

            a   b   d
        a               3
        c               2
        d               1
            3   2   1   0

        In the above matrix, we look at each row and column and see how many operations are required to convert string in the row to string in the column
        - For example, substring on the 4th column (row 0) is empty and to convert it to substring "acd", we need 3 insert operations (it is one of the base cases)
        """
        cache = [
            [float("inf") for i in range(len(word2) + 1)] for j in range(len(word1) + 1)
        ]
        # Add base cases to bottom row and last column
        for j in range(len(word2) + 1):
            cache[len(word1)][j] = len(word2) - j
        for i in range(len(word1) + 1):
            cache[i][len(word2)] = len(word1) - i

        # Use bottom up approach to fill the table
        for row in range(len(word1) - 1, -1, -1):
            for col in range(len(word2) - 1, -1, -1):
                if word1[row] == word2[col]:
                    cache[row][col] = cache[row + 1][col + 1]
                else:
                    cache[row][col] = 1 + min(
                        cache[row + 1][col],
                        cache[row][col + 1],
                        cache[row + 1][col + 1],
                    )

        return cache[0][0]

    def isOneEditDistance(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            # We want to make sure that the first string is of smaller length
            # This will make our if conditions easier to code and understand
            return self.isOneEditDistance(t, s)

        for i in range(len(s)):
            if s[i] != t[i]:
                # Two cases:
                # a. If both strings are of same length, the remaining substring must match
                # as we can only replace the unmatched characters
                if len(s) == len(t):
                    return s[i + 1 :] == t[i + 1 :]
                # Else, we can add one char at index i to make them match
                else:
                    return s[i:] == t[i + 1 :]

        # At the end, we want to make sure that the lengths of the strings actually only differ by 1 to satisfy the DELETE operation
        return len(s) + 1 == len(t)
