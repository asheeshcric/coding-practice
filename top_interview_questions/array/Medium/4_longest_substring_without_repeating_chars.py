from typing import MutableSequence


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)

        """
        Just keep track of the last valid index (as in the char which got repeated by the current char)
        Whenever you find a repeating char, update the last_valid_idx
        """

        seen_chars = dict()
        max_length = 0
        curr_length = 0
        last_valid_idx = -1
        for i, char in enumerate(s):
            if char in seen_chars and seen_chars[char] >= last_valid_idx:
                # This means we've found a repeating char
                curr_length = i - seen_chars[char]
                last_valid_idx = seen_chars[char] + 1
            else:
                curr_length += 1

            seen_chars[char] = i
            max_length = max(max_length, curr_length)

        return max_length
