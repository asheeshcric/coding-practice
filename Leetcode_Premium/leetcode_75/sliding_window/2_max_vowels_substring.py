"""
Given a string s and an integer k, 

return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

"""


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        """
        Again, use a sliding window to keep track of how many vowels are in current window
        As you move the window, check the removed and the added letter to change the vowel
        count
        """
        start = 0
        vowels = {"a", "e", "i", "o", "u"}
        max_vowels = 0
        while start + k <= len(s):
            if start == 0:
                vowel_count = 0
                for char in s[start : start + k]:
                    if char.lower() in vowels:
                        vowel_count += 1

            else:
                if s[start - 1] in vowels:
                    vowel_count -= 1
                if s[start + k - 1] in vowels:
                    vowel_count += 1

            max_vowels = max(max_vowels, vowel_count)
            start += 1

        return max_vowels
