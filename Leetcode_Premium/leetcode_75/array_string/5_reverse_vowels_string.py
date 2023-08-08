"""
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once

"""


class Solution:
    # Can also use a two-pointer approach
    def reverseVowels(self, s: str) -> str:
        chars = list(s)
        vowels = dict()
        print(chars)
        for i, char in enumerate(chars):
            if char.lower() in ["a", "e", "i", "o", "u"]:
                vowels[i] = char

        # Reverse the vowels
        vowel_ids = list(vowels.keys())
        print(vowels)
        for i, id in enumerate(reversed(vowel_ids)):
            chars[id] = s[vowel_ids[i]]

        return "".join(chars)


sol = Solution()
print(sol.reverseVowels("somestring"))
