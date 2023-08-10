"""
Given an array of characters chars, compress it using the following algorithm:

Begin with an empty string s. For each group of consecutive repeating characters in chars:

If the group's length is 1, append the character to s.
Otherwise, append the character followed by the group's length.
The compressed string s should not be returned separately, but instead, be stored in the input character array chars. 
Note that group lengths that are 10 or longer will be split into multiple characters in chars.

After you are done modifying the input array, return the new length of the array.

You must write an algorithm that uses only constant extra space.

"""
from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) < 2:
            return len(chars)

        # we start from the first element of the array
        # "index" variable keeps track of where to put the element and its count and will also be the length of the final array
        start, index = 0, 0
        while start < len(chars):
            end = start
            while end < len(chars) and chars[end] == chars[start]:
                # This loop just counts the frequecy of the current char
                end += 1

            chars[index] = chars[start]
            index += 1
            if end - start > 1:
                for digit in str(end - start):
                    chars[index] = digit
                    index += 1

            start = end

        print(chars)
        chars = chars[:index]

        return index


sol = Solution()
print(sol.compress(["a", "a", "a", "b", "b", "a", "a"]))
