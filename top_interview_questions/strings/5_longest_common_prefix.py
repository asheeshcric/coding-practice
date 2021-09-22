"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

U:
M:
P:
1. First, sort the list based on ascending order of the length of each string
2. Use the first string as the starting point and start finding intersection with other strings
3. The intersection keeps getting updated as we move forward matching more strings
4. At the end, return the common string if any intersection was found, else return ""

"""


from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort(key=lambda s: len(s))
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]

        common = strs[0]
        found = False
        for i in range(1, len(strs)):
            intersection = ""
            word = strs[i]
            for j, char in enumerate(common):
                if char == word[j]:
                    found = True
                    intersection += char
                else:
                    break

            common = intersection

        return common if found else ""
