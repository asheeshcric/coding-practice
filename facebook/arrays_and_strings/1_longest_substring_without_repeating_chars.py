class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen_chars = {}
        max_length = 0
        current_length = 0
        last_valid_index = -1
        for i, char in enumerate(s):
            if char in seen_chars and seen_chars[char] >= last_valid_index:
                current_length = i - seen_chars[char]
                last_valid_index = seen_chars[char] + 1
            else:
                current_length += 1
            
            seen_chars[char] = i

            max_length = max(max_length, current_length)

        return max_length