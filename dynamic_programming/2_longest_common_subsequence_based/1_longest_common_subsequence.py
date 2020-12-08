"""
Given two sequences, find the length of longest subsequence present in both of them. A subsequence is a sequence 
that appears in the same relative order, but not necessarily contiguous. 
For example, “abc”, “abg”, “bdf”, “aeg”, ‘”acefg”, .. etc are subsequences of “abcdefg”.

Examples:
LCS for input Sequences “ABCDGH” and “AEDFHR” is “ADH” of length 3.
LCS for input Sequences “AGGTAB” and “GXTXAYB” is “GTAB” of length 4.
"""

def lcs(x, y, n, m):
    # Base condition
    if n == 0 or m == 0:
        return 0

    # First check if the last chars match in both strings
    if x[n-1] == y[m-1]:
        return 1 + lcs(x, y, n-1, m-1)

    else:
        # Select the one with max LCS
        return max(lcs(x, y, n-1, m), lcs(x, y, n, m-1))


if __name__ == '__main__':
    x = 'ABCDGH'
    y = 'AEDFHR'
    n, m = len(x), len(y)
    print(lcs(x.lower(), y.lower(), n, m))