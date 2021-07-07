"""
Given a string s, return the longest palindromic substring in s.

# For each char in the string expand it outwards until it remains a palindrome and keep updating your result
1. Check for odd palindromes first
2. Check for even palindromes then
"""


def longest_palindrome(s):
    result = ""
    max_len = 0

    for i in range(len(s)):
        # Check for odd palindrome
        left, right = i, i
        while left >= 0 and right < len(s) and s[left] == s[right]:
            new_palindrome = s[left : right + 1]
            new_len = right - left + 1
            if new_len > max_len:
                result = new_palindrome
                max_len = new_len
            left -= 1
            right += 1

        # Check for even palindrome
        left, right = i, i + 1
        while left >= 0 and right < len(s) and s[left] == s[right]:
            new_palindrome = s[left : right + 1]
            new_len = right - left + 1
            if new_len > max_len:
                result = new_palindrome
                max_len = new_len
            left -= 1
            right += 1

    return result


if __name__ == "__main__":
    s = "babad"
    print(longest_palindrome(s))
