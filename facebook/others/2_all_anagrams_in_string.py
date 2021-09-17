"""
Given two strings s and p, return an array of all the start indices of p's anagrams in s.

You may return the answer in any order.

Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
"""
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []

        counts, window = dict(), dict()
        for char in p:
            counts[char] = counts.get(char, 0) + 1

        left = 0
        need, have = len(counts), 0
        output = []
        for right, char in enumerate(s):
            # We start adding letters to the window
            window[char] = window.get(char, 0) + 1

            if char in counts and window[char] == counts[char]:
                have += 1

            if right >= len(p):
                # This means our window size becomes greater than p. So, start removing letters from the left
                if window[s[left]] == 1:
                    window.pop(s[left])
                else:
                    window[s[left]] -= 1
                
                # We need to check if the last char taken disrupts our already formed anagram or not
                if s[left] in counts and window.get(s[left], 0)+1 == counts[s[left]]:
                    have -= 1

                left += 1

            if have == need:
                output.append(left)

        return output
