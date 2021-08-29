class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        The idea is to check palindrome for each character by considering it as the center of the substring and expanding
        outwards
        Time complexity: O(n^2)

        Brute Force: O(n^3)
        """

        output = ""
        out_len = 0

        for i in range(len(s)):
            # First check for odd length palindromes
            left, right = i, i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                # Check if the current palindrome length is greater than what we've already found
                if right - left + 1 > out_len:
                    output = s[left : right + 1]
                    out_len = right - left + 1

                # Expand the substring outwards
                left -= 1
                right += 1

            # Again, do the same thing to get even length palindromes
            left, right = i, i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                # Check if the current palindrome length is greater than what we've already found
                if right - left + 1 > out_len:
                    output = s[left : right + 1]
                    out_len = right - left + 1

                # Expand the substring outwards
                left -= 1
                right += 1

        return output
