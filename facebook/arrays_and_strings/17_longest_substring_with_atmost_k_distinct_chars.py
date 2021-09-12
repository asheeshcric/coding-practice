"""
Given a string s and an integer k, return the length of the longest substring of s that contains at most k distinct characters.

Input: s = "eceba", k = 2
Output: 3
Explanation: The substring is "ece" with length 3.
"""


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        # Base cases
        if len(s) == 0 or k == 0:
            return 0

        # Use two pointers for sliding window approach
        left, right = 0, 0
        window = dict()
        res_len = 0
        # We traverse through the string until our right pointer reaches the end
        # Every time our window contains k distinct chars, we move the left pointer forward
        while right < len(s):
            char = s[right]
            window[char] = window.get(char, 0) + 1
            while len(window) > k:
                # We keep popping chars from the left of the window
                left_char = s[left]
                if window[left_char] == 1:
                    window.pop(left_char)
                else:
                    window[left_char] -= 1

                left += 1

            res_len = max(right - left + 1, res_len)
            right += 1

        return res_len