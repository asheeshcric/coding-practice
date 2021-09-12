"""
Given a string s, return true if the s can be palindrome after deleting at most one character from it

1. Start by checking for palindrome in the normal way
2. If two chars don't match, you've two options:
    a. Delete the char on the left
    b. Delete the char on the right
3. Even after deleting, if two chars don't match, then it can't be a valid palindrome.

"""


class Solution:
    def validPalindrome(self, s: str, deleted=False) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                if deleted:
                    return False
                else:
                    # We have an option to delete a char: either on the left or on the right
                    # Deleting left char
                    if self.validPalindrome(s[left + 1 : right + 1], deleted=True):
                        return True
                    else:
                        return self.validPalindrome(s[left:right], deleted=True)

            left += 1
            right -= 1

        return True
