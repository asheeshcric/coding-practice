"""
Given two sequences, find the length of longest subsequence present in both of them. A subsequence is a sequence that appears in the same relative order, 
but not necessarily contiguous.
For example, “abc”, “abg”, “bdf”, “aeg”, ‘”acefg”, .. etc are subsequences of “abcdefg”

"""


def LCS(x, y, m, n):
    if m <= 0 or n <= 0:
        return 0

    if x[m - 1] == y[n - 1]:
        return 1 + LCS(x, y, m - 1, n - 1)
    else:
        return max(LCS(x, y, m - 1, n), LCS(x, y, m, n - 1))


if __name__ == "__main__":
    x = "abcde"
    y = "ace"
    print(LCS(x, y, len(x), len(y)))
