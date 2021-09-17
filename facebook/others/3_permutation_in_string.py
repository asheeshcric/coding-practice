"""
Same as finding all anagrams of a string, just return True once you find the first anagram
"""


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s, p = s2, s1
        if len(s) < len(p):
            return []

        counts, window = dict(), dict()
        for char in p:
            counts[char] = counts.get(char, 0) + 1

        left = 0
        need, have = len(counts), 0
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
                return True

        return False
