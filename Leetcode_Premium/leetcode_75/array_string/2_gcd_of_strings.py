"""
For two strings s and t, we say "t divides s" if and only if 
s = t + ... + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that 
x divides both str1 and str2.

"""
from math import gcd


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # To have a GCD, the following condition must be satisfied
        if str1 + str2 != str2 + str1:
            return ""

        # Else, find the GCD based on the size of both the strings
        # and that is the length of the GCD
        return str1[: gcd(len(str1), len(str2))]


sol = Solution()
print(sol.gcdOfStrings("ABCABC", "ABC"))
