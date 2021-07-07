"""
A message containing letters from A-Z can be encoded into numbers using the following mapping:

'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). 
For example, "11106" can be mapped into:

"AAJF" with the grouping (1 1 10 6)
"KJF" with the grouping (11 10 6)
Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".

Given a string s containing only digits, return the number of ways to decode it.

Range of any letter: 1-26
"""


def decode_ways(s, dp, n):
    if len(s[n - 1 :]) == 0:
        return 1

    if s[n - 1] == "0":
        return 0

    if len(s[n - 1 :]) == 1:
        return 1

    if dp[n] is not None:
        return dp[n]

    if int(s[n - 1]) <= 2 and int(s[n - 1 : n + 1]) <= 26:
        # Two ways to decode
        dp[n] = decode_ways(s, dp, n + 1) + decode_ways(s, dp, n + 2)
    else:
        # Only one way to decode
        dp[n] = decode_ways(s, dp, n + 1)

    return dp[n]


if __name__ == "__main__":
    s = "226"
    dp = [None] * (len(s) + 1)
    dp[0] = 1
    print(decode_ways(s, dp, n=1))
