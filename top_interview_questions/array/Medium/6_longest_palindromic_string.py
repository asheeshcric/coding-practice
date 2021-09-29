class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        max_len = 0
        output = ""
        for i in range(n):
            # From each index, expand outwards to check palindromes
            # Check for both odd and even length palindromes

            odd_palindrome = self.findPalindrome(i, i, n, s)
            even_palindrome = self.findPalindrome(i, i + 1, n, s)
            if len(odd_palindrome) > max_len:
                output, max_len = odd_palindrome, len(odd_palindrome)
            if len(even_palindrome) > max_len:
                output, max_len = even_palindrome, len(even_palindrome)

        return output

    def findPalindrome(self, left, right, n, s):
        """
        Finding palindrome by expanding outwards from current index
        """
        while left >= 0 and right < n:
            if s[left] != s[right]:
                break
            left -= 1
            right += 1

        result = s[left + 1 : right]
        return result
